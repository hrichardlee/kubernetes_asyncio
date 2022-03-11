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


class V1beta1RuntimeClassStrategyOptions(object):
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
        'allowed_runtime_class_names': 'list[str]',
        'default_runtime_class_name': 'str'
    }

    attribute_map = {
        'allowed_runtime_class_names': 'allowedRuntimeClassNames',
        'default_runtime_class_name': 'defaultRuntimeClassName'
    }

    def __init__(self, allowed_runtime_class_names=None, default_runtime_class_name=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1RuntimeClassStrategyOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allowed_runtime_class_names = None
        self._default_runtime_class_name = None
        self.discriminator = None

        self.allowed_runtime_class_names = allowed_runtime_class_names
        if default_runtime_class_name is not None:
            self.default_runtime_class_name = default_runtime_class_name

    @property
    def allowed_runtime_class_names(self):
        """Gets the allowed_runtime_class_names of this V1beta1RuntimeClassStrategyOptions.  # noqa: E501

        allowedRuntimeClassNames is an allowlist of RuntimeClass names that may be specified on a pod. A value of \"*\" means that any RuntimeClass name is allowed, and must be the only item in the list. An empty list requires the RuntimeClassName field to be unset.  # noqa: E501

        :return: The allowed_runtime_class_names of this V1beta1RuntimeClassStrategyOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_runtime_class_names

    @allowed_runtime_class_names.setter
    def allowed_runtime_class_names(self, allowed_runtime_class_names):
        """Sets the allowed_runtime_class_names of this V1beta1RuntimeClassStrategyOptions.

        allowedRuntimeClassNames is an allowlist of RuntimeClass names that may be specified on a pod. A value of \"*\" means that any RuntimeClass name is allowed, and must be the only item in the list. An empty list requires the RuntimeClassName field to be unset.  # noqa: E501

        :param allowed_runtime_class_names: The allowed_runtime_class_names of this V1beta1RuntimeClassStrategyOptions.  # noqa: E501
        :type allowed_runtime_class_names: list[str]
        """
        if self.local_vars_configuration.client_side_validation and allowed_runtime_class_names is None:  # noqa: E501
            raise ValueError("Invalid value for `allowed_runtime_class_names`, must not be `None`")  # noqa: E501

        self._allowed_runtime_class_names = allowed_runtime_class_names

    @property
    def default_runtime_class_name(self):
        """Gets the default_runtime_class_name of this V1beta1RuntimeClassStrategyOptions.  # noqa: E501

        defaultRuntimeClassName is the default RuntimeClassName to set on the pod. The default MUST be allowed by the allowedRuntimeClassNames list. A value of nil does not mutate the Pod.  # noqa: E501

        :return: The default_runtime_class_name of this V1beta1RuntimeClassStrategyOptions.  # noqa: E501
        :rtype: str
        """
        return self._default_runtime_class_name

    @default_runtime_class_name.setter
    def default_runtime_class_name(self, default_runtime_class_name):
        """Sets the default_runtime_class_name of this V1beta1RuntimeClassStrategyOptions.

        defaultRuntimeClassName is the default RuntimeClassName to set on the pod. The default MUST be allowed by the allowedRuntimeClassNames list. A value of nil does not mutate the Pod.  # noqa: E501

        :param default_runtime_class_name: The default_runtime_class_name of this V1beta1RuntimeClassStrategyOptions.  # noqa: E501
        :type default_runtime_class_name: str
        """

        self._default_runtime_class_name = default_runtime_class_name

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
        if not isinstance(other, V1beta1RuntimeClassStrategyOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1RuntimeClassStrategyOptions):
            return True

        return self.to_dict() != other.to_dict()
