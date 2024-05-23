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
    'GetProductVersionsResult',
    'AwaitableGetProductVersionsResult',
    'get_product_versions',
    'get_product_versions_output',
]

@pulumi.output_type
class GetProductVersionsResult:
    """
    A collection of values returned by getProductVersions.
    """
    def __init__(__self__, enable_details=None, id=None, ids=None, name_regex=None, names=None, output_file=None, product_id=None, product_versions=None, versions=None):
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if product_id and not isinstance(product_id, str):
            raise TypeError("Expected argument 'product_id' to be a str")
        pulumi.set(__self__, "product_id", product_id)
        if product_versions and not isinstance(product_versions, list):
            raise TypeError("Expected argument 'product_versions' to be a list")
        pulumi.set(__self__, "product_versions", product_versions)
        if versions and not isinstance(versions, list):
            raise TypeError("Expected argument 'versions' to be a list")
        pulumi.set(__self__, "versions", versions)

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
        """
        A list of Product Version IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of name of Product Versions.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="productVersions")
    def product_versions(self) -> Sequence['outputs.GetProductVersionsProductVersionResult']:
        """
        A list of Product Version Entries. Each element contains the following attributes:
        """
        return pulumi.get(self, "product_versions")

    @property
    @pulumi.getter
    def versions(self) -> Sequence['outputs.GetProductVersionsVersionResult']:
        warnings.warn("""Field 'versions' has been deprecated from provider version 1.197.0.""", DeprecationWarning)
        pulumi.log.warn("""versions is deprecated: Field 'versions' has been deprecated from provider version 1.197.0.""")

        return pulumi.get(self, "versions")


class AwaitableGetProductVersionsResult(GetProductVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProductVersionsResult(
            enable_details=self.enable_details,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            product_id=self.product_id,
            product_versions=self.product_versions,
            versions=self.versions)


def get_product_versions(enable_details: Optional[bool] = None,
                         ids: Optional[Sequence[str]] = None,
                         name_regex: Optional[str] = None,
                         output_file: Optional[str] = None,
                         product_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProductVersionsResult:
    """
    This data source provides Service Catalog Product Version available to the user.[What is Product Version](https://www.alibabacloud.com/help/en/service-catalog/developer-reference/api-servicecatalog-2021-09-01-listproductversions)

    > **NOTE:** Available in 1.196.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.servicecatalog.get_product_versions(name_regex="1.0.0",
        product_id="prod-bp125x4k29wb7q")
    pulumi.export("alicloudServiceCatalogProductVersionExampleId", default.product_versions[0].id)
    ```


    :param Sequence[str] ids: A list of Product Version IDs.
    :param str name_regex: A regex string to filter results by Group Metric Rule name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str product_id: Product ID
    """
    __args__ = dict()
    __args__['enableDetails'] = enable_details
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['productId'] = product_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:servicecatalog/getProductVersions:getProductVersions', __args__, opts=opts, typ=GetProductVersionsResult).value

    return AwaitableGetProductVersionsResult(
        enable_details=pulumi.get(__ret__, 'enable_details'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        output_file=pulumi.get(__ret__, 'output_file'),
        product_id=pulumi.get(__ret__, 'product_id'),
        product_versions=pulumi.get(__ret__, 'product_versions'),
        versions=pulumi.get(__ret__, 'versions'))


@_utilities.lift_output_func(get_product_versions)
def get_product_versions_output(enable_details: Optional[pulumi.Input[Optional[bool]]] = None,
                                ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                product_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProductVersionsResult]:
    """
    This data source provides Service Catalog Product Version available to the user.[What is Product Version](https://www.alibabacloud.com/help/en/service-catalog/developer-reference/api-servicecatalog-2021-09-01-listproductversions)

    > **NOTE:** Available in 1.196.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.servicecatalog.get_product_versions(name_regex="1.0.0",
        product_id="prod-bp125x4k29wb7q")
    pulumi.export("alicloudServiceCatalogProductVersionExampleId", default.product_versions[0].id)
    ```


    :param Sequence[str] ids: A list of Product Version IDs.
    :param str name_regex: A regex string to filter results by Group Metric Rule name.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str product_id: Product ID
    """
    ...
