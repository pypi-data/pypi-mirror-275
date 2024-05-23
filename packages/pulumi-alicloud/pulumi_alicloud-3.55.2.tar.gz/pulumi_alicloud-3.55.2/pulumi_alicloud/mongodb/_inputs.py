# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstanceParameterArgs',
    'InstanceReplicaSetArgs',
    'ServerlessInstanceSecurityIpGroupArgs',
    'ShardingInstanceConfigServerListArgs',
    'ShardingInstanceMongoListArgs',
    'ShardingInstanceShardListArgs',
    'ShardingNetworkPrivateAddressNetworkAddressArgs',
    'ShardingNetworkPublicAddressNetworkAddressArgs',
]

@pulumi.input_type
class InstanceParameterArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the parameter.
        :param pulumi.Input[str] value: The value of the parameter.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the parameter.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the parameter.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class InstanceReplicaSetArgs:
    def __init__(__self__, *,
                 connection_domain: Optional[pulumi.Input[str]] = None,
                 connection_port: Optional[pulumi.Input[str]] = None,
                 network_type: Optional[pulumi.Input[str]] = None,
                 replica_set_role: Optional[pulumi.Input[str]] = None,
                 vpc_cloud_instance_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] connection_domain: The connection address of the node.
        :param pulumi.Input[str] connection_port: The connection port of the node.
        :param pulumi.Input[str] network_type: The network type of the instance. Valid values:`Classic`, `VPC`.
        :param pulumi.Input[str] replica_set_role: The role of the node.
        :param pulumi.Input[str] vpc_cloud_instance_id: VPC instance ID.
        :param pulumi.Input[str] vpc_id: The ID of the VPC. > **NOTE:** `vpc_id` is valid only when `network_type` is set to `VPC`.
        :param pulumi.Input[str] vswitch_id: The virtual switch ID to launch DB instances in one VPC.
        """
        if connection_domain is not None:
            pulumi.set(__self__, "connection_domain", connection_domain)
        if connection_port is not None:
            pulumi.set(__self__, "connection_port", connection_port)
        if network_type is not None:
            pulumi.set(__self__, "network_type", network_type)
        if replica_set_role is not None:
            pulumi.set(__self__, "replica_set_role", replica_set_role)
        if vpc_cloud_instance_id is not None:
            pulumi.set(__self__, "vpc_cloud_instance_id", vpc_cloud_instance_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)
        if vswitch_id is not None:
            pulumi.set(__self__, "vswitch_id", vswitch_id)

    @property
    @pulumi.getter(name="connectionDomain")
    def connection_domain(self) -> Optional[pulumi.Input[str]]:
        """
        The connection address of the node.
        """
        return pulumi.get(self, "connection_domain")

    @connection_domain.setter
    def connection_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_domain", value)

    @property
    @pulumi.getter(name="connectionPort")
    def connection_port(self) -> Optional[pulumi.Input[str]]:
        """
        The connection port of the node.
        """
        return pulumi.get(self, "connection_port")

    @connection_port.setter
    def connection_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_port", value)

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[str]]:
        """
        The network type of the instance. Valid values:`Classic`, `VPC`.
        """
        return pulumi.get(self, "network_type")

    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_type", value)

    @property
    @pulumi.getter(name="replicaSetRole")
    def replica_set_role(self) -> Optional[pulumi.Input[str]]:
        """
        The role of the node.
        """
        return pulumi.get(self, "replica_set_role")

    @replica_set_role.setter
    def replica_set_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "replica_set_role", value)

    @property
    @pulumi.getter(name="vpcCloudInstanceId")
    def vpc_cloud_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        VPC instance ID.
        """
        return pulumi.get(self, "vpc_cloud_instance_id")

    @vpc_cloud_instance_id.setter
    def vpc_cloud_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_cloud_instance_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VPC. > **NOTE:** `vpc_id` is valid only when `network_type` is set to `VPC`.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> Optional[pulumi.Input[str]]:
        """
        The virtual switch ID to launch DB instances in one VPC.
        """
        return pulumi.get(self, "vswitch_id")

    @vswitch_id.setter
    def vswitch_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vswitch_id", value)


