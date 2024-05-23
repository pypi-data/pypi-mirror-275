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

__all__ = ['AliasArgs', 'Alias']

@pulumi.input_type
class AliasArgs:
    def __init__(__self__, *,
                 alias_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 service_version: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 routing_config: Optional[pulumi.Input['AliasRoutingConfigArgs']] = None):
        """
        The set of arguments for constructing a Alias resource.
        :param pulumi.Input[str] alias_name: Name for the alias you are creating.
        :param pulumi.Input[str] service_name: The Function Compute service name.
        :param pulumi.Input[str] service_version: The Function Compute service version for which you are creating the alias. Pattern: (LATEST|[0-9]+).
        :param pulumi.Input[str] description: Description of the alias.
        :param pulumi.Input['AliasRoutingConfigArgs'] routing_config: The Function Compute alias' route configuration settings. See `routing_config` below.
        """
        pulumi.set(__self__, "alias_name", alias_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "service_version", service_version)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if routing_config is not None:
            pulumi.set(__self__, "routing_config", routing_config)

    @property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> pulumi.Input[str]:
        """
        Name for the alias you are creating.
        """
        return pulumi.get(self, "alias_name")

    @alias_name.setter
    def alias_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "alias_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The Function Compute service name.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="serviceVersion")
    def service_version(self) -> pulumi.Input[str]:
        """
        The Function Compute service version for which you are creating the alias. Pattern: (LATEST|[0-9]+).
        """
        return pulumi.get(self, "service_version")

    @service_version.setter
    def service_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the alias.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> Optional[pulumi.Input['AliasRoutingConfigArgs']]:
        """
        The Function Compute alias' route configuration settings. See `routing_config` below.
        """
        return pulumi.get(self, "routing_config")

    @routing_config.setter
    def routing_config(self, value: Optional[pulumi.Input['AliasRoutingConfigArgs']]):
        pulumi.set(self, "routing_config", value)


