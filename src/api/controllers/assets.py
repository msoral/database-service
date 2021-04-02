import connexion

from src.api.models.asset import Asset  # noqa: E501
from src.api.models.inline_response201 import InlineResponse201  # noqa: E501
from src.api import util


def fetch_indicators(id, exchange_name, start_date=None, end_date=None):  # noqa: E501
    """Returns technical indicators of a given asset for the specified timeperiod.

     # noqa: E501

    :param id: Use /assets endpoint to get the id of the asset.
    :type id: int
    :param exchange_name: 
    :type exchange_name: str
    :param start_date: Must be used together with &#x60;end_date&#x60;. 
    :type start_date: str
    :param end_date: Must be used together with &#x60;start_date&#x60;. 
    :type end_date: str

    :rtype: Dict[str, AssetIndicators]
    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return 'do some magic!'


def insert_asset():
    return 'do some magic!'


def fetch_asset(exchange_name):  # noqa: E501
    """List assets of an exchange

     # noqa: E501

    :param exchange_name: 
    :type exchange_name: str

    :rtype: List[AssetMetadata]
    """
    return 'do some magic!'


def fetch_price(exchange_name, id, start_date=None, end_date=None):  # noqa: E501
    """Returns ochlv + market cap values for an asset.

     # noqa: E501

    :param exchange_name: 
    :type exchange_name: str
    :param id: Use /assets endpoint to get the id of the asset.
    :type id: int
    :param start_date: Must be used together with &#x60;end_date&#x60;. 
    :type start_date: str
    :param end_date: Must be used together with &#x60;start_date&#x60;. 
    :type end_date: str

    :rtype: Dict[str, Asset]
    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return 'do some magic!'


def insert_price(asset):  # noqa: E501
    """Create a new asset object

    **Warning**: This endpoint creates an entry in the database.  # noqa: E501

    :param asset: Placeholder description
    :type asset: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        asset = Asset.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
