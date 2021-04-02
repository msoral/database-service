import connexion

from src.api.models.inline_response2011 import InlineResponse2011  # noqa: E501
from src.api.models import Order  # noqa: E501
from src.api import util


def fetch_order(exchange_name, id, start_date=None, end_date=None):  # noqa: E501
    """Fetch order entry

     # noqa: E501

    :param exchange_name: 
    :type exchange_name: str
    :param id: Use /assets endpoint to get the id of the asset.
    :type id: int
    :param start_date: Must be used together with &#x60;end_date&#x60;. 
    :type start_date: str
    :param end_date: Must be used together with &#x60;start_date&#x60;. 
    :type end_date: str

    :rtype: Orders
    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return 'do some magic!'


def fetch_order_by_id(exchange_name, order_id):  # noqa: E501
    """Fetch order by its id

     # noqa: E501

    :param exchange_name: 
    :type exchange_name: str
    :param order_id: 
    :type order_id: str

    :rtype: Order
    """
    return 'do some magic!'


def insert_order(exchange_name, order):  # noqa: E501
    """Create new order entry

     # noqa: E501

    :param exchange_name: 
    :type exchange_name: str
    :param order: 
    :type order: dict | bytes

    :rtype: InlineResponse2011
    """
    if connexion.request.is_json:
        order = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
