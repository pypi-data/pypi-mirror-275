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

__all__ = ['PrefixListArgs', 'PrefixList']

@pulumi.input_type
class PrefixListArgs:
    def __init__(__self__, *,
                 entrys: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 max_entries: Optional[pulumi.Input[int]] = None,
                 prefix_list_description: Optional[pulumi.Input[str]] = None,
                 prefix_list_name: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a PrefixList resource.
        :param pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]] entrys: The CIDR address block list of the prefix list.See the following `Block Entrys`.
        :param pulumi.Input[str] ip_version: The IP version of the prefix list. Value:-**IPV4**:IPv4 version.-**IPV6**:IPv6 version.
        :param pulumi.Input[int] max_entries: The maximum number of entries for CIDR address blocks in the prefix list.
        :param pulumi.Input[str] prefix_list_description: The description of the prefix list.It must be 2 to 256 characters in length and must start with a letter or Chinese, but cannot start with `http://` or `https://`.
        :param pulumi.Input[str] prefix_list_name: The name of the prefix list. The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, periods (.), underscores (_), and hyphens (-).
        :param pulumi.Input[str] resource_group_id: The ID of the resource group to which the PrefixList belongs.
        :param pulumi.Input[Mapping[str, Any]] tags: The tags of PrefixList.
        """
        if entrys is not None:
            pulumi.set(__self__, "entrys", entrys)
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)
        if max_entries is not None:
            pulumi.set(__self__, "max_entries", max_entries)
        if prefix_list_description is not None:
            pulumi.set(__self__, "prefix_list_description", prefix_list_description)
        if prefix_list_name is not None:
            pulumi.set(__self__, "prefix_list_name", prefix_list_name)
        if resource_group_id is not None:
            pulumi.set(__self__, "resource_group_id", resource_group_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def entrys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]]:
        """
        The CIDR address block list of the prefix list.See the following `Block Entrys`.
        """
        return pulumi.get(self, "entrys")

    @entrys.setter
    def entrys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]]):
        pulumi.set(self, "entrys", value)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[str]]:
        """
        The IP version of the prefix list. Value:-**IPV4**:IPv4 version.-**IPV6**:IPv6 version.
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_version", value)

    @property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of entries for CIDR address blocks in the prefix list.
        """
        return pulumi.get(self, "max_entries")

    @max_entries.setter
    def max_entries(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_entries", value)

    @property
    @pulumi.getter(name="prefixListDescription")
    def prefix_list_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the prefix list.It must be 2 to 256 characters in length and must start with a letter or Chinese, but cannot start with `http://` or `https://`.
        """
        return pulumi.get(self, "prefix_list_description")

    @prefix_list_description.setter
    def prefix_list_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix_list_description", value)

    @property
    @pulumi.getter(name="prefixListName")
    def prefix_list_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the prefix list. The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, periods (.), underscores (_), and hyphens (-).
        """
        return pulumi.get(self, "prefix_list_name")

    @prefix_list_name.setter
    def prefix_list_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix_list_name", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the resource group to which the PrefixList belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The tags of PrefixList.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _PrefixListState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 entrys: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 max_entries: Optional[pulumi.Input[int]] = None,
                 prefix_list_associations: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListPrefixListAssociationArgs']]]] = None,
                 prefix_list_description: Optional[pulumi.Input[str]] = None,
                 prefix_list_id: Optional[pulumi.Input[str]] = None,
                 prefix_list_name: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 share_type: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering PrefixList resources.
        :param pulumi.Input[str] create_time: The time when the prefix list was created.
        :param pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]] entrys: The CIDR address block list of the prefix list.See the following `Block Entrys`.
        :param pulumi.Input[str] ip_version: The IP version of the prefix list. Value:-**IPV4**:IPv4 version.-**IPV6**:IPv6 version.
        :param pulumi.Input[int] max_entries: The maximum number of entries for CIDR address blocks in the prefix list.
        :param pulumi.Input[Sequence[pulumi.Input['PrefixListPrefixListAssociationArgs']]] prefix_list_associations: The association list information of the prefix list.
        :param pulumi.Input[str] prefix_list_description: The description of the prefix list.It must be 2 to 256 characters in length and must start with a letter or Chinese, but cannot start with `http://` or `https://`.
        :param pulumi.Input[str] prefix_list_id: The ID of the query Prefix List.
        :param pulumi.Input[str] prefix_list_name: The name of the prefix list. The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, periods (.), underscores (_), and hyphens (-).
        :param pulumi.Input[str] resource_group_id: The ID of the resource group to which the PrefixList belongs.
        :param pulumi.Input[str] share_type: The share type of the prefix list. Value:-**Shared**: indicates that the prefix list is a Shared prefix list.-Null: indicates that the prefix list is not a shared prefix list.
        :param pulumi.Input[str] status: Resource attribute fields that represent the status of the resource.
        :param pulumi.Input[Mapping[str, Any]] tags: The tags of PrefixList.
        """
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if entrys is not None:
            pulumi.set(__self__, "entrys", entrys)
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)
        if max_entries is not None:
            pulumi.set(__self__, "max_entries", max_entries)
        if prefix_list_associations is not None:
            pulumi.set(__self__, "prefix_list_associations", prefix_list_associations)
        if prefix_list_description is not None:
            pulumi.set(__self__, "prefix_list_description", prefix_list_description)
        if prefix_list_id is not None:
            pulumi.set(__self__, "prefix_list_id", prefix_list_id)
        if prefix_list_name is not None:
            pulumi.set(__self__, "prefix_list_name", prefix_list_name)
        if resource_group_id is not None:
            pulumi.set(__self__, "resource_group_id", resource_group_id)
        if share_type is not None:
            pulumi.set(__self__, "share_type", share_type)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the prefix list was created.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def entrys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]]:
        """
        The CIDR address block list of the prefix list.See the following `Block Entrys`.
        """
        return pulumi.get(self, "entrys")

    @entrys.setter
    def entrys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]]):
        pulumi.set(self, "entrys", value)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[str]]:
        """
        The IP version of the prefix list. Value:-**IPV4**:IPv4 version.-**IPV6**:IPv6 version.
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_version", value)

    @property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of entries for CIDR address blocks in the prefix list.
        """
        return pulumi.get(self, "max_entries")

    @max_entries.setter
    def max_entries(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_entries", value)

    @property
    @pulumi.getter(name="prefixListAssociations")
    def prefix_list_associations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListPrefixListAssociationArgs']]]]:
        """
        The association list information of the prefix list.
        """
        return pulumi.get(self, "prefix_list_associations")

    @prefix_list_associations.setter
    def prefix_list_associations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListPrefixListAssociationArgs']]]]):
        pulumi.set(self, "prefix_list_associations", value)

    @property
    @pulumi.getter(name="prefixListDescription")
    def prefix_list_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the prefix list.It must be 2 to 256 characters in length and must start with a letter or Chinese, but cannot start with `http://` or `https://`.
        """
        return pulumi.get(self, "prefix_list_description")

    @prefix_list_description.setter
    def prefix_list_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix_list_description", value)

    @property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the query Prefix List.
        """
        return pulumi.get(self, "prefix_list_id")

    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix_list_id", value)

    @property
    @pulumi.getter(name="prefixListName")
    def prefix_list_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the prefix list. The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, periods (.), underscores (_), and hyphens (-).
        """
        return pulumi.get(self, "prefix_list_name")

    @prefix_list_name.setter
    def prefix_list_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix_list_name", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the resource group to which the PrefixList belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter(name="shareType")
    def share_type(self) -> Optional[pulumi.Input[str]]:
        """
        The share type of the prefix list. Value:-**Shared**: indicates that the prefix list is a Shared prefix list.-Null: indicates that the prefix list is not a shared prefix list.
        """
        return pulumi.get(self, "share_type")

    @share_type.setter
    def share_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "share_type", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Resource attribute fields that represent the status of the resource.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The tags of PrefixList.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


class PrefixList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 entrys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListEntryArgs']]]]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 max_entries: Optional[pulumi.Input[int]] = None,
                 prefix_list_description: Optional[pulumi.Input[str]] = None,
                 prefix_list_name: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        """
        Provides a Vpc Prefix List resource. This resource is used to create a prefix list.

        For information about Vpc Prefix List and how to use it, see [What is Prefix List](https://www.alibabacloud.com/help/zh/virtual-private-cloud/latest/creatvpcprefixlist).

        > **NOTE:** Available in v1.182.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-testacc-example"
        default_rg = alicloud.resourcemanager.ResourceGroup("defaultRg",
            display_name="tf-testacc-chenyi",
            resource_group_name=name)
        change_rg = alicloud.resourcemanager.ResourceGroup("changeRg",
            display_name="tf-testacc-chenyi-change",
            resource_group_name=f"{name}1")
        default = alicloud.vpc.PrefixList("default",
            max_entries=50,
            resource_group_id=default_rg.id,
            prefix_list_description="test",
            ip_version="IPV4",
            prefix_list_name=name,
            entrys=[alicloud.vpc.PrefixListEntryArgs(
                cidr="192.168.0.0/16",
                description="test",
            )])
        ```

        ## Import

        Vpc Prefix List can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:vpc/prefixList:PrefixList example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListEntryArgs']]]] entrys: The CIDR address block list of the prefix list.See the following `Block Entrys`.
        :param pulumi.Input[str] ip_version: The IP version of the prefix list. Value:-**IPV4**:IPv4 version.-**IPV6**:IPv6 version.
        :param pulumi.Input[int] max_entries: The maximum number of entries for CIDR address blocks in the prefix list.
        :param pulumi.Input[str] prefix_list_description: The description of the prefix list.It must be 2 to 256 characters in length and must start with a letter or Chinese, but cannot start with `http://` or `https://`.
        :param pulumi.Input[str] prefix_list_name: The name of the prefix list. The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, periods (.), underscores (_), and hyphens (-).
        :param pulumi.Input[str] resource_group_id: The ID of the resource group to which the PrefixList belongs.
        :param pulumi.Input[Mapping[str, Any]] tags: The tags of PrefixList.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PrefixListArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Vpc Prefix List resource. This resource is used to create a prefix list.

        For information about Vpc Prefix List and how to use it, see [What is Prefix List](https://www.alibabacloud.com/help/zh/virtual-private-cloud/latest/creatvpcprefixlist).

        > **NOTE:** Available in v1.182.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-testacc-example"
        default_rg = alicloud.resourcemanager.ResourceGroup("defaultRg",
            display_name="tf-testacc-chenyi",
            resource_group_name=name)
        change_rg = alicloud.resourcemanager.ResourceGroup("changeRg",
            display_name="tf-testacc-chenyi-change",
            resource_group_name=f"{name}1")
        default = alicloud.vpc.PrefixList("default",
            max_entries=50,
            resource_group_id=default_rg.id,
            prefix_list_description="test",
            ip_version="IPV4",
            prefix_list_name=name,
            entrys=[alicloud.vpc.PrefixListEntryArgs(
                cidr="192.168.0.0/16",
                description="test",
            )])
        ```

        ## Import

        Vpc Prefix List can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:vpc/prefixList:PrefixList example <id>
        ```

        :param str resource_name: The name of the resource.
        :param PrefixListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrefixListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 entrys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListEntryArgs']]]]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 max_entries: Optional[pulumi.Input[int]] = None,
                 prefix_list_description: Optional[pulumi.Input[str]] = None,
                 prefix_list_name: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrefixListArgs.__new__(PrefixListArgs)

            __props__.__dict__["entrys"] = entrys
            __props__.__dict__["ip_version"] = ip_version
            __props__.__dict__["max_entries"] = max_entries
            __props__.__dict__["prefix_list_description"] = prefix_list_description
            __props__.__dict__["prefix_list_name"] = prefix_list_name
            __props__.__dict__["resource_group_id"] = resource_group_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["create_time"] = None
            __props__.__dict__["prefix_list_associations"] = None
            __props__.__dict__["prefix_list_id"] = None
            __props__.__dict__["share_type"] = None
            __props__.__dict__["status"] = None
        super(PrefixList, __self__).__init__(
            'alicloud:vpc/prefixList:PrefixList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            entrys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListEntryArgs']]]]] = None,
            ip_version: Optional[pulumi.Input[str]] = None,
            max_entries: Optional[pulumi.Input[int]] = None,
            prefix_list_associations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListPrefixListAssociationArgs']]]]] = None,
            prefix_list_description: Optional[pulumi.Input[str]] = None,
            prefix_list_id: Optional[pulumi.Input[str]] = None,
            prefix_list_name: Optional[pulumi.Input[str]] = None,
            resource_group_id: Optional[pulumi.Input[str]] = None,
            share_type: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'PrefixList':
        """
        Get an existing PrefixList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The time when the prefix list was created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListEntryArgs']]]] entrys: The CIDR address block list of the prefix list.See the following `Block Entrys`.
        :param pulumi.Input[str] ip_version: The IP version of the prefix list. Value:-**IPV4**:IPv4 version.-**IPV6**:IPv6 version.
        :param pulumi.Input[int] max_entries: The maximum number of entries for CIDR address blocks in the prefix list.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListPrefixListAssociationArgs']]]] prefix_list_associations: The association list information of the prefix list.
        :param pulumi.Input[str] prefix_list_description: The description of the prefix list.It must be 2 to 256 characters in length and must start with a letter or Chinese, but cannot start with `http://` or `https://`.
        :param pulumi.Input[str] prefix_list_id: The ID of the query Prefix List.
        :param pulumi.Input[str] prefix_list_name: The name of the prefix list. The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, periods (.), underscores (_), and hyphens (-).
        :param pulumi.Input[str] resource_group_id: The ID of the resource group to which the PrefixList belongs.
        :param pulumi.Input[str] share_type: The share type of the prefix list. Value:-**Shared**: indicates that the prefix list is a Shared prefix list.-Null: indicates that the prefix list is not a shared prefix list.
        :param pulumi.Input[str] status: Resource attribute fields that represent the status of the resource.
        :param pulumi.Input[Mapping[str, Any]] tags: The tags of PrefixList.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PrefixListState.__new__(_PrefixListState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["entrys"] = entrys
        __props__.__dict__["ip_version"] = ip_version
        __props__.__dict__["max_entries"] = max_entries
        __props__.__dict__["prefix_list_associations"] = prefix_list_associations
        __props__.__dict__["prefix_list_description"] = prefix_list_description
        __props__.__dict__["prefix_list_id"] = prefix_list_id
        __props__.__dict__["prefix_list_name"] = prefix_list_name
        __props__.__dict__["resource_group_id"] = resource_group_id
        __props__.__dict__["share_type"] = share_type
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        return PrefixList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time when the prefix list was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def entrys(self) -> pulumi.Output[Optional[Sequence['outputs.PrefixListEntry']]]:
        """
        The CIDR address block list of the prefix list.See the following `Block Entrys`.
        """
        return pulumi.get(self, "entrys")

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> pulumi.Output[str]:
        """
        The IP version of the prefix list. Value:-**IPV4**:IPv4 version.-**IPV6**:IPv6 version.
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> pulumi.Output[int]:
        """
        The maximum number of entries for CIDR address blocks in the prefix list.
        """
        return pulumi.get(self, "max_entries")

    @property
    @pulumi.getter(name="prefixListAssociations")
    def prefix_list_associations(self) -> pulumi.Output[Sequence['outputs.PrefixListPrefixListAssociation']]:
        """
        The association list information of the prefix list.
        """
        return pulumi.get(self, "prefix_list_associations")

    @property
    @pulumi.getter(name="prefixListDescription")
    def prefix_list_description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the prefix list.It must be 2 to 256 characters in length and must start with a letter or Chinese, but cannot start with `http://` or `https://`.
        """
        return pulumi.get(self, "prefix_list_description")

    @property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> pulumi.Output[str]:
        """
        The ID of the query Prefix List.
        """
        return pulumi.get(self, "prefix_list_id")

    @property
    @pulumi.getter(name="prefixListName")
    def prefix_list_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the prefix list. The name must be 2 to 128 characters in length, and must start with a letter. It can contain digits, periods (.), underscores (_), and hyphens (-).
        """
        return pulumi.get(self, "prefix_list_name")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the resource group to which the PrefixList belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter(name="shareType")
    def share_type(self) -> pulumi.Output[str]:
        """
        The share type of the prefix list. Value:-**Shared**: indicates that the prefix list is a Shared prefix list.-Null: indicates that the prefix list is not a shared prefix list.
        """
        return pulumi.get(self, "share_type")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Resource attribute fields that represent the status of the resource.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        The tags of PrefixList.
        """
        return pulumi.get(self, "tags")

