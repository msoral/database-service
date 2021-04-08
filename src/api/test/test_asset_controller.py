# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from src.api.models.asset import Asset  # noqa: E501
from src.api.models.asset_indicators import AssetIndicators  # noqa: E501
from src.api.models.asset_metadata import AssetMetadata  # noqa: E501
from src.api.models.inline_response201 import InlineResponse201  # noqa: E501
from src.api.test import BaseTestCase


class TestAssetController(BaseTestCase):
    """AssetController integration test stubs"""

    def test_fetch_asset(self):
        """Test case for fetch_asset

        Returns a list of asset metadata.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/assets',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_indicators(self):
        """Test case for fetch_indicators

        Returns technical indicators of a given asset for the specified timeperiod.
        """
        query_string = [('id', 56),
                        ('start_date', '2013-10-20'),
                        ('end_date', '2013-10-20')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/assets/indicators',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_price(self):
        """Test case for fetch_price

        Returns ochlv + market cap values for an asset.
        """
        query_string = [('id', 56),
                        ('start_date', '2013-10-20'),
                        ('end_date', '2013-10-20')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/assets/price',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_asset(self):
        """Test case for insert_asset

        Create a new asset, provide as many social links as possible.
        """
        asset_metadata = {
  "ticker" : "ticker",
  "website" : "website",
  "social_links" : {
    "twitter" : "",
    "reddit" : "",
    "facebook" : ""
  },
  "name" : "name",
  "id" : 0
}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/assets',
            method='POST',
            headers=headers,
            data=json.dumps(asset_metadata),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_price(self):
        """Test case for insert_price

        Create new price data entry for an asset.
        """
        asset = {
  "volume" : 0.8008282,
  "marketcap" : 6.0274563,
  "high" : 48132.12,
  "low" : 40122.12,
  "assetId" : 1,
  "close" : 46132.12,
  "open" : 45832.12,
  "timestamp" : 1616414075.621394
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/assets/price',
            method='POST',
            headers=headers,
            data=json.dumps(asset),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
