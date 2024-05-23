# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BasicAccelerateIpArgs', 'BasicAccelerateIp']

@pulumi.input_type
class BasicAccelerateIpArgs:
    def __init__(__self__, *,
                 accelerator_id: pulumi.Input[str],
                 ip_set_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a BasicAccelerateIp resource.
        :param pulumi.Input[str] accelerator_id: The ID of the Basic GA instance.
        :param pulumi.Input[str] ip_set_id: The ID of the Basic Ip Set.
        """
        pulumi.set(__self__, "accelerator_id", accelerator_id)
        pulumi.set(__self__, "ip_set_id", ip_set_id)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Input[str]:
        """
        The ID of the Basic GA instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter(name="ipSetId")
    def ip_set_id(self) -> pulumi.Input[str]:
        """
        The ID of the Basic Ip Set.
        """
        return pulumi.get(self, "ip_set_id")

    @ip_set_id.setter
    def ip_set_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_set_id", value)


@pulumi.input_type
class _BasicAccelerateIpState:
    def __init__(__self__, *,
                 accelerate_ip_address: Optional[pulumi.Input[str]] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 ip_set_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BasicAccelerateIp resources.
        :param pulumi.Input[str] accelerate_ip_address: The address of the Basic Accelerate IP.
        :param pulumi.Input[str] accelerator_id: The ID of the Basic GA instance.
        :param pulumi.Input[str] ip_set_id: The ID of the Basic Ip Set.
        :param pulumi.Input[str] status: The status of the Basic Accelerate IP instance.
        """
        if accelerate_ip_address is not None:
            pulumi.set(__self__, "accelerate_ip_address", accelerate_ip_address)
        if accelerator_id is not None:
            pulumi.set(__self__, "accelerator_id", accelerator_id)
        if ip_set_id is not None:
            pulumi.set(__self__, "ip_set_id", ip_set_id)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="accelerateIpAddress")
    def accelerate_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The address of the Basic Accelerate IP.
        """
        return pulumi.get(self, "accelerate_ip_address")

    @accelerate_ip_address.setter
    def accelerate_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerate_ip_address", value)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Basic GA instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter(name="ipSetId")
    def ip_set_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Basic Ip Set.
        """
        return pulumi.get(self, "ip_set_id")

    @ip_set_id.setter
    def ip_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_set_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Basic Accelerate IP instance.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class BasicAccelerateIp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 ip_set_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Global Accelerator (GA) Basic Accelerate IP resource.

        For information about Global Accelerator (GA) Basic Accelerate IP and how to use it, see [What is Basic Accelerate IP](https://www.alibabacloud.com/help/en/global-accelerator/latest/api-ga-2019-11-20-createbasicaccelerateip).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-hangzhou"
        default = alicloud.ga.BasicAccelerator("default",
            duration=1,
            basic_accelerator_name="terraform-example",
            description="terraform-example",
            bandwidth_billing_type="CDT",
            auto_use_coupon="true",
            auto_pay=True)
        default_basic_ip_set = alicloud.ga.BasicIpSet("default",
            accelerator_id=default.id,
            accelerate_region_id=region,
            isp_type="BGP",
            bandwidth=5)
        default_basic_accelerate_ip = alicloud.ga.BasicAccelerateIp("default",
            accelerator_id=default.id,
            ip_set_id=default_basic_ip_set.id)
        ```

        ## Import

        Global Accelerator (GA) Basic Accelerate IP can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:ga/basicAccelerateIp:BasicAccelerateIp example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_id: The ID of the Basic GA instance.
        :param pulumi.Input[str] ip_set_id: The ID of the Basic Ip Set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BasicAccelerateIpArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global Accelerator (GA) Basic Accelerate IP resource.

        For information about Global Accelerator (GA) Basic Accelerate IP and how to use it, see [What is Basic Accelerate IP](https://www.alibabacloud.com/help/en/global-accelerator/latest/api-ga-2019-11-20-createbasicaccelerateip).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        region = config.get("region")
        if region is None:
            region = "cn-hangzhou"
        default = alicloud.ga.BasicAccelerator("default",
            duration=1,
            basic_accelerator_name="terraform-example",
            description="terraform-example",
            bandwidth_billing_type="CDT",
            auto_use_coupon="true",
            auto_pay=True)
        default_basic_ip_set = alicloud.ga.BasicIpSet("default",
            accelerator_id=default.id,
            accelerate_region_id=region,
            isp_type="BGP",
            bandwidth=5)
        default_basic_accelerate_ip = alicloud.ga.BasicAccelerateIp("default",
            accelerator_id=default.id,
            ip_set_id=default_basic_ip_set.id)
        ```

        ## Import

        Global Accelerator (GA) Basic Accelerate IP can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:ga/basicAccelerateIp:BasicAccelerateIp example <id>
        ```

        :param str resource_name: The name of the resource.
        :param BasicAccelerateIpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BasicAccelerateIpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 ip_set_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BasicAccelerateIpArgs.__new__(BasicAccelerateIpArgs)

            if accelerator_id is None and not opts.urn:
                raise TypeError("Missing required property 'accelerator_id'")
            __props__.__dict__["accelerator_id"] = accelerator_id
            if ip_set_id is None and not opts.urn:
                raise TypeError("Missing required property 'ip_set_id'")
            __props__.__dict__["ip_set_id"] = ip_set_id
            __props__.__dict__["accelerate_ip_address"] = None
            __props__.__dict__["status"] = None
        super(BasicAccelerateIp, __self__).__init__(
            'alicloud:ga/basicAccelerateIp:BasicAccelerateIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accelerate_ip_address: Optional[pulumi.Input[str]] = None,
            accelerator_id: Optional[pulumi.Input[str]] = None,
            ip_set_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'BasicAccelerateIp':
        """
        Get an existing BasicAccelerateIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerate_ip_address: The address of the Basic Accelerate IP.
        :param pulumi.Input[str] accelerator_id: The ID of the Basic GA instance.
        :param pulumi.Input[str] ip_set_id: The ID of the Basic Ip Set.
        :param pulumi.Input[str] status: The status of the Basic Accelerate IP instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BasicAccelerateIpState.__new__(_BasicAccelerateIpState)

        __props__.__dict__["accelerate_ip_address"] = accelerate_ip_address
        __props__.__dict__["accelerator_id"] = accelerator_id
        __props__.__dict__["ip_set_id"] = ip_set_id
        __props__.__dict__["status"] = status
        return BasicAccelerateIp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accelerateIpAddress")
    def accelerate_ip_address(self) -> pulumi.Output[str]:
        """
        The address of the Basic Accelerate IP.
        """
        return pulumi.get(self, "accelerate_ip_address")

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Output[str]:
        """
        The ID of the Basic GA instance.
        """
        return pulumi.get(self, "accelerator_id")

    @property
    @pulumi.getter(name="ipSetId")
    def ip_set_id(self) -> pulumi.Output[str]:
        """
        The ID of the Basic Ip Set.
        """
        return pulumi.get(self, "ip_set_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Basic Accelerate IP instance.
        """
        return pulumi.get(self, "status")

