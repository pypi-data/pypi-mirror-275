#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Model for Leveraged Authorizations in the application """

from typing import Optional
from urllib.parse import urljoin

from pydantic import field_validator, Field, ConfigDict

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.utils.app_utils import get_current_datetime
from .regscale_model import RegScaleModel


class LeveragedAuthorization(RegScaleModel):
    """LeveragedAuthorizations model."""

    _module_slug = "leveraged-authorization"
    _get_objects_for_list = True

    id: Optional[int] = 0
    isPublic: Optional[bool] = True
    uuid: Optional[str] = None
    title: str
    fedrampId: Optional[str] = None
    ownerId: str
    securityPlanId: int
    dateAuthorized: str
    description: Optional[str] = None
    dataTypes: Optional[str] = None
    servicesUsed: Optional[str] = None
    authenticationType: Optional[str] = None
    authorizedUserTypes: Optional[str] = None
    impactLevel: Optional[str] = None
    natureOfAgreement: Optional[str] = None
    authorizationType: Optional[str] = None  # not to be confused with authenticationType
    securityPlanLink: Optional[str] = ""
    crmLink: Optional[str] = ""
    responsibilityAndInheritanceLink: Optional[str] = ""
    createdById: str = Field(default_factory=RegScaleModel._api_handler.get_user_id)
    dateCreated: Optional[str] = Field(default_factory=get_current_datetime)
    lastUpdatedById: str = Field(default_factory=RegScaleModel._api_handler.get_user_id)
    dateLastUpdated: Optional[str] = Field(default_factory=get_current_datetime)
    tenantsId: Optional[int] = 1

    @staticmethod
    def _get_additional_endpoints() -> ConfigDict:
        """
        Get additional endpoints for the PortsProtocols model.

        :return: A dictionary of additional endpoints
        :rtype: ConfigDict
        """
        return ConfigDict(  # type: ignore
            get_all_by_parent="/api/{model_slug}/getAllByParent/{intParentID}",
        )

    @classmethod
    @field_validator(
        "crmLink",
        "responsibilityAndInheritanceLink",
        "securityPlanLink",
        mode="before",
        check_fields=True,
    )
    def validate_fields(cls, value: Optional[str]) -> str:
        """
        Validate the CRM link, responsibility and inheritance link, and security plan link.

        :param Optional[str] value: The field value.
        :return: The validated field value or empty string.
        :rtype: str
        """
        if not value:
            value = ""
        return value

    @staticmethod
    def insert_leveraged_authorizations(app: Application, leveraged_auth: "LeveragedAuthorization") -> dict:
        """
        Insert a leveraged authorization into the database.

        :param Application app: The application instance.
        :param LeveragedAuthorization leveraged_auth: The leveraged authorization to insert.
        :return: The response from the API or raise an exception
        :rtype: dict
        """
        api = Api()

        # Construct the URL by joining the domain and endpoint
        url = urljoin(app.config.get("domain"), "/api/leveraged-authorization")
        # Convert the Pydantic model to a dictionary
        data = leveraged_auth.dict()
        # Make the POST request to insert the data
        response = api.post(url, json=data)

        # Check for success and handle the response as needed
        return response.json() if response.ok else response.raise_for_status()
