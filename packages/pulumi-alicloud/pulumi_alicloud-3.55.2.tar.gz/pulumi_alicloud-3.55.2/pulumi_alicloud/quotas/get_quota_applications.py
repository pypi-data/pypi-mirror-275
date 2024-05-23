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
    'GetQuotaApplicationsResult',
    'AwaitableGetQuotaApplicationsResult',
    'get_quota_applications',
    'get_quota_applications_output',
]

@pulumi.output_type
class GetQuotaApplicationsResult:
    """
    A collection of values returned by getQuotaApplications.
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
    def applications(self) -> Sequence['outputs.GetQuotaApplicationsApplicationResult']:
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence['outputs.GetQuotaApplicationsDimensionResult']]:
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


class AwaitableGetQuotaApplicationsResult(GetQuotaApplicationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQuotaApplicationsResult(
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


def get_quota_applications(dimensions: Optional[Sequence[pulumi.InputType['GetQuotaApplicationsDimensionArgs']]] = None,
                           enable_details: Optional[bool] = None,
                           ids: Optional[Sequence[str]] = None,
                           key_word: Optional[str] = None,
                           output_file: Optional[str] = None,
                           product_code: Optional[str] = None,
                           quota_action_code: Optional[str] = None,
                           quota_category: Optional[str] = None,
                           status: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQuotaApplicationsResult:
    """
    This data source provides the Quotas Quota Applications of the current Alibaba Cloud user.

    > **NOTE:** Available since v1.117.0.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default_quota_application = alicloud.quotas.QuotaApplication("default",
        product_code="vpc",
        notice_type=3,
        effective_time="2023-05-22T16:00:00Z",
        expire_time="2024-09-15T00:08:32Z",
        desire_value=1,
        reason="",
        quota_action_code="vpc_whitelist/ha_vip_whitelist",
        audit_mode="Sync",
        env_language="zh",
        quota_category="WhiteListLabel")
    default = pulumi.Output.all(default_quota_application.quota_category, default_quota_application.id).apply(lambda quota_category, id: alicloud.quotas.get_quota_applications_output(product_code="vpc",
        enable_details=True,
        quota_category=quota_category,
        ids=[id]))
    ```


    :param Sequence[pulumi.InputType['GetQuotaApplicationsDimensionArgs']] dimensions: The quota dimensions.
    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Application Info IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str product_code: The product code.
    :param str quota_action_code: The ID of quota action.
    :param str quota_category: The quota category. Valid values: `CommonQuota`, `FlowControl`, `WhiteListLabel`.
    :param str status: The status of the quota application. Valid Values: `Agree`, `Disagree` and `Process`.
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
    __ret__ = pulumi.runtime.invoke('alicloud:quotas/getQuotaApplications:getQuotaApplications', __args__, opts=opts, typ=GetQuotaApplicationsResult).value

    return AwaitableGetQuotaApplicationsResult(
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


@_utilities.lift_output_func(get_quota_applications)
def get_quota_applications_output(dimensions: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetQuotaApplicationsDimensionArgs']]]]] = None,
                                  enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                                  ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                  key_word: Optional[pulumi.Input[Optional[str]]] = None,
                                  output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                  product_code: Optional[pulumi.Input[str]] = None,
                                  quota_action_code: Optional[pulumi.Input[Optional[str]]] = None,
                                  quota_category: Optional[pulumi.Input[Optional[str]]] = None,
                                  status: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQuotaApplicationsResult]:
    """
    This data source provides the Quotas Quota Applications of the current Alibaba Cloud user.

    > **NOTE:** Available since v1.117.0.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default_quota_application = alicloud.quotas.QuotaApplication("default",
        product_code="vpc",
        notice_type=3,
        effective_time="2023-05-22T16:00:00Z",
        expire_time="2024-09-15T00:08:32Z",
        desire_value=1,
        reason="",
        quota_action_code="vpc_whitelist/ha_vip_whitelist",
        audit_mode="Sync",
        env_language="zh",
        quota_category="WhiteListLabel")
    default = pulumi.Output.all(default_quota_application.quota_category, default_quota_application.id).apply(lambda quota_category, id: alicloud.quotas.get_quota_applications_output(product_code="vpc",
        enable_details=True,
        quota_category=quota_category,
        ids=[id]))
    ```


    :param Sequence[pulumi.InputType['GetQuotaApplicationsDimensionArgs']] dimensions: The quota dimensions.
    :param bool enable_details: Default to `false`. Set it to `true` can output more details about resource attributes.
    :param Sequence[str] ids: A list of Application Info IDs.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str product_code: The product code.
    :param str quota_action_code: The ID of quota action.
    :param str quota_category: The quota category. Valid values: `CommonQuota`, `FlowControl`, `WhiteListLabel`.
    :param str status: The status of the quota application. Valid Values: `Agree`, `Disagree` and `Process`.
    """
    ...
