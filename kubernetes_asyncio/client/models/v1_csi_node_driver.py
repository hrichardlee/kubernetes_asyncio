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


class V1CSINodeDriver(object):
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
        'allocatable': 'V1VolumeNodeResources',
        'name': 'str',
        'node_id': 'str',
        'topology_keys': 'list[str]'
    }

    attribute_map = {
        'allocatable': 'allocatable',
        'name': 'name',
        'node_id': 'nodeID',
        'topology_keys': 'topologyKeys'
    }

    def __init__(self, allocatable=None, name=None, node_id=None, topology_keys=None, local_vars_configuration=None):  # noqa: E501
        """V1CSINodeDriver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allocatable = None
        self._name = None
        self._node_id = None
        self._topology_keys = None
        self.discriminator = None

        if allocatable is not None:
            self.allocatable = allocatable
        self.name = name
        self.node_id = node_id
        if topology_keys is not None:
            self.topology_keys = topology_keys

    @property
    def allocatable(self):
        """Gets the allocatable of this V1CSINodeDriver.  # noqa: E501


        :return: The allocatable of this V1CSINodeDriver.  # noqa: E501
        :rtype: V1VolumeNodeResources
        """
        return self._allocatable

    @allocatable.setter
    def allocatable(self, allocatable):
        """Sets the allocatable of this V1CSINodeDriver.


        :param allocatable: The allocatable of this V1CSINodeDriver.  # noqa: E501
        :type allocatable: V1VolumeNodeResources
        """

        self._allocatable = allocatable

    @property
    def name(self):
        """Gets the name of this V1CSINodeDriver.  # noqa: E501

        This is the name of the CSI driver that this object refers to. This MUST be the same name returned by the CSI GetPluginName() call for that driver.  # noqa: E501

        :return: The name of this V1CSINodeDriver.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1CSINodeDriver.

        This is the name of the CSI driver that this object refers to. This MUST be the same name returned by the CSI GetPluginName() call for that driver.  # noqa: E501

        :param name: The name of this V1CSINodeDriver.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def node_id(self):
        """Gets the node_id of this V1CSINodeDriver.  # noqa: E501

        nodeID of the node from the driver point of view. This field enables Kubernetes to communicate with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes may refer to a given node as \"node1\", but the storage system may refer to the same node as \"nodeA\". When Kubernetes issues a command to the storage system to attach a volume to a specific node, it can use this field to refer to the node name using the ID that the storage system will understand, e.g. \"nodeA\" instead of \"node1\". This field is required.  # noqa: E501

        :return: The node_id of this V1CSINodeDriver.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this V1CSINodeDriver.

        nodeID of the node from the driver point of view. This field enables Kubernetes to communicate with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes may refer to a given node as \"node1\", but the storage system may refer to the same node as \"nodeA\". When Kubernetes issues a command to the storage system to attach a volume to a specific node, it can use this field to refer to the node name using the ID that the storage system will understand, e.g. \"nodeA\" instead of \"node1\". This field is required.  # noqa: E501

        :param node_id: The node_id of this V1CSINodeDriver.  # noqa: E501
        :type node_id: str
        """
        if self.local_vars_configuration.client_side_validation and node_id is None:  # noqa: E501
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

    @property
    def topology_keys(self):
        """Gets the topology_keys of this V1CSINodeDriver.  # noqa: E501

        topologyKeys is the list of keys supported by the driver. When a driver is initialized on a cluster, it provides a set of topology keys that it understands (e.g. \"company.com/zone\", \"company.com/region\"). When a driver is initialized on a node, it provides the same topology keys along with values. Kubelet will expose these topology keys as labels on its own node object. When Kubernetes does topology aware provisioning, it can use this list to determine which labels it should retrieve from the node object and pass back to the driver. It is possible for different nodes to use different topology keys. This can be empty if driver does not support topology.  # noqa: E501

        :return: The topology_keys of this V1CSINodeDriver.  # noqa: E501
        :rtype: list[str]
        """
        return self._topology_keys

    @topology_keys.setter
    def topology_keys(self, topology_keys):
        """Sets the topology_keys of this V1CSINodeDriver.

        topologyKeys is the list of keys supported by the driver. When a driver is initialized on a cluster, it provides a set of topology keys that it understands (e.g. \"company.com/zone\", \"company.com/region\"). When a driver is initialized on a node, it provides the same topology keys along with values. Kubelet will expose these topology keys as labels on its own node object. When Kubernetes does topology aware provisioning, it can use this list to determine which labels it should retrieve from the node object and pass back to the driver. It is possible for different nodes to use different topology keys. This can be empty if driver does not support topology.  # noqa: E501

        :param topology_keys: The topology_keys of this V1CSINodeDriver.  # noqa: E501
        :type topology_keys: list[str]
        """

        self._topology_keys = topology_keys

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
        if not isinstance(other, V1CSINodeDriver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CSINodeDriver):
            return True

        return self.to_dict() != other.to_dict()
