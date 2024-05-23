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

__all__ = ['FirewallVpcFirewallCenArgs', 'FirewallVpcFirewallCen']

@pulumi.input_type
class FirewallVpcFirewallCenArgs:
    def __init__(__self__, *,
                 cen_id: pulumi.Input[str],
                 local_vpc: pulumi.Input['FirewallVpcFirewallCenLocalVpcArgs'],
                 status: pulumi.Input[str],
                 vpc_firewall_name: pulumi.Input[str],
                 vpc_region: pulumi.Input[str],
                 lang: Optional[pulumi.Input[str]] = None,
                 member_uid: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FirewallVpcFirewallCen resource.
        :param pulumi.Input[str] cen_id: The ID of the CEN instance.
        :param pulumi.Input['FirewallVpcFirewallCenLocalVpcArgs'] local_vpc: The details of the VPC. See `local_vpc` below.
        :param pulumi.Input[str] status: Firewall switch status.
        :param pulumi.Input[str] vpc_firewall_name: The name of the VPC firewall instance.
        :param pulumi.Input[str] vpc_region: The ID of the region to which the VPC is created.
        :param pulumi.Input[str] lang: The language type of the requested and received messages. Valid values:
        :param pulumi.Input[str] member_uid: The UID of the member account (other Alibaba Cloud account) of the current Alibaba cloud account.
        """
        pulumi.set(__self__, "cen_id", cen_id)
        pulumi.set(__self__, "local_vpc", local_vpc)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "vpc_firewall_name", vpc_firewall_name)
        pulumi.set(__self__, "vpc_region", vpc_region)
        if lang is not None:
            pulumi.set(__self__, "lang", lang)
        if member_uid is not None:
            pulumi.set(__self__, "member_uid", member_uid)

    @property
    @pulumi.getter(name="cenId")
    def cen_id(self) -> pulumi.Input[str]:
        """
        The ID of the CEN instance.
        """
        return pulumi.get(self, "cen_id")

    @cen_id.setter
    def cen_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cen_id", value)

    @property
    @pulumi.getter(name="localVpc")
    def local_vpc(self) -> pulumi.Input['FirewallVpcFirewallCenLocalVpcArgs']:
        """
        The details of the VPC. See `local_vpc` below.
        """
        return pulumi.get(self, "local_vpc")

    @local_vpc.setter
    def local_vpc(self, value: pulumi.Input['FirewallVpcFirewallCenLocalVpcArgs']):
        pulumi.set(self, "local_vpc", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        """
        Firewall switch status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="vpcFirewallName")
    def vpc_firewall_name(self) -> pulumi.Input[str]:
        """
        The name of the VPC firewall instance.
        """
        return pulumi.get(self, "vpc_firewall_name")

    @vpc_firewall_name.setter
    def vpc_firewall_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_firewall_name", value)

    @property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> pulumi.Input[str]:
        """
        The ID of the region to which the VPC is created.
        """
        return pulumi.get(self, "vpc_region")

    @vpc_region.setter
    def vpc_region(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_region", value)

    @property
    @pulumi.getter
    def lang(self) -> Optional[pulumi.Input[str]]:
        """
        The language type of the requested and received messages. Valid values:
        """
        return pulumi.get(self, "lang")

    @lang.setter
    def lang(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lang", value)

    @property
    @pulumi.getter(name="memberUid")
    def member_uid(self) -> Optional[pulumi.Input[str]]:
        """
        The UID of the member account (other Alibaba Cloud account) of the current Alibaba cloud account.
        """
        return pulumi.get(self, "member_uid")

    @member_uid.setter
    def member_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member_uid", value)


@pulumi.input_type
class _FirewallVpcFirewallCenState:
    def __init__(__self__, *,
                 cen_id: Optional[pulumi.Input[str]] = None,
                 connect_type: Optional[pulumi.Input[str]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 local_vpc: Optional[pulumi.Input['FirewallVpcFirewallCenLocalVpcArgs']] = None,
                 member_uid: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 vpc_firewall_id: Optional[pulumi.Input[str]] = None,
                 vpc_firewall_name: Optional[pulumi.Input[str]] = None,
                 vpc_region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FirewallVpcFirewallCen resources.
        :param pulumi.Input[str] cen_id: The ID of the CEN instance.
        :param pulumi.Input[str] connect_type: Intercommunication type, value: expressconnect: Express Channel cen: Cloud Enterprise Network
        :param pulumi.Input[str] lang: The language type of the requested and received messages. Valid values:
        :param pulumi.Input['FirewallVpcFirewallCenLocalVpcArgs'] local_vpc: The details of the VPC. See `local_vpc` below.
        :param pulumi.Input[str] member_uid: The UID of the member account (other Alibaba Cloud account) of the current Alibaba cloud account.
        :param pulumi.Input[str] status: Firewall switch status.
        :param pulumi.Input[str] vpc_firewall_id: VPC firewall ID
        :param pulumi.Input[str] vpc_firewall_name: The name of the VPC firewall instance.
        :param pulumi.Input[str] vpc_region: The ID of the region to which the VPC is created.
        """
        if cen_id is not None:
            pulumi.set(__self__, "cen_id", cen_id)
        if connect_type is not None:
            pulumi.set(__self__, "connect_type", connect_type)
        if lang is not None:
            pulumi.set(__self__, "lang", lang)
        if local_vpc is not None:
            pulumi.set(__self__, "local_vpc", local_vpc)
        if member_uid is not None:
            pulumi.set(__self__, "member_uid", member_uid)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if vpc_firewall_id is not None:
            pulumi.set(__self__, "vpc_firewall_id", vpc_firewall_id)
        if vpc_firewall_name is not None:
            pulumi.set(__self__, "vpc_firewall_name", vpc_firewall_name)
        if vpc_region is not None:
            pulumi.set(__self__, "vpc_region", vpc_region)

    @property
    @pulumi.getter(name="cenId")
    def cen_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the CEN instance.
        """
        return pulumi.get(self, "cen_id")

    @cen_id.setter
    def cen_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cen_id", value)

    @property
    @pulumi.getter(name="connectType")
    def connect_type(self) -> Optional[pulumi.Input[str]]:
        """
        Intercommunication type, value: expressconnect: Express Channel cen: Cloud Enterprise Network
        """
        return pulumi.get(self, "connect_type")

    @connect_type.setter
    def connect_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connect_type", value)

    @property
    @pulumi.getter
    def lang(self) -> Optional[pulumi.Input[str]]:
        """
        The language type of the requested and received messages. Valid values:
        """
        return pulumi.get(self, "lang")

    @lang.setter
    def lang(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lang", value)

    @property
    @pulumi.getter(name="localVpc")
    def local_vpc(self) -> Optional[pulumi.Input['FirewallVpcFirewallCenLocalVpcArgs']]:
        """
        The details of the VPC. See `local_vpc` below.
        """
        return pulumi.get(self, "local_vpc")

    @local_vpc.setter
    def local_vpc(self, value: Optional[pulumi.Input['FirewallVpcFirewallCenLocalVpcArgs']]):
        pulumi.set(self, "local_vpc", value)

    @property
    @pulumi.getter(name="memberUid")
    def member_uid(self) -> Optional[pulumi.Input[str]]:
        """
        The UID of the member account (other Alibaba Cloud account) of the current Alibaba cloud account.
        """
        return pulumi.get(self, "member_uid")

    @member_uid.setter
    def member_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member_uid", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Firewall switch status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="vpcFirewallId")
    def vpc_firewall_id(self) -> Optional[pulumi.Input[str]]:
        """
        VPC firewall ID
        """
        return pulumi.get(self, "vpc_firewall_id")

    @vpc_firewall_id.setter
    def vpc_firewall_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_firewall_id", value)

    @property
    @pulumi.getter(name="vpcFirewallName")
    def vpc_firewall_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the VPC firewall instance.
        """
        return pulumi.get(self, "vpc_firewall_name")

    @vpc_firewall_name.setter
    def vpc_firewall_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_firewall_name", value)

    @property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the region to which the VPC is created.
        """
        return pulumi.get(self, "vpc_region")

    @vpc_region.setter
    def vpc_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_region", value)


class FirewallVpcFirewallCen(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cen_id: Optional[pulumi.Input[str]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 local_vpc: Optional[pulumi.Input[pulumi.InputType['FirewallVpcFirewallCenLocalVpcArgs']]] = None,
                 member_uid: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 vpc_firewall_name: Optional[pulumi.Input[str]] = None,
                 vpc_region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Cloud Firewall Vpc Firewall Cen resource.

        For information about Cloud Firewall Vpc Firewall Cen and how to use it, see [What is Vpc Firewall Cen](https://www.alibabacloud.com/help/en/cloud-firewall/latest/createvpcfirewallcenconfigure).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # These resource primary keys should be replaced with your actual values.
        default = alicloud.cloudfirewall.FirewallVpcFirewallCen("default",
            cen_id="cen-xxx",
            local_vpc=alicloud.cloudfirewall.FirewallVpcFirewallCenLocalVpcArgs(
                network_instance_id="vpc-xxx",
            ),
            status="open",
            member_uid="14151*****827022",
            vpc_region="cn-hangzhou",
            vpc_firewall_name="tf-vpc-firewall-name")
        ```

        ## Import

        Cloud Firewall Vpc Firewall Cen can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cloudfirewall/firewallVpcFirewallCen:FirewallVpcFirewallCen example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cen_id: The ID of the CEN instance.
        :param pulumi.Input[str] lang: The language type of the requested and received messages. Valid values:
        :param pulumi.Input[pulumi.InputType['FirewallVpcFirewallCenLocalVpcArgs']] local_vpc: The details of the VPC. See `local_vpc` below.
        :param pulumi.Input[str] member_uid: The UID of the member account (other Alibaba Cloud account) of the current Alibaba cloud account.
        :param pulumi.Input[str] status: Firewall switch status.
        :param pulumi.Input[str] vpc_firewall_name: The name of the VPC firewall instance.
        :param pulumi.Input[str] vpc_region: The ID of the region to which the VPC is created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallVpcFirewallCenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloud Firewall Vpc Firewall Cen resource.

        For information about Cloud Firewall Vpc Firewall Cen and how to use it, see [What is Vpc Firewall Cen](https://www.alibabacloud.com/help/en/cloud-firewall/latest/createvpcfirewallcenconfigure).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # These resource primary keys should be replaced with your actual values.
        default = alicloud.cloudfirewall.FirewallVpcFirewallCen("default",
            cen_id="cen-xxx",
            local_vpc=alicloud.cloudfirewall.FirewallVpcFirewallCenLocalVpcArgs(
                network_instance_id="vpc-xxx",
            ),
            status="open",
            member_uid="14151*****827022",
            vpc_region="cn-hangzhou",
            vpc_firewall_name="tf-vpc-firewall-name")
        ```

        ## Import

        Cloud Firewall Vpc Firewall Cen can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cloudfirewall/firewallVpcFirewallCen:FirewallVpcFirewallCen example <id>
        ```

        :param str resource_name: The name of the resource.
        :param FirewallVpcFirewallCenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallVpcFirewallCenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cen_id: Optional[pulumi.Input[str]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 local_vpc: Optional[pulumi.Input[pulumi.InputType['FirewallVpcFirewallCenLocalVpcArgs']]] = None,
                 member_uid: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 vpc_firewall_name: Optional[pulumi.Input[str]] = None,
                 vpc_region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallVpcFirewallCenArgs.__new__(FirewallVpcFirewallCenArgs)

            if cen_id is None and not opts.urn:
                raise TypeError("Missing required property 'cen_id'")
            __props__.__dict__["cen_id"] = cen_id
            __props__.__dict__["lang"] = lang
            if local_vpc is None and not opts.urn:
                raise TypeError("Missing required property 'local_vpc'")
            __props__.__dict__["local_vpc"] = local_vpc
            __props__.__dict__["member_uid"] = member_uid
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
            if vpc_firewall_name is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_firewall_name'")
            __props__.__dict__["vpc_firewall_name"] = vpc_firewall_name
            if vpc_region is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_region'")
            __props__.__dict__["vpc_region"] = vpc_region
            __props__.__dict__["connect_type"] = None
            __props__.__dict__["vpc_firewall_id"] = None
        super(FirewallVpcFirewallCen, __self__).__init__(
            'alicloud:cloudfirewall/firewallVpcFirewallCen:FirewallVpcFirewallCen',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cen_id: Optional[pulumi.Input[str]] = None,
            connect_type: Optional[pulumi.Input[str]] = None,
            lang: Optional[pulumi.Input[str]] = None,
            local_vpc: Optional[pulumi.Input[pulumi.InputType['FirewallVpcFirewallCenLocalVpcArgs']]] = None,
            member_uid: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            vpc_firewall_id: Optional[pulumi.Input[str]] = None,
            vpc_firewall_name: Optional[pulumi.Input[str]] = None,
            vpc_region: Optional[pulumi.Input[str]] = None) -> 'FirewallVpcFirewallCen':
        """
        Get an existing FirewallVpcFirewallCen resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cen_id: The ID of the CEN instance.
        :param pulumi.Input[str] connect_type: Intercommunication type, value: expressconnect: Express Channel cen: Cloud Enterprise Network
        :param pulumi.Input[str] lang: The language type of the requested and received messages. Valid values:
        :param pulumi.Input[pulumi.InputType['FirewallVpcFirewallCenLocalVpcArgs']] local_vpc: The details of the VPC. See `local_vpc` below.
        :param pulumi.Input[str] member_uid: The UID of the member account (other Alibaba Cloud account) of the current Alibaba cloud account.
        :param pulumi.Input[str] status: Firewall switch status.
        :param pulumi.Input[str] vpc_firewall_id: VPC firewall ID
        :param pulumi.Input[str] vpc_firewall_name: The name of the VPC firewall instance.
        :param pulumi.Input[str] vpc_region: The ID of the region to which the VPC is created.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallVpcFirewallCenState.__new__(_FirewallVpcFirewallCenState)

        __props__.__dict__["cen_id"] = cen_id
        __props__.__dict__["connect_type"] = connect_type
        __props__.__dict__["lang"] = lang
        __props__.__dict__["local_vpc"] = local_vpc
        __props__.__dict__["member_uid"] = member_uid
        __props__.__dict__["status"] = status
        __props__.__dict__["vpc_firewall_id"] = vpc_firewall_id
        __props__.__dict__["vpc_firewall_name"] = vpc_firewall_name
        __props__.__dict__["vpc_region"] = vpc_region
        return FirewallVpcFirewallCen(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cenId")
    def cen_id(self) -> pulumi.Output[str]:
        """
        The ID of the CEN instance.
        """
        return pulumi.get(self, "cen_id")

    @property
    @pulumi.getter(name="connectType")
    def connect_type(self) -> pulumi.Output[str]:
        """
        Intercommunication type, value: expressconnect: Express Channel cen: Cloud Enterprise Network
        """
        return pulumi.get(self, "connect_type")

    @property
    @pulumi.getter
    def lang(self) -> pulumi.Output[Optional[str]]:
        """
        The language type of the requested and received messages. Valid values:
        """
        return pulumi.get(self, "lang")

    @property
    @pulumi.getter(name="localVpc")
    def local_vpc(self) -> pulumi.Output['outputs.FirewallVpcFirewallCenLocalVpc']:
        """
        The details of the VPC. See `local_vpc` below.
        """
        return pulumi.get(self, "local_vpc")

    @property
    @pulumi.getter(name="memberUid")
    def member_uid(self) -> pulumi.Output[Optional[str]]:
        """
        The UID of the member account (other Alibaba Cloud account) of the current Alibaba cloud account.
        """
        return pulumi.get(self, "member_uid")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Firewall switch status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcFirewallId")
    def vpc_firewall_id(self) -> pulumi.Output[str]:
        """
        VPC firewall ID
        """
        return pulumi.get(self, "vpc_firewall_id")

    @property
    @pulumi.getter(name="vpcFirewallName")
    def vpc_firewall_name(self) -> pulumi.Output[str]:
        """
        The name of the VPC firewall instance.
        """
        return pulumi.get(self, "vpc_firewall_name")

    @property
    @pulumi.getter(name="vpcRegion")
    def vpc_region(self) -> pulumi.Output[str]:
        """
        The ID of the region to which the VPC is created.
        """
        return pulumi.get(self, "vpc_region")

