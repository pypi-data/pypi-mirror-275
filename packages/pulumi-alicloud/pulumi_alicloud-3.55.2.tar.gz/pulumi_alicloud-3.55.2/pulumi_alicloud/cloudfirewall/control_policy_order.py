# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ControlPolicyOrderArgs', 'ControlPolicyOrder']

@pulumi.input_type
class ControlPolicyOrderArgs:
    def __init__(__self__, *,
                 acl_uuid: pulumi.Input[str],
                 direction: pulumi.Input[str],
                 order: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ControlPolicyOrder resource.
        :param pulumi.Input[str] acl_uuid: The unique ID of the access control policy.
        :param pulumi.Input[str] direction: Direction. Valid values: `in`, `out`.
        :param pulumi.Input[int] order: The priority of the access control policy. The priority value starts from 1. A small priority value indicates a high priority. **NOTE:** The value of -1 indicates the lowest priority.
        """
        pulumi.set(__self__, "acl_uuid", acl_uuid)
        pulumi.set(__self__, "direction", direction)
        if order is not None:
            pulumi.set(__self__, "order", order)

    @property
    @pulumi.getter(name="aclUuid")
    def acl_uuid(self) -> pulumi.Input[str]:
        """
        The unique ID of the access control policy.
        """
        return pulumi.get(self, "acl_uuid")

    @acl_uuid.setter
    def acl_uuid(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_uuid", value)

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Input[str]:
        """
        Direction. Valid values: `in`, `out`.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: pulumi.Input[str]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of the access control policy. The priority value starts from 1. A small priority value indicates a high priority. **NOTE:** The value of -1 indicates the lowest priority.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)


@pulumi.input_type
class _ControlPolicyOrderState:
    def __init__(__self__, *,
                 acl_uuid: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering ControlPolicyOrder resources.
        :param pulumi.Input[str] acl_uuid: The unique ID of the access control policy.
        :param pulumi.Input[str] direction: Direction. Valid values: `in`, `out`.
        :param pulumi.Input[int] order: The priority of the access control policy. The priority value starts from 1. A small priority value indicates a high priority. **NOTE:** The value of -1 indicates the lowest priority.
        """
        if acl_uuid is not None:
            pulumi.set(__self__, "acl_uuid", acl_uuid)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)
        if order is not None:
            pulumi.set(__self__, "order", order)

    @property
    @pulumi.getter(name="aclUuid")
    def acl_uuid(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID of the access control policy.
        """
        return pulumi.get(self, "acl_uuid")

    @acl_uuid.setter
    def acl_uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_uuid", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[str]]:
        """
        Direction. Valid values: `in`, `out`.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of the access control policy. The priority value starts from 1. A small priority value indicates a high priority. **NOTE:** The value of -1 indicates the lowest priority.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)


class ControlPolicyOrder(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_uuid: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a Cloud Firewall Control Policy resource.

        For information about Cloud Firewall Control Policy Order and how to use it, see [What is Control Policy Order](https://www.alibabacloud.com/help/doc-detail/138867.htm).

        > **NOTE:** Available in v1.130.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example1 = alicloud.cloudfirewall.ControlPolicy("example1",
            application_name="ANY",
            acl_action="accept",
            description="example",
            destination_type="net",
            destination="100.1.1.0/24",
            direction="out",
            proto="ANY",
            source="1.2.3.0/24",
            source_type="net")
        example2 = alicloud.cloudfirewall.ControlPolicyOrder("example2",
            acl_uuid=example1.acl_uuid,
            direction=example1.direction,
            order=1)
        ```

        ## Import

        Cloud Firewall Control Policy Order can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cloudfirewall/controlPolicyOrder:ControlPolicyOrder example <acl_uuid>:<direction>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_uuid: The unique ID of the access control policy.
        :param pulumi.Input[str] direction: Direction. Valid values: `in`, `out`.
        :param pulumi.Input[int] order: The priority of the access control policy. The priority value starts from 1. A small priority value indicates a high priority. **NOTE:** The value of -1 indicates the lowest priority.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ControlPolicyOrderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloud Firewall Control Policy resource.

        For information about Cloud Firewall Control Policy Order and how to use it, see [What is Control Policy Order](https://www.alibabacloud.com/help/doc-detail/138867.htm).

        > **NOTE:** Available in v1.130.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example1 = alicloud.cloudfirewall.ControlPolicy("example1",
            application_name="ANY",
            acl_action="accept",
            description="example",
            destination_type="net",
            destination="100.1.1.0/24",
            direction="out",
            proto="ANY",
            source="1.2.3.0/24",
            source_type="net")
        example2 = alicloud.cloudfirewall.ControlPolicyOrder("example2",
            acl_uuid=example1.acl_uuid,
            direction=example1.direction,
            order=1)
        ```

        ## Import

        Cloud Firewall Control Policy Order can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cloudfirewall/controlPolicyOrder:ControlPolicyOrder example <acl_uuid>:<direction>
        ```

        :param str resource_name: The name of the resource.
        :param ControlPolicyOrderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ControlPolicyOrderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_uuid: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ControlPolicyOrderArgs.__new__(ControlPolicyOrderArgs)

            if acl_uuid is None and not opts.urn:
                raise TypeError("Missing required property 'acl_uuid'")
            __props__.__dict__["acl_uuid"] = acl_uuid
            if direction is None and not opts.urn:
                raise TypeError("Missing required property 'direction'")
            __props__.__dict__["direction"] = direction
            __props__.__dict__["order"] = order
        super(ControlPolicyOrder, __self__).__init__(
            'alicloud:cloudfirewall/controlPolicyOrder:ControlPolicyOrder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl_uuid: Optional[pulumi.Input[str]] = None,
            direction: Optional[pulumi.Input[str]] = None,
            order: Optional[pulumi.Input[int]] = None) -> 'ControlPolicyOrder':
        """
        Get an existing ControlPolicyOrder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_uuid: The unique ID of the access control policy.
        :param pulumi.Input[str] direction: Direction. Valid values: `in`, `out`.
        :param pulumi.Input[int] order: The priority of the access control policy. The priority value starts from 1. A small priority value indicates a high priority. **NOTE:** The value of -1 indicates the lowest priority.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ControlPolicyOrderState.__new__(_ControlPolicyOrderState)

        __props__.__dict__["acl_uuid"] = acl_uuid
        __props__.__dict__["direction"] = direction
        __props__.__dict__["order"] = order
        return ControlPolicyOrder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aclUuid")
    def acl_uuid(self) -> pulumi.Output[str]:
        """
        The unique ID of the access control policy.
        """
        return pulumi.get(self, "acl_uuid")

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Output[str]:
        """
        Direction. Valid values: `in`, `out`.
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def order(self) -> pulumi.Output[Optional[int]]:
        """
        The priority of the access control policy. The priority value starts from 1. A small priority value indicates a high priority. **NOTE:** The value of -1 indicates the lowest priority.
        """
        return pulumi.get(self, "order")

