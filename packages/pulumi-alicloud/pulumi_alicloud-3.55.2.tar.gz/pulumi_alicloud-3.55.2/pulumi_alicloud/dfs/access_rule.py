# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AccessRuleArgs', 'AccessRule']

@pulumi.input_type
class AccessRuleArgs:
    def __init__(__self__, *,
                 access_group_id: pulumi.Input[str],
                 network_segment: pulumi.Input[str],
                 priority: pulumi.Input[int],
                 rw_access_type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessRule resource.
        :param pulumi.Input[str] access_group_id: Permission group resource ID. You must specify the permission group ID when creating a permission rule.
        :param pulumi.Input[str] network_segment: The IP address or network segment of the authorized object.
        :param pulumi.Input[int] priority: Permission rule priority. When the same authorization object matches multiple rules, the high-priority rule takes effect. Value range: 1~100,1 is the highest priority.
        :param pulumi.Input[str] rw_access_type: The read and write permissions of the authorized object on the file system. Value: RDWR: readable and writable RDONLY: Read only.
        :param pulumi.Input[str] description: Permission rule description.  No more than 32 characters in length.
        """
        pulumi.set(__self__, "access_group_id", access_group_id)
        pulumi.set(__self__, "network_segment", network_segment)
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "rw_access_type", rw_access_type)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> pulumi.Input[str]:
        """
        Permission group resource ID. You must specify the permission group ID when creating a permission rule.
        """
        return pulumi.get(self, "access_group_id")

    @access_group_id.setter
    def access_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_group_id", value)

    @property
    @pulumi.getter(name="networkSegment")
    def network_segment(self) -> pulumi.Input[str]:
        """
        The IP address or network segment of the authorized object.
        """
        return pulumi.get(self, "network_segment")

    @network_segment.setter
    def network_segment(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_segment", value)

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Input[int]:
        """
        Permission rule priority. When the same authorization object matches multiple rules, the high-priority rule takes effect. Value range: 1~100,1 is the highest priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="rwAccessType")
    def rw_access_type(self) -> pulumi.Input[str]:
        """
        The read and write permissions of the authorized object on the file system. Value: RDWR: readable and writable RDONLY: Read only.
        """
        return pulumi.get(self, "rw_access_type")

    @rw_access_type.setter
    def rw_access_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "rw_access_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Permission rule description.  No more than 32 characters in length.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _AccessRuleState:
    def __init__(__self__, *,
                 access_group_id: Optional[pulumi.Input[str]] = None,
                 access_rule_id: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_segment: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rw_access_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessRule resources.
        :param pulumi.Input[str] access_group_id: Permission group resource ID. You must specify the permission group ID when creating a permission rule.
        :param pulumi.Input[str] access_rule_id: The unique identity of the permission rule, which is used to retrieve the permission rule for a specific day in the permission group.
        :param pulumi.Input[str] create_time: Permission rule resource creation time.
        :param pulumi.Input[str] description: Permission rule description.  No more than 32 characters in length.
        :param pulumi.Input[str] network_segment: The IP address or network segment of the authorized object.
        :param pulumi.Input[int] priority: Permission rule priority. When the same authorization object matches multiple rules, the high-priority rule takes effect. Value range: 1~100,1 is the highest priority.
        :param pulumi.Input[str] rw_access_type: The read and write permissions of the authorized object on the file system. Value: RDWR: readable and writable RDONLY: Read only.
        """
        if access_group_id is not None:
            pulumi.set(__self__, "access_group_id", access_group_id)
        if access_rule_id is not None:
            pulumi.set(__self__, "access_rule_id", access_rule_id)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if network_segment is not None:
            pulumi.set(__self__, "network_segment", network_segment)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if rw_access_type is not None:
            pulumi.set(__self__, "rw_access_type", rw_access_type)

    @property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Permission group resource ID. You must specify the permission group ID when creating a permission rule.
        """
        return pulumi.get(self, "access_group_id")

    @access_group_id.setter
    def access_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_group_id", value)

    @property
    @pulumi.getter(name="accessRuleId")
    def access_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identity of the permission rule, which is used to retrieve the permission rule for a specific day in the permission group.
        """
        return pulumi.get(self, "access_rule_id")

    @access_rule_id.setter
    def access_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_rule_id", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Permission rule resource creation time.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Permission rule description.  No more than 32 characters in length.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="networkSegment")
    def network_segment(self) -> Optional[pulumi.Input[str]]:
        """
        The IP address or network segment of the authorized object.
        """
        return pulumi.get(self, "network_segment")

    @network_segment.setter
    def network_segment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_segment", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Permission rule priority. When the same authorization object matches multiple rules, the high-priority rule takes effect. Value range: 1~100,1 is the highest priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="rwAccessType")
    def rw_access_type(self) -> Optional[pulumi.Input[str]]:
        """
        The read and write permissions of the authorized object on the file system. Value: RDWR: readable and writable RDONLY: Read only.
        """
        return pulumi.get(self, "rw_access_type")

    @rw_access_type.setter
    def rw_access_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rw_access_type", value)


class AccessRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_group_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_segment: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rw_access_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a DFS Access Rule resource.

        For information about DFS Access Rule and how to use it, see [What is Access Rule](https://www.alibabacloud.com/help/en/aibaba-cloud-storage-services/latest/apsara-file-storage-for-hdfs).

        > **NOTE:** Available since v1.140.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "example_name"
        default = alicloud.dfs.AccessGroup("default",
            network_type="VPC",
            access_group_name=name,
            description=name)
        default_access_rule = alicloud.dfs.AccessRule("default",
            network_segment="192.0.2.0/24",
            access_group_id=default.id,
            description=name,
            rw_access_type="RDWR",
            priority=10)
        ```

        ## Import

        DFS Access Rule can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:dfs/accessRule:AccessRule example <access_group_id>:<access_rule_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_group_id: Permission group resource ID. You must specify the permission group ID when creating a permission rule.
        :param pulumi.Input[str] description: Permission rule description.  No more than 32 characters in length.
        :param pulumi.Input[str] network_segment: The IP address or network segment of the authorized object.
        :param pulumi.Input[int] priority: Permission rule priority. When the same authorization object matches multiple rules, the high-priority rule takes effect. Value range: 1~100,1 is the highest priority.
        :param pulumi.Input[str] rw_access_type: The read and write permissions of the authorized object on the file system. Value: RDWR: readable and writable RDONLY: Read only.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DFS Access Rule resource.

        For information about DFS Access Rule and how to use it, see [What is Access Rule](https://www.alibabacloud.com/help/en/aibaba-cloud-storage-services/latest/apsara-file-storage-for-hdfs).

        > **NOTE:** Available since v1.140.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "example_name"
        default = alicloud.dfs.AccessGroup("default",
            network_type="VPC",
            access_group_name=name,
            description=name)
        default_access_rule = alicloud.dfs.AccessRule("default",
            network_segment="192.0.2.0/24",
            access_group_id=default.id,
            description=name,
            rw_access_type="RDWR",
            priority=10)
        ```

        ## Import

        DFS Access Rule can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:dfs/accessRule:AccessRule example <access_group_id>:<access_rule_id>
        ```

        :param str resource_name: The name of the resource.
        :param AccessRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_group_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_segment: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rw_access_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessRuleArgs.__new__(AccessRuleArgs)

            if access_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'access_group_id'")
            __props__.__dict__["access_group_id"] = access_group_id
            __props__.__dict__["description"] = description
            if network_segment is None and not opts.urn:
                raise TypeError("Missing required property 'network_segment'")
            __props__.__dict__["network_segment"] = network_segment
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__.__dict__["priority"] = priority
            if rw_access_type is None and not opts.urn:
                raise TypeError("Missing required property 'rw_access_type'")
            __props__.__dict__["rw_access_type"] = rw_access_type
            __props__.__dict__["access_rule_id"] = None
            __props__.__dict__["create_time"] = None
        super(AccessRule, __self__).__init__(
            'alicloud:dfs/accessRule:AccessRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_group_id: Optional[pulumi.Input[str]] = None,
            access_rule_id: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            network_segment: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            rw_access_type: Optional[pulumi.Input[str]] = None) -> 'AccessRule':
        """
        Get an existing AccessRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_group_id: Permission group resource ID. You must specify the permission group ID when creating a permission rule.
        :param pulumi.Input[str] access_rule_id: The unique identity of the permission rule, which is used to retrieve the permission rule for a specific day in the permission group.
        :param pulumi.Input[str] create_time: Permission rule resource creation time.
        :param pulumi.Input[str] description: Permission rule description.  No more than 32 characters in length.
        :param pulumi.Input[str] network_segment: The IP address or network segment of the authorized object.
        :param pulumi.Input[int] priority: Permission rule priority. When the same authorization object matches multiple rules, the high-priority rule takes effect. Value range: 1~100,1 is the highest priority.
        :param pulumi.Input[str] rw_access_type: The read and write permissions of the authorized object on the file system. Value: RDWR: readable and writable RDONLY: Read only.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessRuleState.__new__(_AccessRuleState)

        __props__.__dict__["access_group_id"] = access_group_id
        __props__.__dict__["access_rule_id"] = access_rule_id
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["network_segment"] = network_segment
        __props__.__dict__["priority"] = priority
        __props__.__dict__["rw_access_type"] = rw_access_type
        return AccessRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessGroupId")
    def access_group_id(self) -> pulumi.Output[str]:
        """
        Permission group resource ID. You must specify the permission group ID when creating a permission rule.
        """
        return pulumi.get(self, "access_group_id")

    @property
    @pulumi.getter(name="accessRuleId")
    def access_rule_id(self) -> pulumi.Output[str]:
        """
        The unique identity of the permission rule, which is used to retrieve the permission rule for a specific day in the permission group.
        """
        return pulumi.get(self, "access_rule_id")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Permission rule resource creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Permission rule description.  No more than 32 characters in length.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="networkSegment")
    def network_segment(self) -> pulumi.Output[str]:
        """
        The IP address or network segment of the authorized object.
        """
        return pulumi.get(self, "network_segment")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Permission rule priority. When the same authorization object matches multiple rules, the high-priority rule takes effect. Value range: 1~100,1 is the highest priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="rwAccessType")
    def rw_access_type(self) -> pulumi.Output[str]:
        """
        The read and write permissions of the authorized object on the file system. Value: RDWR: readable and writable RDONLY: Read only.
        """
        return pulumi.get(self, "rw_access_type")

