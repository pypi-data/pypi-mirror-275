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

__all__ = [
    'GetApplicationInfosResult',
    'AwaitableGetApplicationInfosResult',
    'get_application_infos',
    'get_application_infos_output',
]

@pulumi.output_type
class GetApplicationInfosResult:
    """
    A collection of values returned by getApplicationInfos.
    """
    def __init__(__self__, applications=None, dimensions=None, enable_details=None, id=None, ids=None, key_word=None, output_file=None, product_code=None, quota_action_code=None, quota_category=None, status=None):
        if applications and not isinstance(applications, list):
            raise TypeError("Expected argument 'applications' to be a list")
        pulumi.set(__self__, "applications", applications)
        if dimensions and not isinstance(dimensions, list):
            raise TypeError("Expected argument 'dimensions' to be a list")
        pulumi.set(__self__, "dimensions", dimensions)
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if key_word and not isinstance(key_word, str):
            raise TypeError("Expected argument 'key_word' to be a str")
        pulumi.set(__self__, "key_word", key_word)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if product_code and not isinstance(product_code, str):
            raise TypeError("Expected argument 'product_code' to be a str")
        pulumi.set(__self__, "product_code", product_code)
        if quota_action_code and not isinstance(quota_action_code, str):
            raise TypeError("Expected argument 'quota_action_code' to be a str")
        pulumi.set(__self__, "quota_action_code", quota_action_code)
        if quota_category and not isinstance(quota_category, str):
            raise TypeError("Expected argument 'quota_category' to be a str")
        pulumi.set(__self__, "quota_category", quota_category)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def applications(self) -> Sequence['outputs.GetApplicationInfosApplicationResult']:
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence['outputs.GetApplicationInfosDimensionResult']]:
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        return pulumi.get(self, "enable_details")

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
    @pulumi.getter(name="keyWord")
    def key_word(self) -> Optional[str]:
        return pulumi.get(self, "key_word")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="productCode")
    def product_code(self) -> str:
        return pulumi.get(self, "product_code")

    @property
    @pulumi.getter(name="quotaActionCode")
    def quota_action_code(self) -> Optional[str]:
        return pulumi.get(self, "quota_action_code")

    @property
    @pulumi.getter(name="quotaCategory")
    def quota_category(self) -> Optional[str]:
        return pulumi.get(self, "quota_category")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


class AwaitableGetApplicationInfosResult(GetApplicationInfosResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationInfosResult(
            applications=self.applications,
            dimensions=self.dimensions,
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            key_word=self.key_word,
            output_file=self.output_file,
            product_code=self.product_code,
            quota_action_code=self.quota_action_code,
            quota_category=self.quota_category,
            status=self.status)


def get_application_infos(dimensions: Optional[Sequence[pulumi.InputType['GetApplicationInfosDimensionArgs']]] = None,
                          enable_details: Optional[bool] = None,
                          ids: Optional[Sequence[str]] = None,
                          key_word: Optional[str] = None,
                          output_file: Optional[str] = None,
                          product_code: Optional[str] = None,
                          quota_action_code: Optional[str] = None,
                          quota_category: Optional[str] = None,
                          status: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationInfosResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['dimensions'] = dimensions
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['keyWord'] = key_word
    __args__['outputFile'] = output_file
    __args__['productCode'] = product_code
    __args__['quotaActionCode'] = quota_action_code
    __args__['quotaCategory'] = quota_category
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:quotas/getApplicationInfos:getApplicationInfos', __args__, opts=opts, typ=GetApplicationInfosResult).value

    return AwaitableGetApplicationInfosResult(
        applications=pulumi.get(__ret__, 'applications'),
        dimensions=pulumi.get(__ret__, 'dimensions'),
        enable_details=pulumi.get(__ret__, 'enable_details'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        key_word=pulumi.get(__ret__, 'key_word'),
        output_file=pulumi.get(__ret__, 'output_file'),
        product_code=pulumi.get(__ret__, 'product_code'),
        quota_action_code=pulumi.get(__ret__, 'quota_action_code'),
        quota_category=pulumi.get(__ret__, 'quota_category'),
        status=pulumi.get(__ret__, 'status'))


@_utilities.lift_output_func(get_application_infos)
def get_application_infos_output(dimensions: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetApplicationInfosDimensionArgs']]]]] = None,
                                 enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                                 ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                 key_word: Optional[pulumi.Input[Optional[str]]] = None,
                                 output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                 product_code: Optional[pulumi.Input[str]] = None,
                                 quota_action_code: Optional[pulumi.Input[Optional[str]]] = None,
                                 quota_category: Optional[pulumi.Input[Optional[str]]] = None,
                                 status: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationInfosResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
