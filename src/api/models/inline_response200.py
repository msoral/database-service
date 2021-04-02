# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from src.api.models.base_model_ import Model
from src.api import util

from src.api.models import InlineResponse200Assets  # noqa: E501

class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, timestamp=None, assets=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param timestamp: The timestamp of this InlineResponse200.  # noqa: E501
        :type timestamp: float
        :param assets: The assets of this InlineResponse200.  # noqa: E501
        :type assets: List[InlineResponse200Assets]
        """
        self.openapi_types = {
            'timestamp': float,
            'assets': List[InlineResponse200Assets]
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'assets': 'assets'
        }

        self._timestamp = timestamp
        self._assets = assets

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse200.


        :return: The timestamp of this InlineResponse200.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse200.


        :param timestamp: The timestamp of this InlineResponse200.
        :type timestamp: float
        """

        self._timestamp = timestamp

    @property
    def assets(self):
        """Gets the assets of this InlineResponse200.


        :return: The assets of this InlineResponse200.
        :rtype: List[InlineResponse200Assets]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this InlineResponse200.


        :param assets: The assets of this InlineResponse200.
        :type assets: List[InlineResponse200Assets]
        """

        self._assets = assets