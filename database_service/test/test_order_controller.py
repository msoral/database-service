# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from database_service.models.inline_response2011 import InlineResponse2011  # noqa: E501
from database_service.models.order import Order  # noqa: E501
from database_service.models.orders import Orders  # noqa: E501
from database_service.test import BaseTestCase


class TestOrderController(BaseTestCase):
    """OrderController integration test stubs"""

    def test_apiorder_fetch_order(self):
        """Test case for apiorder_fetch_order

        Fetch order entry
        """
        query_string = [('id', 789),
                        ('start_date', '2013-10-20'),
                        ('end_date', '2013-10-20')]
        headers = [('exchange_name', 'exchange_name_example')]
        response = self.client.open(
            '/orders',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apiorder_fetch_order_by_id(self):
        """Test case for apiorder_fetch_order_by_id

        Fetch order by its id
        """
        query_string = [('order_id', 'order_id_example')]
        headers = [('exchange_name', 'exchange_name_example')]
        response = self.client.open(
            '/orders/by_id',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_apiorder_insert_order(self):
        """Test case for apiorder_insert_order

        Create new order entry
        """
        body = Order()
        headers = [('exchange_name', 'exchange_name_example')]
        response = self.client.open(
            '/orders',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
