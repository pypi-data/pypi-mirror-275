# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GroupArgs', 'Group']

@pulumi.input_type
class GroupArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Group resource.
        :param pulumi.Input[str] description: The description of the api gateway group. Defaults to null.
        :param pulumi.Input[str] instance_id: The id of the api gateway.
        :param pulumi.Input[str] name: The name of the api gateway group. Defaults to null.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the api gateway group. Defaults to null.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the api gateway.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the api gateway group. Defaults to null.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _GroupState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sub_domain: Optional[pulumi.Input[str]] = None,
                 vpc_domain: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Group resources.
        :param pulumi.Input[str] description: The description of the api gateway group. Defaults to null.
        :param pulumi.Input[str] instance_id: The id of the api gateway.
        :param pulumi.Input[str] name: The name of the api gateway group. Defaults to null.
        :param pulumi.Input[str] sub_domain: (Available in 1.69.0+)	Second-level domain name automatically assigned to the API group.
        :param pulumi.Input[str] vpc_domain: (Available in 1.69.0+)	Second-level VPC domain name automatically assigned to the API group.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sub_domain is not None:
            pulumi.set(__self__, "sub_domain", sub_domain)
        if vpc_domain is not None:
            pulumi.set(__self__, "vpc_domain", vpc_domain)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the api gateway group. Defaults to null.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the api gateway.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the api gateway group. Defaults to null.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="subDomain")
    def sub_domain(self) -> Optional[pulumi.Input[str]]:
        """
        (Available in 1.69.0+)	Second-level domain name automatically assigned to the API group.
        """
        return pulumi.get(self, "sub_domain")

    @sub_domain.setter
    def sub_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sub_domain", value)

    @property
    @pulumi.getter(name="vpcDomain")
    def vpc_domain(self) -> Optional[pulumi.Input[str]]:
        """
        (Available in 1.69.0+)	Second-level VPC domain name automatically assigned to the API group.
        """
        return pulumi.get(self, "vpc_domain")

    @vpc_domain.setter
    def vpc_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_domain", value)


class Group(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.apigateway.Group("default",
            name="tf_example",
            description="tf_example")
        ```

        ## Import

        Api gateway group can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:apigateway/group:Group example "ab2351f2ce904edaa8d92a0510832b91"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the api gateway group. Defaults to null.
        :param pulumi.Input[str] instance_id: The id of the api gateway.
        :param pulumi.Input[str] name: The name of the api gateway group. Defaults to null.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.apigateway.Group("default",
            name="tf_example",
            description="tf_example")
        ```

        ## Import

        Api gateway group can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:apigateway/group:Group example "ab2351f2ce904edaa8d92a0510832b91"
        ```

        :param str resource_name: The name of the resource.
        :param GroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupArgs.__new__(GroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["name"] = name
            __props__.__dict__["sub_domain"] = None
            __props__.__dict__["vpc_domain"] = None
        super(Group, __self__).__init__(
            'alicloud:apigateway/group:Group',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sub_domain: Optional[pulumi.Input[str]] = None,
            vpc_domain: Optional[pulumi.Input[str]] = None) -> 'Group':
        """
        Get an existing Group resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the api gateway group. Defaults to null.
        :param pulumi.Input[str] instance_id: The id of the api gateway.
        :param pulumi.Input[str] name: The name of the api gateway group. Defaults to null.
        :param pulumi.Input[str] sub_domain: (Available in 1.69.0+)	Second-level domain name automatically assigned to the API group.
        :param pulumi.Input[str] vpc_domain: (Available in 1.69.0+)	Second-level VPC domain name automatically assigned to the API group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupState.__new__(_GroupState)

        __props__.__dict__["description"] = description
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["name"] = name
        __props__.__dict__["sub_domain"] = sub_domain
        __props__.__dict__["vpc_domain"] = vpc_domain
        return Group(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the api gateway group. Defaults to null.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The id of the api gateway.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the api gateway group. Defaults to null.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="subDomain")
    def sub_domain(self) -> pulumi.Output[str]:
        """
        (Available in 1.69.0+)	Second-level domain name automatically assigned to the API group.
        """
        return pulumi.get(self, "sub_domain")

    @property
    @pulumi.getter(name="vpcDomain")
    def vpc_domain(self) -> pulumi.Output[str]:
        """
        (Available in 1.69.0+)	Second-level VPC domain name automatically assigned to the API group.
        """
        return pulumi.get(self, "vpc_domain")