@pulumi.input_type
class _AliasState:
    def __init__(__self__, *,
                 alias_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 routing_config: Optional[pulumi.Input['AliasRoutingConfigArgs']] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Alias resources.
        :param pulumi.Input[str] alias_name: Name for the alias you are creating.
        :param pulumi.Input[str] description: Description of the alias.
        :param pulumi.Input['AliasRoutingConfigArgs'] routing_config: The Function Compute alias' route configuration settings. See `routing_config` below.
        :param pulumi.Input[str] service_name: The Function Compute service name.
        :param pulumi.Input[str] service_version: The Function Compute service version for which you are creating the alias. Pattern: (LATEST|[0-9]+).
        """
        if alias_name is not None:
            pulumi.set(__self__, "alias_name", alias_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if routing_config is not None:
            pulumi.set(__self__, "routing_config", routing_config)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if service_version is not None:
            pulumi.set(__self__, "service_version", service_version)

    @property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for the alias you are creating.
        """
        return pulumi.get(self, "alias_name")

    @alias_name.setter
    def alias_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the alias.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> Optional[pulumi.Input['AliasRoutingConfigArgs']]:
        """
        The Function Compute alias' route configuration settings. See `routing_config` below.
        """
        return pulumi.get(self, "routing_config")

    @routing_config.setter
    def routing_config(self, value: Optional[pulumi.Input['AliasRoutingConfigArgs']]):
        pulumi.set(self, "routing_config", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Function Compute service name.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="serviceVersion")
    def service_version(self) -> Optional[pulumi.Input[str]]:
        """
        The Function Compute service version for which you are creating the alias. Pattern: (LATEST|[0-9]+).
        """
        return pulumi.get(self, "service_version")

    @service_version.setter
    def service_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_version", value)


class Alias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 routing_config: Optional[pulumi.Input[pulumi.InputType['AliasRoutingConfigArgs']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a Function Compute service alias. Creates an alias that points to the specified Function Compute service version.
         For the detailed information, please refer to the [developer guide](https://www.alibabacloud.com/help/en/fc/developer-reference/api-createalias).

        > **NOTE:** Available since v1.104.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud
        import pulumi_random as random

        default = random.index.Integer("default",
            max=99999,
            min=10000)
        default_service = alicloud.fc.Service("default",
            name=f"example-value-{default['result']}",
            description="example-value",
            publish=True)
        example = alicloud.fc.Alias("example",
            alias_name="example-value",
            description="example-value",
            service_name=default_service.name,
            service_version="1")
        ```

        ## Import

        Function Compute alias can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:fc/alias:Alias example my_alias_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias_name: Name for the alias you are creating.
        :param pulumi.Input[str] description: Description of the alias.
        :param pulumi.Input[pulumi.InputType['AliasRoutingConfigArgs']] routing_config: The Function Compute alias' route configuration settings. See `routing_config` below.
        :param pulumi.Input[str] service_name: The Function Compute service name.
        :param pulumi.Input[str] service_version: The Function Compute service version for which you are creating the alias. Pattern: (LATEST|[0-9]+).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Function Compute service alias. Creates an alias that points to the specified Function Compute service version.
         For the detailed information, please refer to the [developer guide](https://www.alibabacloud.com/help/en/fc/developer-reference/api-createalias).

        > **NOTE:** Available since v1.104.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud
        import pulumi_random as random

        default = random.index.Integer("default",
            max=99999,
            min=10000)
        default_service = alicloud.fc.Service("default",
            name=f"example-value-{default['result']}",
            description="example-value",
            publish=True)
        example = alicloud.fc.Alias("example",
            alias_name="example-value",
            description="example-value",
            service_name=default_service.name,
            service_version="1")
        ```

        ## Import

        Function Compute alias can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:fc/alias:Alias example my_alias_id
        ```

        :param str resource_name: The name of the resource.
        :param AliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 routing_config: Optional[pulumi.Input[pulumi.InputType['AliasRoutingConfigArgs']]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AliasArgs.__new__(AliasArgs)

            if alias_name is None and not opts.urn:
                raise TypeError("Missing required property 'alias_name'")
            __props__.__dict__["alias_name"] = alias_name
            __props__.__dict__["description"] = description
            __props__.__dict__["routing_config"] = routing_config
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if service_version is None and not opts.urn:
                raise TypeError("Missing required property 'service_version'")
            __props__.__dict__["service_version"] = service_version
        super(Alias, __self__).__init__(
            'alicloud:fc/alias:Alias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            alias_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            routing_config: Optional[pulumi.Input[pulumi.InputType['AliasRoutingConfigArgs']]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            service_version: Optional[pulumi.Input[str]] = None) -> 'Alias':
        """
        Get an existing Alias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias_name: Name for the alias you are creating.
        :param pulumi.Input[str] description: Description of the alias.
        :param pulumi.Input[pulumi.InputType['AliasRoutingConfigArgs']] routing_config: The Function Compute alias' route configuration settings. See `routing_config` below.
        :param pulumi.Input[str] service_name: The Function Compute service name.
        :param pulumi.Input[str] service_version: The Function Compute service version for which you are creating the alias. Pattern: (LATEST|[0-9]+).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AliasState.__new__(_AliasState)

        __props__.__dict__["alias_name"] = alias_name
        __props__.__dict__["description"] = description
        __props__.__dict__["routing_config"] = routing_config
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["service_version"] = service_version
        return Alias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> pulumi.Output[str]:
        """
        Name for the alias you are creating.
        """
        return pulumi.get(self, "alias_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the alias.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="routingConfig")
    def routing_config(self) -> pulumi.Output[Optional['outputs.AliasRoutingConfig']]:
        """
        The Function Compute alias' route configuration settings. See `routing_config` below.
        """
        return pulumi.get(self, "routing_config")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The Function Compute service name.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="serviceVersion")
    def service_version(self) -> pulumi.Output[str]:
        """
        The Function Compute service version for which you are creating the alias. Pattern: (LATEST|[0-9]+).
        """
        return pulumi.get(self, "service_version")