@pulumi.input_type
class ServerlessInstanceSecurityIpGroupArgs:
    def __init__(__self__, *,
                 security_ip_group_attribute: Optional[pulumi.Input[str]] = None,
                 security_ip_group_name: Optional[pulumi.Input[str]] = None,
                 security_ip_list: Optional[pulumi.Input[str]] = None):
        if security_ip_group_attribute is not None:
            pulumi.set(__self__, "security_ip_group_attribute", security_ip_group_attribute)
        if security_ip_group_name is not None:
            pulumi.set(__self__, "security_ip_group_name", security_ip_group_name)
        if security_ip_list is not None:
            pulumi.set(__self__, "security_ip_list", security_ip_list)

    @property
    @pulumi.getter(name="securityIpGroupAttribute")
    def security_ip_group_attribute(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security_ip_group_attribute")

    @security_ip_group_attribute.setter
    def security_ip_group_attribute(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_ip_group_attribute", value)

    @property
    @pulumi.getter(name="securityIpGroupName")
    def security_ip_group_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security_ip_group_name")

    @security_ip_group_name.setter
    def security_ip_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_ip_group_name", value)

    @property
    @pulumi.getter(name="securityIpList")
    def security_ip_list(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security_ip_list")

    @security_ip_list.setter
    def security_ip_list(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_ip_list", value)


@pulumi.input_type
class ShardingInstanceConfigServerListArgs:
    def __init__(__self__, *,
                 connect_string: Optional[pulumi.Input[str]] = None,
                 max_connections: Optional[pulumi.Input[int]] = None,
                 max_iops: Optional[pulumi.Input[int]] = None,
                 node_class: Optional[pulumi.Input[str]] = None,
                 node_description: Optional[pulumi.Input[str]] = None,
                 node_id: Optional[pulumi.Input[str]] = None,
                 node_storage: Optional[pulumi.Input[int]] = None,
                 port: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] connect_string: The connection address of the Config Server node.
        :param pulumi.Input[int] max_connections: The max connections of the Config Server node.
        :param pulumi.Input[int] max_iops: The maximum IOPS of the Config Server node.
        :param pulumi.Input[str] node_class: The instance type of the ConfigServer node. Valid values: `mdb.shard.2x.xlarge.d`, `dds.cs.mid`.
        :param pulumi.Input[str] node_description: The description of the Config Server node.
        :param pulumi.Input[str] node_id: The ID of the Config Server node.
        :param pulumi.Input[int] node_storage: The storage space of the ConfigServer node.
        :param pulumi.Input[int] port: The connection port of the Config Server node.
        """
        if connect_string is not None:
            pulumi.set(__self__, "connect_string", connect_string)
        if max_connections is not None:
            pulumi.set(__self__, "max_connections", max_connections)
        if max_iops is not None:
            pulumi.set(__self__, "max_iops", max_iops)
        if node_class is not None:
            pulumi.set(__self__, "node_class", node_class)
        if node_description is not None:
            pulumi.set(__self__, "node_description", node_description)
        if node_id is not None:
            pulumi.set(__self__, "node_id", node_id)
        if node_storage is not None:
            pulumi.set(__self__, "node_storage", node_storage)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter(name="connectString")
    def connect_string(self) -> Optional[pulumi.Input[str]]:
        """
        The connection address of the Config Server node.
        """
        return pulumi.get(self, "connect_string")

    @connect_string.setter
    def connect_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connect_string", value)

    @property
    @pulumi.getter(name="maxConnections")
    def max_connections(self) -> Optional[pulumi.Input[int]]:
        """
        The max connections of the Config Server node.
        """
        return pulumi.get(self, "max_connections")

    @max_connections.setter
    def max_connections(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_connections", value)

    @property
    @pulumi.getter(name="maxIops")
    def max_iops(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum IOPS of the Config Server node.
        """
        return pulumi.get(self, "max_iops")

    @max_iops.setter
    def max_iops(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_iops", value)

    @property
    @pulumi.getter(name="nodeClass")
    def node_class(self) -> Optional[pulumi.Input[str]]:
        """
        The instance type of the ConfigServer node. Valid values: `mdb.shard.2x.xlarge.d`, `dds.cs.mid`.
        """
        return pulumi.get(self, "node_class")

    @node_class.setter
    def node_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_class", value)

    @property
    @pulumi.getter(name="nodeDescription")
    def node_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the Config Server node.
        """
        return pulumi.get(self, "node_description")

    @node_description.setter
    def node_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_description", value)

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Config Server node.
        """
        return pulumi.get(self, "node_id")

    @node_id.setter
    def node_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_id", value)

    @property
    @pulumi.getter(name="nodeStorage")
    def node_storage(self) -> Optional[pulumi.Input[int]]:
        """
        The storage space of the ConfigServer node.
        """
        return pulumi.get(self, "node_storage")

    @node_storage.setter
    def node_storage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_storage", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The connection port of the Config Server node.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)


@pulumi.input_type
class ShardingInstanceMongoListArgs:
    def __init__(__self__, *,
                 node_class: pulumi.Input[str],
                 connect_string: Optional[pulumi.Input[str]] = None,
                 node_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] node_class: The instance type of the mongo node. see [Instance specifications](https://www.alibabacloud.com/help/doc-detail/57141.htm).
        :param pulumi.Input[str] connect_string: The connection address of the Config Server node.
        :param pulumi.Input[str] node_id: The ID of the Config Server node.
        :param pulumi.Input[int] port: The connection port of the Config Server node.
        """
        pulumi.set(__self__, "node_class", node_class)
        if connect_string is not None:
            pulumi.set(__self__, "connect_string", connect_string)
        if node_id is not None:
            pulumi.set(__self__, "node_id", node_id)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter(name="nodeClass")
    def node_class(self) -> pulumi.Input[str]:
        """
        The instance type of the mongo node. see [Instance specifications](https://www.alibabacloud.com/help/doc-detail/57141.htm).
        """
        return pulumi.get(self, "node_class")

    @node_class.setter
    def node_class(self, value: pulumi.Input[str]):
        pulumi.set(self, "node_class", value)

    @property
    @pulumi.getter(name="connectString")
    def connect_string(self) -> Optional[pulumi.Input[str]]:
        """
        The connection address of the Config Server node.
        """
        return pulumi.get(self, "connect_string")

    @connect_string.setter
    def connect_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connect_string", value)

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Config Server node.
        """
        return pulumi.get(self, "node_id")

    @node_id.setter
    def node_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_id", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The connection port of the Config Server node.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)


@pulumi.input_type
class ShardingInstanceShardListArgs:
    def __init__(__self__, *,
                 node_class: pulumi.Input[str],
                 node_storage: pulumi.Input[int],
                 node_id: Optional[pulumi.Input[str]] = None,
                 readonly_replicas: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] node_class: The instance type of the shard node. see [Instance specifications](https://www.alibabacloud.com/help/doc-detail/57141.htm).
        :param pulumi.Input[int] node_storage: The storage space of the shard node.
               - Custom storage space; value range: [10, 1,000]
               - 10-GB increments. Unit: GB.
        :param pulumi.Input[str] node_id: The ID of the Config Server node.
        :param pulumi.Input[int] readonly_replicas: The number of read-only nodes in shard node Default value: `0`. Valid values: `0` to `5`.
        """
        pulumi.set(__self__, "node_class", node_class)
        pulumi.set(__self__, "node_storage", node_storage)
        if node_id is not None:
            pulumi.set(__self__, "node_id", node_id)
        if readonly_replicas is not None:
            pulumi.set(__self__, "readonly_replicas", readonly_replicas)

    @property
    @pulumi.getter(name="nodeClass")
    def node_class(self) -> pulumi.Input[str]:
        """
        The instance type of the shard node. see [Instance specifications](https://www.alibabacloud.com/help/doc-detail/57141.htm).
        """
        return pulumi.get(self, "node_class")

    @node_class.setter
    def node_class(self, value: pulumi.Input[str]):
        pulumi.set(self, "node_class", value)

    @property
    @pulumi.getter(name="nodeStorage")
    def node_storage(self) -> pulumi.Input[int]:
        """
        The storage space of the shard node.
        - Custom storage space; value range: [10, 1,000]
        - 10-GB increments. Unit: GB.
        """
        return pulumi.get(self, "node_storage")

    @node_storage.setter
    def node_storage(self, value: pulumi.Input[int]):
        pulumi.set(self, "node_storage", value)

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Config Server node.
        """
        return pulumi.get(self, "node_id")

    @node_id.setter
    def node_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_id", value)

    @property
    @pulumi.getter(name="readonlyReplicas")
    def readonly_replicas(self) -> Optional[pulumi.Input[int]]:
        """
        The number of read-only nodes in shard node Default value: `0`. Valid values: `0` to `5`.
        """
        return pulumi.get(self, "readonly_replicas")

    @readonly_replicas.setter
    def readonly_replicas(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "readonly_replicas", value)


@pulumi.input_type
class ShardingNetworkPrivateAddressNetworkAddressArgs:
    def __init__(__self__, *,
                 expired_time: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 network_address: Optional[pulumi.Input[str]] = None,
                 network_type: Optional[pulumi.Input[str]] = None,
                 node_id: Optional[pulumi.Input[str]] = None,
                 node_type: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] expired_time: The remaining duration of the classic network address. Unit: `seconds`.
        :param pulumi.Input[str] ip_address: The IP address of the instance.
        :param pulumi.Input[str] network_address: The endpoint of the instance.
        :param pulumi.Input[str] network_type: The network type.
        :param pulumi.Input[str] node_id: The ID of the Shard node or the ConfigServer node.
        :param pulumi.Input[str] node_type: The type of the node.
        :param pulumi.Input[str] port: The port number.
        :param pulumi.Input[str] role: The role of the node.
        :param pulumi.Input[str] vpc_id: The ID of the VPC.
        :param pulumi.Input[str] vswitch_id: The vSwitch ID of the VPC.
        """
        if expired_time is not None:
            pulumi.set(__self__, "expired_time", expired_time)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if network_address is not None:
            pulumi.set(__self__, "network_address", network_address)
        if network_type is not None:
            pulumi.set(__self__, "network_type", network_type)
        if node_id is not None:
            pulumi.set(__self__, "node_id", node_id)
        if node_type is not None:
            pulumi.set(__self__, "node_type", node_type)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)
        if vswitch_id is not None:
            pulumi.set(__self__, "vswitch_id", vswitch_id)

    @property
    @pulumi.getter(name="expiredTime")
    def expired_time(self) -> Optional[pulumi.Input[str]]:
        """
        The remaining duration of the classic network address. Unit: `seconds`.
        """
        return pulumi.get(self, "expired_time")

    @expired_time.setter
    def expired_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expired_time", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the instance.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="networkAddress")
    def network_address(self) -> Optional[pulumi.Input[str]]:
        """
        The endpoint of the instance.
        """
        return pulumi.get(self, "network_address")

    @network_address.setter
    def network_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_address", value)

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[str]]:
        """
        The network type.
        """
        return pulumi.get(self, "network_type")

    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_type", value)

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Shard node or the ConfigServer node.
        """
        return pulumi.get(self, "node_id")

    @node_id.setter
    def node_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_id", value)

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the node.
        """
        return pulumi.get(self, "node_type")

    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_type", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        The port number.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role of the node.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VPC.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> Optional[pulumi.Input[str]]:
        """
        The vSwitch ID of the VPC.
        """
        return pulumi.get(self, "vswitch_id")

    @vswitch_id.setter
    def vswitch_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vswitch_id", value)


@pulumi.input_type
class ShardingNetworkPublicAddressNetworkAddressArgs:
    def __init__(__self__, *,
                 expired_time: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 network_address: Optional[pulumi.Input[str]] = None,
                 network_type: Optional[pulumi.Input[str]] = None,
                 node_id: Optional[pulumi.Input[str]] = None,
                 node_type: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] expired_time: The remaining duration of the classic network address. Unit: `seconds`.
        :param pulumi.Input[str] ip_address: The IP address of the instance.
        :param pulumi.Input[str] network_address: The endpoint of the instance.
        :param pulumi.Input[str] network_type: The network type.
        :param pulumi.Input[str] node_id: The ID of the `mongos`, `shard`, or `Configserver` node in the sharded cluster instance.
        :param pulumi.Input[str] node_type: The type of the node.
        :param pulumi.Input[str] port: The port number.
        :param pulumi.Input[str] role: The role of the node.
        :param pulumi.Input[str] vpc_id: The ID of the VPC.
        :param pulumi.Input[str] vswitch_id: The vSwitch ID of the VPC.
        """
        if expired_time is not None:
            pulumi.set(__self__, "expired_time", expired_time)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if network_address is not None:
            pulumi.set(__self__, "network_address", network_address)
        if network_type is not None:
            pulumi.set(__self__, "network_type", network_type)
        if node_id is not None:
            pulumi.set(__self__, "node_id", node_id)
        if node_type is not None:
            pulumi.set(__self__, "node_type", node_type)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)
        if vswitch_id is not None:
            pulumi.set(__self__, "vswitch_id", vswitch_id)

    @property
    @pulumi.getter(name="expiredTime")
    def expired_time(self) -> Optional[pulumi.Input[str]]:
        """
        The remaining duration of the classic network address. Unit: `seconds`.
        """
        return pulumi.get(self, "expired_time")

    @expired_time.setter
    def expired_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expired_time", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address of the instance.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="networkAddress")
    def network_address(self) -> Optional[pulumi.Input[str]]:
        """
        The endpoint of the instance.
        """
        return pulumi.get(self, "network_address")

    @network_address.setter
    def network_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_address", value)

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[str]]:
        """
        The network type.
        """
        return pulumi.get(self, "network_type")

    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_type", value)

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the `mongos`, `shard`, or `Configserver` node in the sharded cluster instance.
        """
        return pulumi.get(self, "node_id")

    @node_id.setter
    def node_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_id", value)

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the node.
        """
        return pulumi.get(self, "node_type")

    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_type", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        The port number.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role of the node.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VPC.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> Optional[pulumi.Input[str]]:
        """
        The vSwitch ID of the VPC.
        """
        return pulumi.get(self, "vswitch_id")

    @vswitch_id.setter
    def vswitch_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vswitch_id", value)


