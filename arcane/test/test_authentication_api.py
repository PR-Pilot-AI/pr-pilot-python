# coding: utf-8

"""
    Arcane Engine API

    API for creating Arcane Engine tasks

    The version of the OpenAPI document: 1.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from arcane.api.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthenticationApi()

    def tearDown(self) -> None:
        pass

    def test_exchange_github_token_create(self) -> None:
        """Test case for exchange_github_token_create

        """
        pass


if __name__ == '__main__':
    unittest.main()
