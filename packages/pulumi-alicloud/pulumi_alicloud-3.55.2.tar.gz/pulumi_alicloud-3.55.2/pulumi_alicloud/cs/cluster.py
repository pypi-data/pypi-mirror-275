# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 cidr_block: pulumi.Input[str],
                 instance_type: pulumi.Input[str],
                 password: pulumi.Input[str],
                 vswitch_id: pulumi.Input[str],
                 disk_category: Optional[pulumi.Input[str]] = None,
                 disk_size: Optional[pulumi.Input[int]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 is_outdated: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 need_slb: Optional[pulumi.Input[bool]] = None,
                 node_number: Optional[pulumi.Input[int]] = None,
                 release_eip: Optional[pulumi.Input[bool]] = None,
                 size: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        """
        pulumi.set(__self__, "cidr_block", cidr_block)
        pulumi.set(__self__, "instance_type", instance_type)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "vswitch_id", vswitch_id)
        if disk_category is not None:
            pulumi.set(__self__, "disk_category", disk_category)
        if disk_size is not None:
            pulumi.set(__self__, "disk_size", disk_size)
        if image_id is not None:
            pulumi.set(__self__, "image_id", image_id)
        if is_outdated is not None:
            pulumi.set(__self__, "is_outdated", is_outdated)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if need_slb is not None:
            pulumi.set(__self__, "need_slb", need_slb)
        if node_number is not None:
            pulumi.set(__self__, "node_number", node_number)
        if release_eip is not None:
            pulumi.set(__self__, "release_eip", release_eip)
        if size is not None:
            warnings.warn("""Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""", DeprecationWarning)
            pulumi.log.warn("""size is deprecated: Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""")
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Input[str]:
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: pulumi.Input[str]):
        pulumi.set(self, "cidr_block", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "vswitch_id")

    @vswitch_id.setter
    def vswitch_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vswitch_id", value)

    @property
    @pulumi.getter(name="diskCategory")
    def disk_category(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "disk_category")

    @disk_category.setter
    def disk_category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_category", value)

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "disk_size")

    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_size", value)

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "image_id")

    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_id", value)

    @property
    @pulumi.getter(name="isOutdated")
    def is_outdated(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_outdated")

    @is_outdated.setter
    def is_outdated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_outdated", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter(name="needSlb")
    def need_slb(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "need_slb")

    @need_slb.setter
    def need_slb(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "need_slb", value)

    @property
    @pulumi.getter(name="nodeNumber")
    def node_number(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "node_number")

    @node_number.setter
    def node_number(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_number", value)

    @property
    @pulumi.getter(name="releaseEip")
    def release_eip(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "release_eip")

    @release_eip.setter
    def release_eip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "release_eip", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        warnings.warn("""Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""", DeprecationWarning)
        pulumi.log.warn("""size is deprecated: Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""")

        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *,
                 agent_version: Optional[pulumi.Input[str]] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 disk_category: Optional[pulumi.Input[str]] = None,
                 disk_size: Optional[pulumi.Input[int]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 is_outdated: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 need_slb: Optional[pulumi.Input[bool]] = None,
                 node_number: Optional[pulumi.Input[int]] = None,
                 nodes: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterNodeArgs']]]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 release_eip: Optional[pulumi.Input[bool]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 slb_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Cluster resources.
        """
        if agent_version is not None:
            pulumi.set(__self__, "agent_version", agent_version)
        if cidr_block is not None:
            pulumi.set(__self__, "cidr_block", cidr_block)
        if disk_category is not None:
            pulumi.set(__self__, "disk_category", disk_category)
        if disk_size is not None:
            pulumi.set(__self__, "disk_size", disk_size)
        if image_id is not None:
            pulumi.set(__self__, "image_id", image_id)
        if instance_type is not None:
            pulumi.set(__self__, "instance_type", instance_type)
        if is_outdated is not None:
            pulumi.set(__self__, "is_outdated", is_outdated)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if need_slb is not None:
            pulumi.set(__self__, "need_slb", need_slb)
        if node_number is not None:
            pulumi.set(__self__, "node_number", node_number)
        if nodes is not None:
            pulumi.set(__self__, "nodes", nodes)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if release_eip is not None:
            pulumi.set(__self__, "release_eip", release_eip)
        if security_group_id is not None:
            pulumi.set(__self__, "security_group_id", security_group_id)
        if size is not None:
            warnings.warn("""Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""", DeprecationWarning)
            pulumi.log.warn("""size is deprecated: Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""")
        if size is not None:
            pulumi.set(__self__, "size", size)
        if slb_id is not None:
            pulumi.set(__self__, "slb_id", slb_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)
        if vswitch_id is not None:
            pulumi.set(__self__, "vswitch_id", vswitch_id)

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "agent_version")

    @agent_version.setter
    def agent_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_version", value)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_block", value)

    @property
    @pulumi.getter(name="diskCategory")
    def disk_category(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "disk_category")

    @disk_category.setter
    def disk_category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_category", value)

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "disk_size")

    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_size", value)

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "image_id")

    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_id", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter(name="isOutdated")
    def is_outdated(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_outdated")

    @is_outdated.setter
    def is_outdated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_outdated", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter(name="needSlb")
    def need_slb(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "need_slb")

    @need_slb.setter
    def need_slb(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "need_slb", value)

    @property
    @pulumi.getter(name="nodeNumber")
    def node_number(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "node_number")

    @node_number.setter
    def node_number(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_number", value)

    @property
    @pulumi.getter
    def nodes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ClusterNodeArgs']]]]:
        return pulumi.get(self, "nodes")

    @nodes.setter
    def nodes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterNodeArgs']]]]):
        pulumi.set(self, "nodes", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="releaseEip")
    def release_eip(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "release_eip")

    @release_eip.setter
    def release_eip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "release_eip", value)

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security_group_id")

    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_group_id", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        warnings.warn("""Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""", DeprecationWarning)
        pulumi.log.warn("""size is deprecated: Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""")

        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="slbId")
    def slb_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slb_id")

    @slb_id.setter
    def slb_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slb_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vswitch_id")

    @vswitch_id.setter
    def vswitch_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vswitch_id", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 disk_category: Optional[pulumi.Input[str]] = None,
                 disk_size: Optional[pulumi.Input[int]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 is_outdated: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 need_slb: Optional[pulumi.Input[bool]] = None,
                 node_number: Optional[pulumi.Input[int]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 release_eip: Optional[pulumi.Input[bool]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 disk_category: Optional[pulumi.Input[str]] = None,
                 disk_size: Optional[pulumi.Input[int]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 is_outdated: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 need_slb: Optional[pulumi.Input[bool]] = None,
                 node_number: Optional[pulumi.Input[int]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 release_eip: Optional[pulumi.Input[bool]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            if cidr_block is None and not opts.urn:
                raise TypeError("Missing required property 'cidr_block'")
            __props__.__dict__["cidr_block"] = cidr_block
            __props__.__dict__["disk_category"] = disk_category
            __props__.__dict__["disk_size"] = disk_size
            __props__.__dict__["image_id"] = image_id
            if instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'instance_type'")
            __props__.__dict__["instance_type"] = instance_type
            __props__.__dict__["is_outdated"] = is_outdated
            __props__.__dict__["name"] = name
            __props__.__dict__["name_prefix"] = name_prefix
            __props__.__dict__["need_slb"] = need_slb
            __props__.__dict__["node_number"] = node_number
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["release_eip"] = release_eip
            __props__.__dict__["size"] = size
            if vswitch_id is None and not opts.urn:
                raise TypeError("Missing required property 'vswitch_id'")
            __props__.__dict__["vswitch_id"] = vswitch_id
            __props__.__dict__["agent_version"] = None
            __props__.__dict__["nodes"] = None
            __props__.__dict__["security_group_id"] = None
            __props__.__dict__["slb_id"] = None
            __props__.__dict__["vpc_id"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Cluster, __self__).__init__(
            'alicloud:cs/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            agent_version: Optional[pulumi.Input[str]] = None,
            cidr_block: Optional[pulumi.Input[str]] = None,
            disk_category: Optional[pulumi.Input[str]] = None,
            disk_size: Optional[pulumi.Input[int]] = None,
            image_id: Optional[pulumi.Input[str]] = None,
            instance_type: Optional[pulumi.Input[str]] = None,
            is_outdated: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            need_slb: Optional[pulumi.Input[bool]] = None,
            node_number: Optional[pulumi.Input[int]] = None,
            nodes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterNodeArgs']]]]] = None,
            password: Optional[pulumi.Input[str]] = None,
            release_eip: Optional[pulumi.Input[bool]] = None,
            security_group_id: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            slb_id: Optional[pulumi.Input[str]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None,
            vswitch_id: Optional[pulumi.Input[str]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterState.__new__(_ClusterState)

        __props__.__dict__["agent_version"] = agent_version
        __props__.__dict__["cidr_block"] = cidr_block
        __props__.__dict__["disk_category"] = disk_category
        __props__.__dict__["disk_size"] = disk_size
        __props__.__dict__["image_id"] = image_id
        __props__.__dict__["instance_type"] = instance_type
        __props__.__dict__["is_outdated"] = is_outdated
        __props__.__dict__["name"] = name
        __props__.__dict__["name_prefix"] = name_prefix
        __props__.__dict__["need_slb"] = need_slb
        __props__.__dict__["node_number"] = node_number
        __props__.__dict__["nodes"] = nodes
        __props__.__dict__["password"] = password
        __props__.__dict__["release_eip"] = release_eip
        __props__.__dict__["security_group_id"] = security_group_id
        __props__.__dict__["size"] = size
        __props__.__dict__["slb_id"] = slb_id
        __props__.__dict__["vpc_id"] = vpc_id
        __props__.__dict__["vswitch_id"] = vswitch_id
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "agent_version")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="diskCategory")
    def disk_category(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "disk_category")

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "disk_size")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="isOutdated")
    def is_outdated(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "is_outdated")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter(name="needSlb")
    def need_slb(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "need_slb")

    @property
    @pulumi.getter(name="nodeNumber")
    def node_number(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "node_number")

    @property
    @pulumi.getter
    def nodes(self) -> pulumi.Output[Sequence['outputs.ClusterNode']]:
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="releaseEip")
    def release_eip(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "release_eip")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[Optional[int]]:
        warnings.warn("""Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""", DeprecationWarning)
        pulumi.log.warn("""size is deprecated: Field 'size' has been deprecated from provider version 1.9.1. New field 'node_number' replaces it.""")

        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="slbId")
    def slb_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "slb_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "vswitch_id")

