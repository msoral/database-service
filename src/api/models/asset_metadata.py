# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from src.api.models.base_model_ import Model
from src.api import util


class AssetMetadata(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, ticker=None, website=None, social_links=None):  # noqa: E501
        """AssetMetadata - a model defined in OpenAPI

        :param id: The id of this AssetMetadata.  # noqa: E501
        :type id: int
        :param name: The name of this AssetMetadata.  # noqa: E501
        :type name: str
        :param ticker: The ticker of this AssetMetadata.  # noqa: E501
        :type ticker: str
        :param website: The website of this AssetMetadata.  # noqa: E501
        :type website: str
        :param social_links: The social_links of this AssetMetadata.  # noqa: E501
        :type social_links: Dict[str, str]
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'ticker': str,
            'website': str,
            'social_links': Dict[str, str]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'ticker': 'ticker',
            'website': 'website',
            'social_links': 'social_links'
        }

        self._id = id
        self._name = name
        self._ticker = ticker
        self._website = website
        self._social_links = social_links

    @classmethod
    def from_dict(cls, dikt) -> 'AssetMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssetMetadata of this AssetMetadata.  # noqa: E501
        :rtype: AssetMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this AssetMetadata.


        :return: The id of this AssetMetadata.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetMetadata.


        :param id: The id of this AssetMetadata.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssetMetadata.


        :return: The name of this AssetMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetMetadata.


        :param name: The name of this AssetMetadata.
        :type name: str
        """

        self._name = name

    @property
    def ticker(self):
        """Gets the ticker of this AssetMetadata.


        :return: The ticker of this AssetMetadata.
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this AssetMetadata.


        :param ticker: The ticker of this AssetMetadata.
        :type ticker: str
        """

        self._ticker = ticker

    @property
    def website(self):
        """Gets the website of this AssetMetadata.


        :return: The website of this AssetMetadata.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this AssetMetadata.


        :param website: The website of this AssetMetadata.
        :type website: str
        """

        self._website = website

    @property
    def social_links(self):
        """Gets the social_links of this AssetMetadata.


        :return: The social_links of this AssetMetadata.
        :rtype: Dict[str, str]
        """
        return self._social_links

    @social_links.setter
    def social_links(self, social_links):
        """Sets the social_links of this AssetMetadata.


        :param social_links: The social_links of this AssetMetadata.
        :type social_links: Dict[str, str]
        """

        self._social_links = social_links