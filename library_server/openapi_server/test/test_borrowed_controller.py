# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.borrow_book import BorrowBook  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.test import BaseTestCase


class TestBorrowedController(BaseTestCase):
    """BorrowedController integration test stubs"""

    def test_borrow_book(self):
        """Test case for borrow_book

        
        """
        borrow_book = openapi_server.BorrowBook()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/borrow/add',
            method='POST',
            headers=headers,
            data=json.dumps(borrow_book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_borrowed_book(self):
        """Test case for get_borrowed_book

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/borrow/{book_name}'.format(book_name='book_name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_borrowed_list(self):
        """Test case for get_borrowed_list

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/borrow',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_borrowed_book(self):
        """Test case for remove_borrowed_book

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/borrow/{book_name}'.format(book_name='book_name_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
