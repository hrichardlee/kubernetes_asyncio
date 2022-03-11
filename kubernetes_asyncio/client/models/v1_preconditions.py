# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.21.7
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1Preconditions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'resource_version': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'resource_version': 'resourceVersion',
        'uid': 'uid'
    }

    def __init__(self, resource_version=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """V1Preconditions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._resource_version = None
        self._uid = None
        self.discriminator = None

        if resource_version is not None:
            self.resource_version = resource_version
        if uid is not None:
            self.uid = uid

    @property
    def resource_version(self):
        """Gets the resource_version of this V1Preconditions.  # noqa: E501

        Specifies the target ResourceVersion  # noqa: E501

        :return: The resource_version of this V1Preconditions.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this V1Preconditions.

        Specifies the target ResourceVersion  # noqa: E501

        :param resource_version: The resource_version of this V1Preconditions.  # noqa: E501
        :type resource_version: str
        """

        self._resource_version = resource_version

    @property
    def uid(self):
        """Gets the uid of this V1Preconditions.  # noqa: E501

        Specifies the target UID.  # noqa: E501

        :return: The uid of this V1Preconditions.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1Preconditions.

        Specifies the target UID.  # noqa: E501

        :param uid: The uid of this V1Preconditions.  # noqa: E501
        :type uid: str
        """

        self._uid = uid

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1Preconditions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Preconditions):
            return True

        return self.to_dict() != other.to_dict()
