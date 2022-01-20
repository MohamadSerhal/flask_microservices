# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UserRegisterBody(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, username=None, password=None, full_name=None, type=None):  # noqa: E501
        """UserRegisterBody - a model defined in OpenAPI

        :param username: The username of this UserRegisterBody.  # noqa: E501
        :type username: str
        :param password: The password of this UserRegisterBody.  # noqa: E501
        :type password: str
        :param full_name: The full_name of this UserRegisterBody.  # noqa: E501
        :type full_name: str
        :param type: The type of this UserRegisterBody.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'username': str,
            'password': str,
            'full_name': str,
            'type': str
        }

        self.attribute_map = {
            'username': 'username',
            'password': 'password',
            'full_name': 'full_name',
            'type': 'type'
        }

        self._username = username
        self._password = password
        self._full_name = full_name
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'UserRegisterBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The userRegisterBody of this UserRegisterBody.  # noqa: E501
        :rtype: UserRegisterBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self):
        """Gets the username of this UserRegisterBody.


        :return: The username of this UserRegisterBody.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserRegisterBody.


        :param username: The username of this UserRegisterBody.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this UserRegisterBody.


        :return: The password of this UserRegisterBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserRegisterBody.


        :param password: The password of this UserRegisterBody.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def full_name(self):
        """Gets the full_name of this UserRegisterBody.


        :return: The full_name of this UserRegisterBody.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserRegisterBody.


        :param full_name: The full_name of this UserRegisterBody.
        :type full_name: str
        """

        self._full_name = full_name

    @property
    def type(self):
        """Gets the type of this UserRegisterBody.


        :return: The type of this UserRegisterBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserRegisterBody.


        :param type: The type of this UserRegisterBody.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type
