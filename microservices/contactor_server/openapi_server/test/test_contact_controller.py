# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.models.late_borrowers import LateBorrowers  # noqa: E501
from openapi_server.test import BaseTestCase


class TestContactController(BaseTestCase):
    """ContactController integration test stubs"""

    def test_get_late(self):
        """Test case for get_late

        
        """
        query_string = [('limit', 56),
                        ('offset', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contact',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_db(self):
        """Test case for update_db

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contact/update',
            method='PATCH',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
