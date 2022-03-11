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


class V1beta1IngressClassSpec(object):
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
        'controller': 'str',
        'parameters': 'V1beta1IngressClassParametersReference'
    }

    attribute_map = {
        'controller': 'controller',
        'parameters': 'parameters'
    }

    def __init__(self, controller=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1IngressClassSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._controller = None
        self._parameters = None
        self.discriminator = None

        if controller is not None:
            self.controller = controller
        if parameters is not None:
            self.parameters = parameters

    @property
    def controller(self):
        """Gets the controller of this V1beta1IngressClassSpec.  # noqa: E501

        Controller refers to the name of the controller that should handle this class. This allows for different \"flavors\" that are controlled by the same controller. For example, you may have different Parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. \"acme.io/ingress-controller\". This field is immutable.  # noqa: E501

        :return: The controller of this V1beta1IngressClassSpec.  # noqa: E501
        :rtype: str
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this V1beta1IngressClassSpec.

        Controller refers to the name of the controller that should handle this class. This allows for different \"flavors\" that are controlled by the same controller. For example, you may have different Parameters for the same implementing controller. This should be specified as a domain-prefixed path no more than 250 characters in length, e.g. \"acme.io/ingress-controller\". This field is immutable.  # noqa: E501

        :param controller: The controller of this V1beta1IngressClassSpec.  # noqa: E501
        :type controller: str
        """

        self._controller = controller

    @property
    def parameters(self):
        """Gets the parameters of this V1beta1IngressClassSpec.  # noqa: E501


        :return: The parameters of this V1beta1IngressClassSpec.  # noqa: E501
        :rtype: V1beta1IngressClassParametersReference
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this V1beta1IngressClassSpec.


        :param parameters: The parameters of this V1beta1IngressClassSpec.  # noqa: E501
        :type parameters: V1beta1IngressClassParametersReference
        """

        self._parameters = parameters

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
        if not isinstance(other, V1beta1IngressClassSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1IngressClassSpec):
            return True

        return self.to_dict() != other.to_dict()
