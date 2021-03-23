import connexion
import six

from database_service.models.inline_response2011 import InlineResponse2011  # noqa: E501
from database_service.models.order import Order  # noqa: E501
from database_service.models.orders import Orders  # noqa: E501
from database_service import util


def apiorder_fetch_order(exchange_name, id, start_date=None, end_date=None):  # noqa: E501
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


def apiorder_fetch_order_by_id(exchange_name, order_id):  # noqa: E501
    """Fetch order by its id

     # noqa: E501

    :param exchange_name: 
    :type exchange_name: str
    :param order_id: 
    :type order_id: str

    :rtype: Order
    """
    return 'do some magic!'


def apiorder_insert_order(body, exchange_name):  # noqa: E501
    """Create new order entry

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param exchange_name: 
    :type exchange_name: str

    :rtype: InlineResponse2011
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
