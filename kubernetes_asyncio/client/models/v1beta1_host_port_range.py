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


class V1beta1HostPortRange(object):
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
        'max': 'int',
        'min': 'int'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min'
    }

    def __init__(self, max=None, min=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1HostPortRange - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._max = None
        self._min = None
        self.discriminator = None

        self.max = max
        self.min = min

    @property
    def max(self):
        """Gets the max of this V1beta1HostPortRange.  # noqa: E501

        max is the end of the range, inclusive.  # noqa: E501

        :return: The max of this V1beta1HostPortRange.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this V1beta1HostPortRange.

        max is the end of the range, inclusive.  # noqa: E501

        :param max: The max of this V1beta1HostPortRange.  # noqa: E501
        :type max: int
        """
        if self.local_vars_configuration.client_side_validation and max is None:  # noqa: E501
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    @property
    def min(self):
        """Gets the min of this V1beta1HostPortRange.  # noqa: E501

        min is the start of the range, inclusive.  # noqa: E501

        :return: The min of this V1beta1HostPortRange.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this V1beta1HostPortRange.

        min is the start of the range, inclusive.  # noqa: E501

        :param min: The min of this V1beta1HostPortRange.  # noqa: E501
        :type min: int
        """
        if self.local_vars_configuration.client_side_validation and min is None:  # noqa: E501
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

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
        if not isinstance(other, V1beta1HostPortRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1HostPortRange):
            return True

        return self.to_dict() != other.to_dict()
