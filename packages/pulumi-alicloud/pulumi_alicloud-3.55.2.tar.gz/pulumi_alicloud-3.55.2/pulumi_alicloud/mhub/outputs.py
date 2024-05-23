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
    'GetAppsAppResult',
    'GetProductsProductResult',
]

@pulumi.output_type
class GetAppsAppResult(dict):
    def __init__(__self__, *,
                 app_key: str,
                 app_name: str,
                 bundle_id: str,
                 create_time: str,
                 encoded_icon: str,
                 id: str,
                 industry_id: str,
                 package_name: str,
                 product_id: str,
                 type: str):
        """
        :param str app_key: Application AppKey, which uniquely identifies an application when requested by the interface
        :param str app_name: The Name of the App.
        :param str bundle_id: iOS application ID. Required when creating an iOS app. **NOTE:** Either `bundle_id` or `package_name` must be set.
        :param str create_time: The CreateTime of the App.
        :param str encoded_icon: Base64 string of picture.
        :param str id: The ID of the App.
        :param str industry_id: The Industry ID of the app. For information about Industry and how to use it, MHUB[Industry](https://help.aliyun.com/document_detail/201638.html).
        :param str package_name: Android App package name.  **NOTE:** Either `bundle_id` or `package_name` must be set.
        :param str product_id: The ID of the Product.
        :param str type: The type of the App. Valid values: `Android` and `iOS`.
        """
        pulumi.set(__self__, "app_key", app_key)
        pulumi.set(__self__, "app_name", app_name)
        pulumi.set(__self__, "bundle_id", bundle_id)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "encoded_icon", encoded_icon)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "industry_id", industry_id)
        pulumi.set(__self__, "package_name", package_name)
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="appKey")
    def app_key(self) -> str:
        """
        Application AppKey, which uniquely identifies an application when requested by the interface
        """
        return pulumi.get(self, "app_key")

    @property
    @pulumi.getter(name="appName")
    def app_name(self) -> str:
        """
        The Name of the App.
        """
        return pulumi.get(self, "app_name")

    @property
    @pulumi.getter(name="bundleId")
    def bundle_id(self) -> str:
        """
        iOS application ID. Required when creating an iOS app. **NOTE:** Either `bundle_id` or `package_name` must be set.
        """
        return pulumi.get(self, "bundle_id")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The CreateTime of the App.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="encodedIcon")
    def encoded_icon(self) -> str:
        """
        Base64 string of picture.
        """
        return pulumi.get(self, "encoded_icon")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the App.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="industryId")
    def industry_id(self) -> str:
        """
        The Industry ID of the app. For information about Industry and how to use it, MHUB[Industry](https://help.aliyun.com/document_detail/201638.html).
        """
        return pulumi.get(self, "industry_id")

    @property
    @pulumi.getter(name="packageName")
    def package_name(self) -> str:
        """
        Android App package name.  **NOTE:** Either `bundle_id` or `package_name` must be set.
        """
        return pulumi.get(self, "package_name")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the App. Valid values: `Android` and `iOS`.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetProductsProductResult(dict):
    def __init__(__self__, *,
                 id: str,
                 product_id: str,
                 product_name: str):
        """
        :param str id: The ID of the Product.
        :param str product_id: The ID of the Product.
        :param str product_name: The name of the Product.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "product_name", product_name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        """
        The ID of the Product.
        """
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> str:
        """
        The name of the Product.
        """
        return pulumi.get(self, "product_name")


