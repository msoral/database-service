# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from src.api.models.wallet import Wallet  # noqa: E501
from src.api.test import BaseTestCase


class TestWalletController(BaseTestCase):
    """WalletController integration test stubs"""

    def test_fetch_funds(self):
        """Test case for fetch_funds

        Get amount of available funds
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/wallet/funds',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_holdings(self):
        """Test case for fetch_holdings

        Get current portfolio holdings
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/wallet',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_total(self):
        """Test case for fetch_total

        Get dollar equavalent of current holdings.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/wallet/total',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
