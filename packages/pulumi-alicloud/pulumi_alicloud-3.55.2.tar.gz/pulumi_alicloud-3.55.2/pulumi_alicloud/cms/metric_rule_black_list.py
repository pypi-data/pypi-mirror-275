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

__all__ = ['MetricRuleBlackListArgs', 'MetricRuleBlackList']

@pulumi.input_type
class MetricRuleBlackListArgs:
    def __init__(__self__, *,
                 category: pulumi.Input[str],
                 instances: pulumi.Input[Sequence[pulumi.Input[str]]],
                 metric_rule_black_list_name: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 effective_time: Optional[pulumi.Input[str]] = None,
                 enable_end_time: Optional[pulumi.Input[str]] = None,
                 enable_start_time: Optional[pulumi.Input[str]] = None,
                 is_enable: Optional[pulumi.Input[bool]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input['MetricRuleBlackListMetricArgs']]]] = None,
                 scope_type: Optional[pulumi.Input[str]] = None,
                 scope_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MetricRuleBlackList resource.
        :param pulumi.Input[str] category: Cloud service classification. For example, Redis includes kvstore_standard, kvstore_sharding, and kvstore_splitrw.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instances: The list of instances of cloud services specified in the alert blacklist policy.
        :param pulumi.Input[str] metric_rule_black_list_name: The name of the alert blacklist policy.
        :param pulumi.Input[str] namespace: The data namespace of the cloud service.
        :param pulumi.Input[str] effective_time: The effective time range of the alert blacklist policy.
        :param pulumi.Input[str] enable_end_time: The start timestamp of the alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[str] enable_start_time: The end timestamp of the alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[bool] is_enable: The status of the alert blacklist policy. Value:-true: enabled.-false: disabled.
        :param pulumi.Input[Sequence[pulumi.Input['MetricRuleBlackListMetricArgs']]] metrics: Monitoring metrics in the instance. See `metrics` below.
        :param pulumi.Input[str] scope_type: The effective range of the alert blacklist policy. Value:-USER: The alert blacklist policy only takes effect in the current Alibaba cloud account.-GROUP: The alert blacklist policy takes effect in the specified application GROUP.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_values: Application Group ID list. The format is JSON Array.> This parameter is displayed only when 'ScopeType' is 'GROUP.
        """
        pulumi.set(__self__, "category", category)
        pulumi.set(__self__, "instances", instances)
        pulumi.set(__self__, "metric_rule_black_list_name", metric_rule_black_list_name)
        pulumi.set(__self__, "namespace", namespace)
        if effective_time is not None:
            pulumi.set(__self__, "effective_time", effective_time)
        if enable_end_time is not None:
            pulumi.set(__self__, "enable_end_time", enable_end_time)
        if enable_start_time is not None:
            pulumi.set(__self__, "enable_start_time", enable_start_time)
        if is_enable is not None:
            pulumi.set(__self__, "is_enable", is_enable)
        if metrics is not None:
            pulumi.set(__self__, "metrics", metrics)
        if scope_type is not None:
            pulumi.set(__self__, "scope_type", scope_type)
        if scope_values is not None:
            pulumi.set(__self__, "scope_values", scope_values)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Input[str]:
        """
        Cloud service classification. For example, Redis includes kvstore_standard, kvstore_sharding, and kvstore_splitrw.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: pulumi.Input[str]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of instances of cloud services specified in the alert blacklist policy.
        """
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "instances", value)

    @property
    @pulumi.getter(name="metricRuleBlackListName")
    def metric_rule_black_list_name(self) -> pulumi.Input[str]:
        """
        The name of the alert blacklist policy.
        """
        return pulumi.get(self, "metric_rule_black_list_name")

    @metric_rule_black_list_name.setter
    def metric_rule_black_list_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "metric_rule_black_list_name", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        The data namespace of the cloud service.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[pulumi.Input[str]]:
        """
        The effective time range of the alert blacklist policy.
        """
        return pulumi.get(self, "effective_time")

    @effective_time.setter
    def effective_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "effective_time", value)

    @property
    @pulumi.getter(name="enableEndTime")
    def enable_end_time(self) -> Optional[pulumi.Input[str]]:
        """
        The start timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "enable_end_time")

    @enable_end_time.setter
    def enable_end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enable_end_time", value)

    @property
    @pulumi.getter(name="enableStartTime")
    def enable_start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The end timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "enable_start_time")

    @enable_start_time.setter
    def enable_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enable_start_time", value)

    @property
    @pulumi.getter(name="isEnable")
    def is_enable(self) -> Optional[pulumi.Input[bool]]:
        """
        The status of the alert blacklist policy. Value:-true: enabled.-false: disabled.
        """
        return pulumi.get(self, "is_enable")

    @is_enable.setter
    def is_enable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enable", value)

    @property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MetricRuleBlackListMetricArgs']]]]:
        """
        Monitoring metrics in the instance. See `metrics` below.
        """
        return pulumi.get(self, "metrics")

    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MetricRuleBlackListMetricArgs']]]]):
        pulumi.set(self, "metrics", value)

    @property
    @pulumi.getter(name="scopeType")
    def scope_type(self) -> Optional[pulumi.Input[str]]:
        """
        The effective range of the alert blacklist policy. Value:-USER: The alert blacklist policy only takes effect in the current Alibaba cloud account.-GROUP: The alert blacklist policy takes effect in the specified application GROUP.
        """
        return pulumi.get(self, "scope_type")

    @scope_type.setter
    def scope_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope_type", value)

    @property
    @pulumi.getter(name="scopeValues")
    def scope_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Application Group ID list. The format is JSON Array.> This parameter is displayed only when 'ScopeType' is 'GROUP.
        """
        return pulumi.get(self, "scope_values")

    @scope_values.setter
    def scope_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scope_values", value)


@pulumi.input_type
class _MetricRuleBlackListState:
    def __init__(__self__, *,
                 category: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 effective_time: Optional[pulumi.Input[str]] = None,
                 enable_end_time: Optional[pulumi.Input[str]] = None,
                 enable_start_time: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_enable: Optional[pulumi.Input[bool]] = None,
                 metric_rule_black_list_id: Optional[pulumi.Input[str]] = None,
                 metric_rule_black_list_name: Optional[pulumi.Input[str]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input['MetricRuleBlackListMetricArgs']]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 scope_type: Optional[pulumi.Input[str]] = None,
                 scope_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MetricRuleBlackList resources.
        :param pulumi.Input[str] category: Cloud service classification. For example, Redis includes kvstore_standard, kvstore_sharding, and kvstore_splitrw.
        :param pulumi.Input[str] create_time: The timestamp for creating an alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[str] effective_time: The effective time range of the alert blacklist policy.
        :param pulumi.Input[str] enable_end_time: The start timestamp of the alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[str] enable_start_time: The end timestamp of the alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instances: The list of instances of cloud services specified in the alert blacklist policy.
        :param pulumi.Input[bool] is_enable: The status of the alert blacklist policy. Value:-true: enabled.-false: disabled.
        :param pulumi.Input[str] metric_rule_black_list_id: The ID of the blacklist policy.
        :param pulumi.Input[str] metric_rule_black_list_name: The name of the alert blacklist policy.
        :param pulumi.Input[Sequence[pulumi.Input['MetricRuleBlackListMetricArgs']]] metrics: Monitoring metrics in the instance. See `metrics` below.
        :param pulumi.Input[str] namespace: The data namespace of the cloud service.
        :param pulumi.Input[str] scope_type: The effective range of the alert blacklist policy. Value:-USER: The alert blacklist policy only takes effect in the current Alibaba cloud account.-GROUP: The alert blacklist policy takes effect in the specified application GROUP.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_values: Application Group ID list. The format is JSON Array.> This parameter is displayed only when 'ScopeType' is 'GROUP.
        :param pulumi.Input[str] update_time: Modify the timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        if category is not None:
            pulumi.set(__self__, "category", category)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if effective_time is not None:
            pulumi.set(__self__, "effective_time", effective_time)
        if enable_end_time is not None:
            pulumi.set(__self__, "enable_end_time", enable_end_time)
        if enable_start_time is not None:
            pulumi.set(__self__, "enable_start_time", enable_start_time)
        if instances is not None:
            pulumi.set(__self__, "instances", instances)
        if is_enable is not None:
            pulumi.set(__self__, "is_enable", is_enable)
        if metric_rule_black_list_id is not None:
            pulumi.set(__self__, "metric_rule_black_list_id", metric_rule_black_list_id)
        if metric_rule_black_list_name is not None:
            pulumi.set(__self__, "metric_rule_black_list_name", metric_rule_black_list_name)
        if metrics is not None:
            pulumi.set(__self__, "metrics", metrics)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if scope_type is not None:
            pulumi.set(__self__, "scope_type", scope_type)
        if scope_values is not None:
            pulumi.set(__self__, "scope_values", scope_values)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud service classification. For example, Redis includes kvstore_standard, kvstore_sharding, and kvstore_splitrw.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The timestamp for creating an alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> Optional[pulumi.Input[str]]:
        """
        The effective time range of the alert blacklist policy.
        """
        return pulumi.get(self, "effective_time")

    @effective_time.setter
    def effective_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "effective_time", value)

    @property
    @pulumi.getter(name="enableEndTime")
    def enable_end_time(self) -> Optional[pulumi.Input[str]]:
        """
        The start timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "enable_end_time")

    @enable_end_time.setter
    def enable_end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enable_end_time", value)

    @property
    @pulumi.getter(name="enableStartTime")
    def enable_start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The end timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "enable_start_time")

    @enable_start_time.setter
    def enable_start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enable_start_time", value)

    @property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of instances of cloud services specified in the alert blacklist policy.
        """
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "instances", value)

    @property
    @pulumi.getter(name="isEnable")
    def is_enable(self) -> Optional[pulumi.Input[bool]]:
        """
        The status of the alert blacklist policy. Value:-true: enabled.-false: disabled.
        """
        return pulumi.get(self, "is_enable")

    @is_enable.setter
    def is_enable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enable", value)

    @property
    @pulumi.getter(name="metricRuleBlackListId")
    def metric_rule_black_list_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the blacklist policy.
        """
        return pulumi.get(self, "metric_rule_black_list_id")

    @metric_rule_black_list_id.setter
    def metric_rule_black_list_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_rule_black_list_id", value)

    @property
    @pulumi.getter(name="metricRuleBlackListName")
    def metric_rule_black_list_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the alert blacklist policy.
        """
        return pulumi.get(self, "metric_rule_black_list_name")

    @metric_rule_black_list_name.setter
    def metric_rule_black_list_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_rule_black_list_name", value)

    @property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MetricRuleBlackListMetricArgs']]]]:
        """
        Monitoring metrics in the instance. See `metrics` below.
        """
        return pulumi.get(self, "metrics")

    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MetricRuleBlackListMetricArgs']]]]):
        pulumi.set(self, "metrics", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The data namespace of the cloud service.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="scopeType")
    def scope_type(self) -> Optional[pulumi.Input[str]]:
        """
        The effective range of the alert blacklist policy. Value:-USER: The alert blacklist policy only takes effect in the current Alibaba cloud account.-GROUP: The alert blacklist policy takes effect in the specified application GROUP.
        """
        return pulumi.get(self, "scope_type")

    @scope_type.setter
    def scope_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope_type", value)

    @property
    @pulumi.getter(name="scopeValues")
    def scope_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Application Group ID list. The format is JSON Array.> This parameter is displayed only when 'ScopeType' is 'GROUP.
        """
        return pulumi.get(self, "scope_values")

    @scope_values.setter
    def scope_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scope_values", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        Modify the timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class MetricRuleBlackList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 effective_time: Optional[pulumi.Input[str]] = None,
                 enable_end_time: Optional[pulumi.Input[str]] = None,
                 enable_start_time: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_enable: Optional[pulumi.Input[bool]] = None,
                 metric_rule_black_list_name: Optional[pulumi.Input[str]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricRuleBlackListMetricArgs']]]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 scope_type: Optional[pulumi.Input[str]] = None,
                 scope_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Cloud Monitor Service Metric Rule Black List resource.

        For information about Cloud Monitor Service Metric Rule Black List and how to use it, see [What is Metric Rule Black List](https://www.alibabacloud.com/help/en/cloudmonitor/latest/describemetricruleblacklist).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default = alicloud.get_zones(available_resource_creation="Instance")
        default_get_instance_types = alicloud.ecs.get_instance_types(availability_zone=default.zones[0].id,
            cpu_core_count=1,
            memory_size=2)
        default_get_images = alicloud.ecs.get_images(name_regex="^ubuntu_[0-9]+_[0-9]+_x64*",
            owners="system")
        default_network = alicloud.vpc.Network("default",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("default",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default.zones[0].id)
        default_security_group = alicloud.ecs.SecurityGroup("default",
            name=name,
            vpc_id=default_network.id)
        default_instance = alicloud.ecs.Instance("default",
            availability_zone=default.zones[0].id,
            instance_name=name,
            image_id=default_get_images.images[0].id,
            instance_type=default_get_instance_types.instance_types[0].id,
            security_groups=[default_security_group.id],
            vswitch_id=default_switch.id)
        default_metric_rule_black_list = alicloud.cms.MetricRuleBlackList("default",
            instances=[default_instance.id.apply(lambda id: f"{{\\"instancceId\\":\\"{id}\\"}}")],
            metrics=[alicloud.cms.MetricRuleBlackListMetricArgs(
                metric_name="disk_utilization",
            )],
            category="ecs",
            enable_end_time="1799443209000",
            namespace="acs_ecs_dashboard",
            enable_start_time="1689243209000",
            metric_rule_black_list_name=name)
        ```

        ## Import

        Cloud Monitor Service Metric Rule Black List can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cms/metricRuleBlackList:MetricRuleBlackList example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: Cloud service classification. For example, Redis includes kvstore_standard, kvstore_sharding, and kvstore_splitrw.
        :param pulumi.Input[str] effective_time: The effective time range of the alert blacklist policy.
        :param pulumi.Input[str] enable_end_time: The start timestamp of the alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[str] enable_start_time: The end timestamp of the alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instances: The list of instances of cloud services specified in the alert blacklist policy.
        :param pulumi.Input[bool] is_enable: The status of the alert blacklist policy. Value:-true: enabled.-false: disabled.
        :param pulumi.Input[str] metric_rule_black_list_name: The name of the alert blacklist policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricRuleBlackListMetricArgs']]]] metrics: Monitoring metrics in the instance. See `metrics` below.
        :param pulumi.Input[str] namespace: The data namespace of the cloud service.
        :param pulumi.Input[str] scope_type: The effective range of the alert blacklist policy. Value:-USER: The alert blacklist policy only takes effect in the current Alibaba cloud account.-GROUP: The alert blacklist policy takes effect in the specified application GROUP.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_values: Application Group ID list. The format is JSON Array.> This parameter is displayed only when 'ScopeType' is 'GROUP.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetricRuleBlackListArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloud Monitor Service Metric Rule Black List resource.

        For information about Cloud Monitor Service Metric Rule Black List and how to use it, see [What is Metric Rule Black List](https://www.alibabacloud.com/help/en/cloudmonitor/latest/describemetricruleblacklist).

        > **NOTE:** Available since v1.194.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default = alicloud.get_zones(available_resource_creation="Instance")
        default_get_instance_types = alicloud.ecs.get_instance_types(availability_zone=default.zones[0].id,
            cpu_core_count=1,
            memory_size=2)
        default_get_images = alicloud.ecs.get_images(name_regex="^ubuntu_[0-9]+_[0-9]+_x64*",
            owners="system")
        default_network = alicloud.vpc.Network("default",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("default",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default.zones[0].id)
        default_security_group = alicloud.ecs.SecurityGroup("default",
            name=name,
            vpc_id=default_network.id)
        default_instance = alicloud.ecs.Instance("default",
            availability_zone=default.zones[0].id,
            instance_name=name,
            image_id=default_get_images.images[0].id,
            instance_type=default_get_instance_types.instance_types[0].id,
            security_groups=[default_security_group.id],
            vswitch_id=default_switch.id)
        default_metric_rule_black_list = alicloud.cms.MetricRuleBlackList("default",
            instances=[default_instance.id.apply(lambda id: f"{{\\"instancceId\\":\\"{id}\\"}}")],
            metrics=[alicloud.cms.MetricRuleBlackListMetricArgs(
                metric_name="disk_utilization",
            )],
            category="ecs",
            enable_end_time="1799443209000",
            namespace="acs_ecs_dashboard",
            enable_start_time="1689243209000",
            metric_rule_black_list_name=name)
        ```

        ## Import

        Cloud Monitor Service Metric Rule Black List can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cms/metricRuleBlackList:MetricRuleBlackList example <id>
        ```

        :param str resource_name: The name of the resource.
        :param MetricRuleBlackListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetricRuleBlackListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 effective_time: Optional[pulumi.Input[str]] = None,
                 enable_end_time: Optional[pulumi.Input[str]] = None,
                 enable_start_time: Optional[pulumi.Input[str]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 is_enable: Optional[pulumi.Input[bool]] = None,
                 metric_rule_black_list_name: Optional[pulumi.Input[str]] = None,
                 metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricRuleBlackListMetricArgs']]]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 scope_type: Optional[pulumi.Input[str]] = None,
                 scope_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MetricRuleBlackListArgs.__new__(MetricRuleBlackListArgs)

            if category is None and not opts.urn:
                raise TypeError("Missing required property 'category'")
            __props__.__dict__["category"] = category
            __props__.__dict__["effective_time"] = effective_time
            __props__.__dict__["enable_end_time"] = enable_end_time
            __props__.__dict__["enable_start_time"] = enable_start_time
            if instances is None and not opts.urn:
                raise TypeError("Missing required property 'instances'")
            __props__.__dict__["instances"] = instances
            __props__.__dict__["is_enable"] = is_enable
            if metric_rule_black_list_name is None and not opts.urn:
                raise TypeError("Missing required property 'metric_rule_black_list_name'")
            __props__.__dict__["metric_rule_black_list_name"] = metric_rule_black_list_name
            __props__.__dict__["metrics"] = metrics
            if namespace is None and not opts.urn:
                raise TypeError("Missing required property 'namespace'")
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["scope_type"] = scope_type
            __props__.__dict__["scope_values"] = scope_values
            __props__.__dict__["create_time"] = None
            __props__.__dict__["metric_rule_black_list_id"] = None
            __props__.__dict__["update_time"] = None
        super(MetricRuleBlackList, __self__).__init__(
            'alicloud:cms/metricRuleBlackList:MetricRuleBlackList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            category: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            effective_time: Optional[pulumi.Input[str]] = None,
            enable_end_time: Optional[pulumi.Input[str]] = None,
            enable_start_time: Optional[pulumi.Input[str]] = None,
            instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            is_enable: Optional[pulumi.Input[bool]] = None,
            metric_rule_black_list_id: Optional[pulumi.Input[str]] = None,
            metric_rule_black_list_name: Optional[pulumi.Input[str]] = None,
            metrics: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricRuleBlackListMetricArgs']]]]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            scope_type: Optional[pulumi.Input[str]] = None,
            scope_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'MetricRuleBlackList':
        """
        Get an existing MetricRuleBlackList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: Cloud service classification. For example, Redis includes kvstore_standard, kvstore_sharding, and kvstore_splitrw.
        :param pulumi.Input[str] create_time: The timestamp for creating an alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[str] effective_time: The effective time range of the alert blacklist policy.
        :param pulumi.Input[str] enable_end_time: The start timestamp of the alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[str] enable_start_time: The end timestamp of the alert blacklist policy.Unit: milliseconds.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instances: The list of instances of cloud services specified in the alert blacklist policy.
        :param pulumi.Input[bool] is_enable: The status of the alert blacklist policy. Value:-true: enabled.-false: disabled.
        :param pulumi.Input[str] metric_rule_black_list_id: The ID of the blacklist policy.
        :param pulumi.Input[str] metric_rule_black_list_name: The name of the alert blacklist policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MetricRuleBlackListMetricArgs']]]] metrics: Monitoring metrics in the instance. See `metrics` below.
        :param pulumi.Input[str] namespace: The data namespace of the cloud service.
        :param pulumi.Input[str] scope_type: The effective range of the alert blacklist policy. Value:-USER: The alert blacklist policy only takes effect in the current Alibaba cloud account.-GROUP: The alert blacklist policy takes effect in the specified application GROUP.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scope_values: Application Group ID list. The format is JSON Array.> This parameter is displayed only when 'ScopeType' is 'GROUP.
        :param pulumi.Input[str] update_time: Modify the timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MetricRuleBlackListState.__new__(_MetricRuleBlackListState)

        __props__.__dict__["category"] = category
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["effective_time"] = effective_time
        __props__.__dict__["enable_end_time"] = enable_end_time
        __props__.__dict__["enable_start_time"] = enable_start_time
        __props__.__dict__["instances"] = instances
        __props__.__dict__["is_enable"] = is_enable
        __props__.__dict__["metric_rule_black_list_id"] = metric_rule_black_list_id
        __props__.__dict__["metric_rule_black_list_name"] = metric_rule_black_list_name
        __props__.__dict__["metrics"] = metrics
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["scope_type"] = scope_type
        __props__.__dict__["scope_values"] = scope_values
        __props__.__dict__["update_time"] = update_time
        return MetricRuleBlackList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        """
        Cloud service classification. For example, Redis includes kvstore_standard, kvstore_sharding, and kvstore_splitrw.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The timestamp for creating an alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="effectiveTime")
    def effective_time(self) -> pulumi.Output[Optional[str]]:
        """
        The effective time range of the alert blacklist policy.
        """
        return pulumi.get(self, "effective_time")

    @property
    @pulumi.getter(name="enableEndTime")
    def enable_end_time(self) -> pulumi.Output[Optional[str]]:
        """
        The start timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "enable_end_time")

    @property
    @pulumi.getter(name="enableStartTime")
    def enable_start_time(self) -> pulumi.Output[Optional[str]]:
        """
        The end timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "enable_start_time")

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of instances of cloud services specified in the alert blacklist policy.
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="isEnable")
    def is_enable(self) -> pulumi.Output[bool]:
        """
        The status of the alert blacklist policy. Value:-true: enabled.-false: disabled.
        """
        return pulumi.get(self, "is_enable")

    @property
    @pulumi.getter(name="metricRuleBlackListId")
    def metric_rule_black_list_id(self) -> pulumi.Output[str]:
        """
        The ID of the blacklist policy.
        """
        return pulumi.get(self, "metric_rule_black_list_id")

    @property
    @pulumi.getter(name="metricRuleBlackListName")
    def metric_rule_black_list_name(self) -> pulumi.Output[str]:
        """
        The name of the alert blacklist policy.
        """
        return pulumi.get(self, "metric_rule_black_list_name")

    @property
    @pulumi.getter
    def metrics(self) -> pulumi.Output[Optional[Sequence['outputs.MetricRuleBlackListMetric']]]:
        """
        Monitoring metrics in the instance. See `metrics` below.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[str]:
        """
        The data namespace of the cloud service.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="scopeType")
    def scope_type(self) -> pulumi.Output[str]:
        """
        The effective range of the alert blacklist policy. Value:-USER: The alert blacklist policy only takes effect in the current Alibaba cloud account.-GROUP: The alert blacklist policy takes effect in the specified application GROUP.
        """
        return pulumi.get(self, "scope_type")

    @property
    @pulumi.getter(name="scopeValues")
    def scope_values(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Application Group ID list. The format is JSON Array.> This parameter is displayed only when 'ScopeType' is 'GROUP.
        """
        return pulumi.get(self, "scope_values")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Modify the timestamp of the alert blacklist policy.Unit: milliseconds.
        """
        return pulumi.get(self, "update_time")

