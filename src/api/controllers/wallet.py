import connexion
import six

from src.api.models.wallet import Wallet  # noqa: E501
from src.api import util


def fetch_funds():  # noqa: E501
    """Get amount of available funds

     # noqa: E501


    :rtype: float
    """
    return 'do some magic!'


def fetch_holdings():  # noqa: E501
    """Get current portfolio holdings

     # noqa: E501


    :rtype: Wallet
    """
    return 'do some magic!'


def fetch_total():  # noqa: E501
    """Get dollar equavalent of current holdings.

     # noqa: E501


    :rtype: float
    """
    return 'do some magic!'
