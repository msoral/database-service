# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from database_service.models.asset import Asset  # noqa: E501
from database_service.models.asset_indicators import AssetIndicators  # noqa: E501
from database_service.models.assets import Assets  # noqa: E501
from database_service.models.inline_response201 import InlineResponse201  # noqa: E501
from database_service.test import BaseTestCase


class TestAssetController(BaseTestCase):
    """AssetController integration test stubs"""

    def test_apiasset_fetch_indicators(self):
        """Test case for apiasset_fetch_indicators

        Returns technical indicators of a given asset for the specified timeperiod.
        """
        query_string = [('id', 789),
                        ('start_date', '2013-10-20'),
                        ('end_date', '2013-10-20')]
        headers = [('exchange_name', 'exchange_name_example')]
        response = self.client.open(
            '/assets/indicators',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apiasset_fetch_metadata(self):
        """Test case for apiasset_fetch_metadata

        List assets of an exchange
        """
        headers = [('exchange_name', 'exchange_name_example')]
        response = self.client.open(
            '/assets',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apiasset_fetch_price(self):
        """Test case for apiasset_fetch_price

        Returns ochlv + market cap values for an asset.
        """
        query_string = [('id', 789),
                        ('start_date', '2013-10-20'),
                        ('end_date', '2013-10-20')]
        headers = [('exchange_name', 'exchange_name_example')]
        response = self.client.open(
            '/assets/price',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apiasset_insert_price(self):
        """Test case for apiasset_insert_price

        Create a new asset object
        """
        body = Asset()
        response = self.client.open(
            '/assets/price',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
