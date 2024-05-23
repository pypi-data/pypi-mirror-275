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
    'GetIpInfoResult',
    'AwaitableGetIpInfoResult',
    'get_ip_info',
    'get_ip_info_output',
]

@pulumi.output_type
class GetIpInfoResult:
    """
    A collection of values returned by getIpInfo.
    """
    def __init__(__self__, cdn_ip=None, id=None, ip=None, isp=None, isp_ename=None, region=None, region_ename=None):
        if cdn_ip and not isinstance(cdn_ip, str):
            raise TypeError("Expected argument 'cdn_ip' to be a str")
        pulumi.set(__self__, "cdn_ip", cdn_ip)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip and not isinstance(ip, str):
            raise TypeError("Expected argument 'ip' to be a str")
        pulumi.set(__self__, "ip", ip)
        if isp and not isinstance(isp, str):
            raise TypeError("Expected argument 'isp' to be a str")
        pulumi.set(__self__, "isp", isp)
        if isp_ename and not isinstance(isp_ename, str):
            raise TypeError("Expected argument 'isp_ename' to be a str")
        pulumi.set(__self__, "isp_ename", isp_ename)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if region_ename and not isinstance(region_ename, str):
            raise TypeError("Expected argument 'region_ename' to be a str")
        pulumi.set(__self__, "region_ename", region_ename)

    @property
    @pulumi.getter(name="cdnIp")
    def cdn_ip(self) -> str:
        return pulumi.get(self, "cdn_ip")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip(self) -> str:
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter
    def isp(self) -> str:
        return pulumi.get(self, "isp")

    @property
    @pulumi.getter(name="ispEname")
    def isp_ename(self) -> str:
        return pulumi.get(self, "isp_ename")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="regionEname")
    def region_ename(self) -> str:
        return pulumi.get(self, "region_ename")


class AwaitableGetIpInfoResult(GetIpInfoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpInfoResult(
            cdn_ip=self.cdn_ip,
            id=self.id,
            ip=self.ip,
            isp=self.isp,
            isp_ename=self.isp_ename,
            region=self.region,
            region_ename=self.region_ename)


def get_ip_info(ip: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpInfoResult:
    """
    This data source provides the function of verifying whether an IP is a CDN node.

    > **NOTE:** Available in v1.153.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ip_test = alicloud.cdn.get_ip_info(ip="114.114.114.114")
    ```


    :param str ip: Specify IP address.
    """
    __args__ = dict()
    __args__['ip'] = ip
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:cdn/getIpInfo:getIpInfo', __args__, opts=opts, typ=GetIpInfoResult).value

    return AwaitableGetIpInfoResult(
        cdn_ip=pulumi.get(__ret__, 'cdn_ip'),
        id=pulumi.get(__ret__, 'id'),
        ip=pulumi.get(__ret__, 'ip'),
        isp=pulumi.get(__ret__, 'isp'),
        isp_ename=pulumi.get(__ret__, 'isp_ename'),
        region=pulumi.get(__ret__, 'region'),
        region_ename=pulumi.get(__ret__, 'region_ename'))


@_utilities.lift_output_func(get_ip_info)
def get_ip_info_output(ip: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIpInfoResult]:
    """
    This data source provides the function of verifying whether an IP is a CDN node.

    > **NOTE:** Available in v1.153.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ip_test = alicloud.cdn.get_ip_info(ip="114.114.114.114")
    ```


    :param str ip: Specify IP address.
    """
    ...
