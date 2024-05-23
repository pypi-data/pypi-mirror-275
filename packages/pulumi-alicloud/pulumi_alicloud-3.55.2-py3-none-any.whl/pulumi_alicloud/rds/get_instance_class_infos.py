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
    'GetInstanceClassInfosResult',
    'AwaitableGetInstanceClassInfosResult',
    'get_instance_class_infos',
    'get_instance_class_infos_output',
]

@pulumi.output_type
class GetInstanceClassInfosResult:
    """
    A collection of values returned by getInstanceClassInfos.
    """
    def __init__(__self__, commodity_code=None, db_instance_id=None, id=None, ids=None, infos=None, order_type=None, output_file=None):
        if commodity_code and not isinstance(commodity_code, str):
            raise TypeError("Expected argument 'commodity_code' to be a str")
        pulumi.set(__self__, "commodity_code", commodity_code)
        if db_instance_id and not isinstance(db_instance_id, str):
            raise TypeError("Expected argument 'db_instance_id' to be a str")
        pulumi.set(__self__, "db_instance_id", db_instance_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if infos and not isinstance(infos, list):
            raise TypeError("Expected argument 'infos' to be a list")
        pulumi.set(__self__, "infos", infos)
        if order_type and not isinstance(order_type, str):
            raise TypeError("Expected argument 'order_type' to be a str")
        pulumi.set(__self__, "order_type", order_type)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)

    @property
    @pulumi.getter(name="commodityCode")
    def commodity_code(self) -> str:
        return pulumi.get(self, "commodity_code")

    @property
    @pulumi.getter(name="dbInstanceId")
    def db_instance_id(self) -> Optional[str]:
        return pulumi.get(self, "db_instance_id")

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
        A list of Rds instance class codes.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def infos(self) -> Optional[Sequence['outputs.GetInstanceClassInfosInfoResult']]:
        """
        A list of Rds available resource. Each element contains the following attributes:
        """
        return pulumi.get(self, "infos")

    @property
    @pulumi.getter(name="orderType")
    def order_type(self) -> str:
        return pulumi.get(self, "order_type")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")


class AwaitableGetInstanceClassInfosResult(GetInstanceClassInfosResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceClassInfosResult(
            commodity_code=self.commodity_code,
            db_instance_id=self.db_instance_id,
            id=self.id,
            ids=self.ids,
            infos=self.infos,
            order_type=self.order_type,
            output_file=self.output_file)


def get_instance_class_infos(commodity_code: Optional[str] = None,
                             db_instance_id: Optional[str] = None,
                             infos: Optional[Sequence[pulumi.InputType['GetInstanceClassInfosInfoArgs']]] = None,
                             order_type: Optional[str] = None,
                             output_file: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceClassInfosResult:
    """
    This data source operation to query the instance types that are available to specific instances of Alibaba Cloud.

    > **NOTE:** Available in v1.196.0+

    ## Example Usage


    :param str commodity_code: The commodity code of the instance. Valid values:
           * **bards**: The instance is a pay-as-you-go primary instance. This value is available on the China site (aliyun.com).
           * **rds**: The instance is a subscription primary instance. This value is available on the China site (aliyun.com).
           * **rords**: The instance is a pay-as-you-go read-only instance. This value is available on the China site (aliyun.com).
           * **rds_rordspre_public_cn**: The instance is a subscription read-only instance. This value is available on the China site (aliyun.com).
           * **bards_intl**: The instance is a pay-as-you-go primary instance. This value is available on the International site (alibabacloud.com).
           * **rds_intl**: The instance is a subscription primary instance. This value is available on the International site (alibabacloud.com).
           * **rords_intl**: The instance is a pay-as-you-go read-only instance. This value is available on the International site (alibabacloud.com).
           * **rds_rordspre_public_intl**: The instance is a subscription read-only instance. This value is available on the International site (alibabacloud.com).
    :param str db_instance_id: The ID of the primary instance.
    :param Sequence[pulumi.InputType['GetInstanceClassInfosInfoArgs']] infos: A list of Rds available resource. Each element contains the following attributes:
    :param str order_type: FThe type of order that you want to query. Valid values:
           * **BUY**: specifies the query orders that are used to purchase instances.
           * **UPGRADE**: specifies the query orders that are used to change the specifications of instances.
           * **RENEW**: specifies the query orders that are used to renew instances.
           * **CONVERT**: specifies the query orders that are used to change the billing methods of instances.
    :param str output_file: File name where to save data source results (after running `pulumi up`).
           
           > **NOTE**: If you use the CommodityCode parameter to query the instance types that are available to read-only instances, you must specify the DBInstanceId parameter.
    """
    __args__ = dict()
    __args__['commodityCode'] = commodity_code
    __args__['dbInstanceId'] = db_instance_id
    __args__['infos'] = infos
    __args__['orderType'] = order_type
    __args__['outputFile'] = output_file
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:rds/getInstanceClassInfos:getInstanceClassInfos', __args__, opts=opts, typ=GetInstanceClassInfosResult).value

    return AwaitableGetInstanceClassInfosResult(
        commodity_code=pulumi.get(__ret__, 'commodity_code'),
        db_instance_id=pulumi.get(__ret__, 'db_instance_id'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        infos=pulumi.get(__ret__, 'infos'),
        order_type=pulumi.get(__ret__, 'order_type'),
        output_file=pulumi.get(__ret__, 'output_file'))


@_utilities.lift_output_func(get_instance_class_infos)
def get_instance_class_infos_output(commodity_code: Optional[pulumi.Input[str]] = None,
                                    db_instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                                    infos: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetInstanceClassInfosInfoArgs']]]]] = None,
                                    order_type: Optional[pulumi.Input[str]] = None,
                                    output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceClassInfosResult]:
    """
    This data source operation to query the instance types that are available to specific instances of Alibaba Cloud.

    > **NOTE:** Available in v1.196.0+

    ## Example Usage


    :param str commodity_code: The commodity code of the instance. Valid values:
           * **bards**: The instance is a pay-as-you-go primary instance. This value is available on the China site (aliyun.com).
           * **rds**: The instance is a subscription primary instance. This value is available on the China site (aliyun.com).
           * **rords**: The instance is a pay-as-you-go read-only instance. This value is available on the China site (aliyun.com).
           * **rds_rordspre_public_cn**: The instance is a subscription read-only instance. This value is available on the China site (aliyun.com).
           * **bards_intl**: The instance is a pay-as-you-go primary instance. This value is available on the International site (alibabacloud.com).
           * **rds_intl**: The instance is a subscription primary instance. This value is available on the International site (alibabacloud.com).
           * **rords_intl**: The instance is a pay-as-you-go read-only instance. This value is available on the International site (alibabacloud.com).
           * **rds_rordspre_public_intl**: The instance is a subscription read-only instance. This value is available on the International site (alibabacloud.com).
    :param str db_instance_id: The ID of the primary instance.
    :param Sequence[pulumi.InputType['GetInstanceClassInfosInfoArgs']] infos: A list of Rds available resource. Each element contains the following attributes:
    :param str order_type: FThe type of order that you want to query. Valid values:
           * **BUY**: specifies the query orders that are used to purchase instances.
           * **UPGRADE**: specifies the query orders that are used to change the specifications of instances.
           * **RENEW**: specifies the query orders that are used to renew instances.
           * **CONVERT**: specifies the query orders that are used to change the billing methods of instances.
    :param str output_file: File name where to save data source results (after running `pulumi up`).
           
           > **NOTE**: If you use the CommodityCode parameter to query the instance types that are available to read-only instances, you must specify the DBInstanceId parameter.
    """
    ...
