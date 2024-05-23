# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetInstanceKeywordsResult',
    'AwaitableGetInstanceKeywordsResult',
    'get_instance_keywords',
    'get_instance_keywords_output',
]

@pulumi.output_type
class GetInstanceKeywordsResult:
    """
    A collection of values returned by getInstanceKeywords.
    """
    def __init__(__self__, id=None, ids=None, key=None, keywords=None, output_file=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if keywords and not isinstance(keywords, list):
            raise TypeError("Expected argument 'keywords' to be a list")
        pulumi.set(__self__, "keywords", keywords)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)

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
        """
        A list of keywords.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def keywords(self) -> Sequence[str]:
        """
        An array that consists of reserved keywords.
        """
        return pulumi.get(self, "keywords")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")


class AwaitableGetInstanceKeywordsResult(GetInstanceKeywordsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceKeywordsResult(
            id=self.id,
            ids=self.ids,
            key=self.key,
            keywords=self.keywords,
            output_file=self.output_file)


def get_instance_keywords(key: Optional[str] = None,
                          output_file: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceKeywordsResult:
    """
    Operation to query the reserved keywords of an ApsaraDB RDS instance. The reserved keywords cannot be used for the usernames of accounts or the names of databases.

    > **NOTE:** Available in v1.196.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    resources = alicloud.ecs.get_instance_keywords(key="account",
        output_file="./classes.txt")
    pulumi.export("accountKeywords", resources.keywords[0])
    ```


    :param str key: The type of reserved keyword to query. Valid values: `account`, `database`.
    :param str output_file: File name where to save data source results (after running `pulumi up`).
    """
    __args__ = dict()
    __args__['key'] = key
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:ecs/getInstanceKeywords:getInstanceKeywords', __args__, opts=opts, typ=GetInstanceKeywordsResult).value

    return AwaitableGetInstanceKeywordsResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        key=pulumi.get(__ret__, 'key'),
        keywords=pulumi.get(__ret__, 'keywords'),
        output_file=pulumi.get(__ret__, 'output_file'))


@_utilities.lift_output_func(get_instance_keywords)
def get_instance_keywords_output(key: Optional[pulumi.Input[str]] = None,
                                 output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceKeywordsResult]:
    """
    Operation to query the reserved keywords of an ApsaraDB RDS instance. The reserved keywords cannot be used for the usernames of accounts or the names of databases.

    > **NOTE:** Available in v1.196.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    resources = alicloud.ecs.get_instance_keywords(key="account",
        output_file="./classes.txt")
    pulumi.export("accountKeywords", resources.keywords[0])
    ```


    :param str key: The type of reserved keyword to query. Valid values: `account`, `database`.
    :param str output_file: File name where to save data source results (after running `pulumi up`).
    """
    ...
