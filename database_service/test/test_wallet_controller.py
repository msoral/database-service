# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from database_service.models.inline_response200 import InlineResponse200  # noqa: E501
from database_service.test import BaseTestCase


class TestWalletController(BaseTestCase):
    """WalletController integration test stubs"""

    def test_apiwallet_fetch_funds(self):
        """Test case for apiwallet_fetch_funds

        Get amount of available funds
        """
        response = self.client.open(
            '/wallet/funds',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apiwallet_fetch_holdings(self):
        """Test case for apiwallet_fetch_holdings

        Get current portfolio holdings
        """
        response = self.client.open(
            '/wallet',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apiwallet_fetch_total(self):
        """Test case for apiwallet_fetch_total

        Get dollar equavalent of current holdings.
        """
        response = self.client.open(
            '/wallet/total',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
