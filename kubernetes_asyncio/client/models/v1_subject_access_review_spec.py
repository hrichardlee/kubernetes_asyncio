# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.21.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1SubjectAccessReviewSpec(object):
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
        'extra': 'dict(str, list[str])',
        'groups': 'list[str]',
        'non_resource_attributes': 'V1NonResourceAttributes',
        'resource_attributes': 'V1ResourceAttributes',
        'uid': 'str',
        'user': 'str'
    }

    attribute_map = {
        'extra': 'extra',
        'groups': 'groups',
        'non_resource_attributes': 'nonResourceAttributes',
        'resource_attributes': 'resourceAttributes',
        'uid': 'uid',
        'user': 'user'
    }

    def __init__(self, extra=None, groups=None, non_resource_attributes=None, resource_attributes=None, uid=None, user=None, local_vars_configuration=None):  # noqa: E501
        """V1SubjectAccessReviewSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._extra = None
        self._groups = None
        self._non_resource_attributes = None
        self._resource_attributes = None
        self._uid = None
        self._user = None
        self.discriminator = None

        if extra is not None:
            self.extra = extra
        if groups is not None:
            self.groups = groups
        if non_resource_attributes is not None:
            self.non_resource_attributes = non_resource_attributes
        if resource_attributes is not None:
            self.resource_attributes = resource_attributes
        if uid is not None:
            self.uid = uid
        if user is not None:
            self.user = user

    @property
    def extra(self):
        """Gets the extra of this V1SubjectAccessReviewSpec.  # noqa: E501

        Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here.  # noqa: E501

        :return: The extra of this V1SubjectAccessReviewSpec.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this V1SubjectAccessReviewSpec.

        Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here.  # noqa: E501

        :param extra: The extra of this V1SubjectAccessReviewSpec.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._extra = extra

    @property
    def groups(self):
        """Gets the groups of this V1SubjectAccessReviewSpec.  # noqa: E501

        Groups is the groups you're testing for.  # noqa: E501

        :return: The groups of this V1SubjectAccessReviewSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this V1SubjectAccessReviewSpec.

        Groups is the groups you're testing for.  # noqa: E501

        :param groups: The groups of this V1SubjectAccessReviewSpec.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def non_resource_attributes(self):
        """Gets the non_resource_attributes of this V1SubjectAccessReviewSpec.  # noqa: E501


        :return: The non_resource_attributes of this V1SubjectAccessReviewSpec.  # noqa: E501
        :rtype: V1NonResourceAttributes
        """
        return self._non_resource_attributes

    @non_resource_attributes.setter
    def non_resource_attributes(self, non_resource_attributes):
        """Sets the non_resource_attributes of this V1SubjectAccessReviewSpec.


        :param non_resource_attributes: The non_resource_attributes of this V1SubjectAccessReviewSpec.  # noqa: E501
        :type: V1NonResourceAttributes
        """

        self._non_resource_attributes = non_resource_attributes

    @property
    def resource_attributes(self):
        """Gets the resource_attributes of this V1SubjectAccessReviewSpec.  # noqa: E501


        :return: The resource_attributes of this V1SubjectAccessReviewSpec.  # noqa: E501
        :rtype: V1ResourceAttributes
        """
        return self._resource_attributes

    @resource_attributes.setter
    def resource_attributes(self, resource_attributes):
        """Sets the resource_attributes of this V1SubjectAccessReviewSpec.


        :param resource_attributes: The resource_attributes of this V1SubjectAccessReviewSpec.  # noqa: E501
        :type: V1ResourceAttributes
        """

        self._resource_attributes = resource_attributes

    @property
    def uid(self):
        """Gets the uid of this V1SubjectAccessReviewSpec.  # noqa: E501

        UID information about the requesting user.  # noqa: E501

        :return: The uid of this V1SubjectAccessReviewSpec.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1SubjectAccessReviewSpec.

        UID information about the requesting user.  # noqa: E501

        :param uid: The uid of this V1SubjectAccessReviewSpec.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def user(self):
        """Gets the user of this V1SubjectAccessReviewSpec.  # noqa: E501

        User is the user you're testing for. If you specify \"User\" but not \"Groups\", then is it interpreted as \"What if User were not a member of any groups  # noqa: E501

        :return: The user of this V1SubjectAccessReviewSpec.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1SubjectAccessReviewSpec.

        User is the user you're testing for. If you specify \"User\" but not \"Groups\", then is it interpreted as \"What if User were not a member of any groups  # noqa: E501

        :param user: The user of this V1SubjectAccessReviewSpec.  # noqa: E501
        :type: str
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1SubjectAccessReviewSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SubjectAccessReviewSpec):
            return True

        return self.to_dict() != other.to_dict()
