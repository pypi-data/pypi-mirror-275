import pytest

from regscale.core.app.utils.app_utils import get_current_datetime
from regscale.models import Search
from regscale.models.regscale_models.asset import Asset


# Can we create an instance of the Asset class?
def test_asset_instance():
    asset = Asset(
        host_name="host.example.com",
        name="Host Name",
        type="Other",
        ipAddress="1.1.1.1",
        parentId=1,
        parentModule="securityplans",
        assetOwnerId="asdfasdf",
        status="Active (On Network)",
        assetType="Virtual Machine (VM)",
        dateCreated=get_current_datetime(),
        dateLastUpdated=get_current_datetime(),
        createdById="asdfasdf",
        lastUpdatedById="asdfasdf",
        assetCategory="Hardware",
        scanningTool="Rando Scanner",
        isPublic=True,
        tenantsId=0,
    )
    assert isinstance(asset, Asset)


def test_bad_asset():
    asset = Asset(
        host_name="host.example.com",
        name="Host Name",
        type="Other",
        ipAddress="1.1.1.1",
        parentId=1,
        parentModule="securityplans",
        assetOwnerId="asdfasdf",
        status="Active (On Network)",
        assetType="Virtual Machine (VM)",
        dateCreated=get_current_datetime(),
        dateLastUpdated=get_current_datetime(),
        createdById="asdfasdf",
        lastUpdatedById="asdfasdf",
        assetCategory="Hardware",
        scanningTool="Rando Scanner",
        isPublic=True,
        tenantsId=0,
        fqdn=0,  # Bad attribute
    )
    # Check if an attribute error is raised
    with pytest.raises(AttributeError):
        asset.model_fields_set


def test_assets_by_search():
    empty_search = Search(parentID=4, module="securityplans", sort="id")
    search = Search(parentID=3, module="securityplans", sort="id")
    # this will return an empty list
    no_assets = Asset.get_all_by_search(empty_search)
    assets = Asset.get_all_by_search(search)
    assert no_assets == []
    assert len(assets) > 0
