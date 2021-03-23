# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from database_service.models.base_model_ import Model
from database_service.models.order import Order  # noqa: F401,E501
from database_service import util


class Orders(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """Orders - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'Orders':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Orders of this Orders.  # noqa: E501
        :rtype: Orders
        """
        return util.deserialize_model(dikt, cls)