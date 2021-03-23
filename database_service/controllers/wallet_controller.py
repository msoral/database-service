import connexion
import six

from database_service.models.inline_response200 import InlineResponse200  # noqa: E501
from database_service import util


def apiwallet_fetch_funds():  # noqa: E501
    """Get amount of available funds

     # noqa: E501


    :rtype: float
    """
    return 'do some magic!'


def apiwallet_fetch_holdings():  # noqa: E501
    """Get current portfolio holdings

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def apiwallet_fetch_total():  # noqa: E501
    """Get dollar equavalent of current holdings.

     # noqa: E501


    :rtype: float
    """
    return 'do some magic!'
