# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from src.api.models.inline_response2011 import InlineResponse2011  # noqa: E501
from src.api.models.order import Order  # noqa: E501
from src.api.models.orders import Orders  # noqa: E501
from src.api.test import BaseTestCase


class TestOrderController(BaseTestCase):
    """OrderController integration test stubs"""

    def test_fetch_order(self):
        """Test case for fetch_order

        Fetch order entry
        """
        query_string = [('id', 56),
                        ('start_date', '2013-10-20'),
                        ('end_date', '2013-10-20')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/orders',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_order_by_id(self):
        """Test case for fetch_order_by_id

        Fetch order by its id
        """
        query_string = [('order id', 'order_id_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/orders/by_id',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_order(self):
        """Test case for insert_order

        Create new order entry
        """
        order = {
  "symbol" : "symbol",
  "side" : "side",
  "quantity" : 6.027456183070403,
  "stop_price" : 5,
  "optional_parameters" : {
    "key" : "{}"
  },
  "price" : 1,
  "id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "order_type" : "{}",
  "timeInForce" : "timeInForce",
  "timestamp" : 0.8008282,
  "status" : "status"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/orders',
            method='POST',
            headers=headers,
            data=json.dumps(order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
