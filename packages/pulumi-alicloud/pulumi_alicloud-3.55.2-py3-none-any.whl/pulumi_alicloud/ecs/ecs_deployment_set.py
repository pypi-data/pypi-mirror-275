# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EcsDeploymentSetArgs', 'EcsDeploymentSet']

@pulumi.input_type
class EcsDeploymentSetArgs:
    def __init__(__self__, *,
                 deployment_set_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 granularity: Optional[pulumi.Input[str]] = None,
                 on_unable_to_redeploy_failed_instance: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EcsDeploymentSet resource.
        :param pulumi.Input[str] deployment_set_name: The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        :param pulumi.Input[str] description: The description of the deployment set. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        :param pulumi.Input[str] domain: The deployment domain. Valid values: `Default`.
        :param pulumi.Input[str] granularity: The deployment granularity. Valid values: `Host`.
        :param pulumi.Input[str] on_unable_to_redeploy_failed_instance: The on unable to redeploy failed instance. Valid values: `CancelMembershipAndStart`, `KeepStopped`.
        :param pulumi.Input[str] strategy: The deployment strategy. Valid values: `Availability`(Default), `AvailabilityGroup`, `LowLatency`.
        """
        if deployment_set_name is not None:
            pulumi.set(__self__, "deployment_set_name", deployment_set_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if granularity is not None:
            pulumi.set(__self__, "granularity", granularity)
        if on_unable_to_redeploy_failed_instance is not None:
            pulumi.set(__self__, "on_unable_to_redeploy_failed_instance", on_unable_to_redeploy_failed_instance)
        if strategy is not None:
            pulumi.set(__self__, "strategy", strategy)

    @property
    @pulumi.getter(name="deploymentSetName")
    def deployment_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        """
        return pulumi.get(self, "deployment_set_name")

    @deployment_set_name.setter
    def deployment_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_set_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the deployment set. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment domain. Valid values: `Default`.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def granularity(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment granularity. Valid values: `Host`.
        """
        return pulumi.get(self, "granularity")

    @granularity.setter
    def granularity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "granularity", value)

    @property
    @pulumi.getter(name="onUnableToRedeployFailedInstance")
    def on_unable_to_redeploy_failed_instance(self) -> Optional[pulumi.Input[str]]:
        """
        The on unable to redeploy failed instance. Valid values: `CancelMembershipAndStart`, `KeepStopped`.
        """
        return pulumi.get(self, "on_unable_to_redeploy_failed_instance")

    @on_unable_to_redeploy_failed_instance.setter
    def on_unable_to_redeploy_failed_instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "on_unable_to_redeploy_failed_instance", value)

    @property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment strategy. Valid values: `Availability`(Default), `AvailabilityGroup`, `LowLatency`.
        """
        return pulumi.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strategy", value)


@pulumi.input_type
class _EcsDeploymentSetState:
    def __init__(__self__, *,
                 deployment_set_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 granularity: Optional[pulumi.Input[str]] = None,
                 on_unable_to_redeploy_failed_instance: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EcsDeploymentSet resources.
        :param pulumi.Input[str] deployment_set_name: The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        :param pulumi.Input[str] description: The description of the deployment set. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        :param pulumi.Input[str] domain: The deployment domain. Valid values: `Default`.
        :param pulumi.Input[str] granularity: The deployment granularity. Valid values: `Host`.
        :param pulumi.Input[str] on_unable_to_redeploy_failed_instance: The on unable to redeploy failed instance. Valid values: `CancelMembershipAndStart`, `KeepStopped`.
        :param pulumi.Input[str] strategy: The deployment strategy. Valid values: `Availability`(Default), `AvailabilityGroup`, `LowLatency`.
        """
        if deployment_set_name is not None:
            pulumi.set(__self__, "deployment_set_name", deployment_set_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if granularity is not None:
            pulumi.set(__self__, "granularity", granularity)
        if on_unable_to_redeploy_failed_instance is not None:
            pulumi.set(__self__, "on_unable_to_redeploy_failed_instance", on_unable_to_redeploy_failed_instance)
        if strategy is not None:
            pulumi.set(__self__, "strategy", strategy)

    @property
    @pulumi.getter(name="deploymentSetName")
    def deployment_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        """
        return pulumi.get(self, "deployment_set_name")

    @deployment_set_name.setter
    def deployment_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_set_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the deployment set. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment domain. Valid values: `Default`.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def granularity(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment granularity. Valid values: `Host`.
        """
        return pulumi.get(self, "granularity")

    @granularity.setter
    def granularity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "granularity", value)

    @property
    @pulumi.getter(name="onUnableToRedeployFailedInstance")
    def on_unable_to_redeploy_failed_instance(self) -> Optional[pulumi.Input[str]]:
        """
        The on unable to redeploy failed instance. Valid values: `CancelMembershipAndStart`, `KeepStopped`.
        """
        return pulumi.get(self, "on_unable_to_redeploy_failed_instance")

    @on_unable_to_redeploy_failed_instance.setter
    def on_unable_to_redeploy_failed_instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "on_unable_to_redeploy_failed_instance", value)

    @property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment strategy. Valid values: `Availability`(Default), `AvailabilityGroup`, `LowLatency`.
        """
        return pulumi.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strategy", value)


class EcsDeploymentSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_set_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 granularity: Optional[pulumi.Input[str]] = None,
                 on_unable_to_redeploy_failed_instance: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a ECS Deployment Set resource.

        For information about ECS Deployment Set and how to use it, see [What is Deployment Set](https://www.alibabacloud.com/help/en/doc-detail/91269.htm).

        > **NOTE:** Available since v1.140.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.EcsDeploymentSet("default",
            strategy="Availability",
            domain="Default",
            granularity="Host",
            deployment_set_name="example_value",
            description="example_value")
        ```

        ## Import

        ECS Deployment Set can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:ecs/ecsDeploymentSet:EcsDeploymentSet example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_set_name: The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        :param pulumi.Input[str] description: The description of the deployment set. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        :param pulumi.Input[str] domain: The deployment domain. Valid values: `Default`.
        :param pulumi.Input[str] granularity: The deployment granularity. Valid values: `Host`.
        :param pulumi.Input[str] on_unable_to_redeploy_failed_instance: The on unable to redeploy failed instance. Valid values: `CancelMembershipAndStart`, `KeepStopped`.
        :param pulumi.Input[str] strategy: The deployment strategy. Valid values: `Availability`(Default), `AvailabilityGroup`, `LowLatency`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[EcsDeploymentSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a ECS Deployment Set resource.

        For information about ECS Deployment Set and how to use it, see [What is Deployment Set](https://www.alibabacloud.com/help/en/doc-detail/91269.htm).

        > **NOTE:** Available since v1.140.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.EcsDeploymentSet("default",
            strategy="Availability",
            domain="Default",
            granularity="Host",
            deployment_set_name="example_value",
            description="example_value")
        ```

        ## Import

        ECS Deployment Set can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:ecs/ecsDeploymentSet:EcsDeploymentSet example <id>
        ```

        :param str resource_name: The name of the resource.
        :param EcsDeploymentSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EcsDeploymentSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_set_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 granularity: Optional[pulumi.Input[str]] = None,
                 on_unable_to_redeploy_failed_instance: Optional[pulumi.Input[str]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EcsDeploymentSetArgs.__new__(EcsDeploymentSetArgs)

            __props__.__dict__["deployment_set_name"] = deployment_set_name
            __props__.__dict__["description"] = description
            __props__.__dict__["domain"] = domain
            __props__.__dict__["granularity"] = granularity
            __props__.__dict__["on_unable_to_redeploy_failed_instance"] = on_unable_to_redeploy_failed_instance
            __props__.__dict__["strategy"] = strategy
        super(EcsDeploymentSet, __self__).__init__(
            'alicloud:ecs/ecsDeploymentSet:EcsDeploymentSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            deployment_set_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            granularity: Optional[pulumi.Input[str]] = None,
            on_unable_to_redeploy_failed_instance: Optional[pulumi.Input[str]] = None,
            strategy: Optional[pulumi.Input[str]] = None) -> 'EcsDeploymentSet':
        """
        Get an existing EcsDeploymentSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_set_name: The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        :param pulumi.Input[str] description: The description of the deployment set. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        :param pulumi.Input[str] domain: The deployment domain. Valid values: `Default`.
        :param pulumi.Input[str] granularity: The deployment granularity. Valid values: `Host`.
        :param pulumi.Input[str] on_unable_to_redeploy_failed_instance: The on unable to redeploy failed instance. Valid values: `CancelMembershipAndStart`, `KeepStopped`.
        :param pulumi.Input[str] strategy: The deployment strategy. Valid values: `Availability`(Default), `AvailabilityGroup`, `LowLatency`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EcsDeploymentSetState.__new__(_EcsDeploymentSetState)

        __props__.__dict__["deployment_set_name"] = deployment_set_name
        __props__.__dict__["description"] = description
        __props__.__dict__["domain"] = domain
        __props__.__dict__["granularity"] = granularity
        __props__.__dict__["on_unable_to_redeploy_failed_instance"] = on_unable_to_redeploy_failed_instance
        __props__.__dict__["strategy"] = strategy
        return EcsDeploymentSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deploymentSetName")
    def deployment_set_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the deployment set. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        """
        return pulumi.get(self, "deployment_set_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the deployment set. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        """
        The deployment domain. Valid values: `Default`.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def granularity(self) -> pulumi.Output[Optional[str]]:
        """
        The deployment granularity. Valid values: `Host`.
        """
        return pulumi.get(self, "granularity")

    @property
    @pulumi.getter(name="onUnableToRedeployFailedInstance")
    def on_unable_to_redeploy_failed_instance(self) -> pulumi.Output[Optional[str]]:
        """
        The on unable to redeploy failed instance. Valid values: `CancelMembershipAndStart`, `KeepStopped`.
        """
        return pulumi.get(self, "on_unable_to_redeploy_failed_instance")

    @property
    @pulumi.getter
    def strategy(self) -> pulumi.Output[Optional[str]]:
        """
        The deployment strategy. Valid values: `Availability`(Default), `AvailabilityGroup`, `LowLatency`.
        """
        return pulumi.get(self, "strategy")

