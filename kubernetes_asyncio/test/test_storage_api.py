# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.13.5
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.storage_api import StorageApi  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestStorageApi(unittest.TestCase):
    """StorageApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.storage_api.StorageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
