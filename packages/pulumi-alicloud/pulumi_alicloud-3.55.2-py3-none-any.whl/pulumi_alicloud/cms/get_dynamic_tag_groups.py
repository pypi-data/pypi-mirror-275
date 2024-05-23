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

__all__ = [
    'GetDynamicTagGroupsResult',
    'AwaitableGetDynamicTagGroupsResult',
    'get_dynamic_tag_groups',
    'get_dynamic_tag_groups_output',
]

@pulumi.output_type
class GetDynamicTagGroupsResult:
    """
    A collection of values returned by getDynamicTagGroups.
    """
    def __init__(__self__, groups=None, id=None, ids=None, output_file=None, status=None, tag_key=None):
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tag_key and not isinstance(tag_key, str):
            raise TypeError("Expected argument 'tag_key' to be a str")
        pulumi.set(__self__, "tag_key", tag_key)

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GetDynamicTagGroupsGroupResult']:
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> Optional[str]:
        return pulumi.get(self, "tag_key")


class AwaitableGetDynamicTagGroupsResult(GetDynamicTagGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDynamicTagGroupsResult(
            groups=self.groups,
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            status=self.status,
            tag_key=self.tag_key)


def get_dynamic_tag_groups(ids: Optional[Sequence[str]] = None,
                           output_file: Optional[str] = None,
                           status: Optional[str] = None,
                           tag_key: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDynamicTagGroupsResult:
    """
    This data source provides the Cms Dynamic Tag Groups of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.142.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    config = pulumi.Config()
    name = config.get("name")
    if name is None:
        name = "example_value"
    default = alicloud.cms.AlarmContactGroup("default",
        alarm_contact_group_name=name,
        describe="example_value",
        enable_subscribed=True)
    default_dynamic_tag_group = alicloud.cms.DynamicTagGroup("default",
        contact_group_lists=[default.id],
        tag_key="your_tag_key",
        match_expresses=[alicloud.cms.DynamicTagGroupMatchExpressArgs(
            tag_value="your_tag_value",
            tag_value_match_function="all",
        )])
    ids = alicloud.cms.get_dynamic_tag_groups_output(ids=[default_dynamic_tag_group.id])
    pulumi.export("cmsDynamicTagGroupId1", ids.groups[0].id)
    ```


    :param Sequence[str] ids: A list of Dynamic Tag Group IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the resource. Valid values: `RUNNING`, `FINISH`.
    :param str tag_key: The tag key of the tag.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['status'] = status
    __args__['tagKey'] = tag_key
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:cms/getDynamicTagGroups:getDynamicTagGroups', __args__, opts=opts, typ=GetDynamicTagGroupsResult).value

    return AwaitableGetDynamicTagGroupsResult(
        groups=pulumi.get(__ret__, 'groups'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        output_file=pulumi.get(__ret__, 'output_file'),
        status=pulumi.get(__ret__, 'status'),
        tag_key=pulumi.get(__ret__, 'tag_key'))


@_utilities.lift_output_func(get_dynamic_tag_groups)
def get_dynamic_tag_groups_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                  output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                  status: Optional[pulumi.Input[Optional[str]]] = None,
                                  tag_key: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDynamicTagGroupsResult]:
    """
    This data source provides the Cms Dynamic Tag Groups of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.142.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    config = pulumi.Config()
    name = config.get("name")
    if name is None:
        name = "example_value"
    default = alicloud.cms.AlarmContactGroup("default",
        alarm_contact_group_name=name,
        describe="example_value",
        enable_subscribed=True)
    default_dynamic_tag_group = alicloud.cms.DynamicTagGroup("default",
        contact_group_lists=[default.id],
        tag_key="your_tag_key",
        match_expresses=[alicloud.cms.DynamicTagGroupMatchExpressArgs(
            tag_value="your_tag_value",
            tag_value_match_function="all",
        )])
    ids = alicloud.cms.get_dynamic_tag_groups_output(ids=[default_dynamic_tag_group.id])
    pulumi.export("cmsDynamicTagGroupId1", ids.groups[0].id)
    ```


    :param Sequence[str] ids: A list of Dynamic Tag Group IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of the resource. Valid values: `RUNNING`, `FINISH`.
    :param str tag_key: The tag key of the tag.
    """
    ...
