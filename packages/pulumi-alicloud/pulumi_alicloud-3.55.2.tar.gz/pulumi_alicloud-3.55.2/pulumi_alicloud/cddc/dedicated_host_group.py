# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DedicatedHostGroupArgs', 'DedicatedHostGroup']

@pulumi.input_type
class DedicatedHostGroupArgs:
    def __init__(__self__, *,
                 engine: pulumi.Input[str],
                 vpc_id: pulumi.Input[str],
                 allocation_policy: Optional[pulumi.Input[str]] = None,
                 cpu_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 dedicated_host_group_desc: Optional[pulumi.Input[str]] = None,
                 disk_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 host_replace_policy: Optional[pulumi.Input[str]] = None,
                 mem_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 open_permission: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a DedicatedHostGroup resource.
        :param pulumi.Input[str] engine: Database Engine Type.The database engine of the dedicated cluster. Valid values:`Redis`, `SQLServer`, `MySQL`, `PostgreSQL`, `MongoDB`, `alisql`, `tair`, `mssql`. **NOTE:** Since v1.210.0., the `engine = SQLServer` was deprecated.
        :param pulumi.Input[str] vpc_id: The virtual private cloud (VPC) ID of the dedicated cluster.
        :param pulumi.Input[str] allocation_policy: AThe policy that is used to allocate resources in the dedicated cluster. Valid values:`Evenly`,`Intensively`
        :param pulumi.Input[int] cpu_allocation_ratio: The CPU overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        :param pulumi.Input[str] dedicated_host_group_desc: The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        :param pulumi.Input[int] disk_allocation_ratio: The Disk Allocation Ratio of the Dedicated Host Group. **NOTE:** When `engine = SQLServer`, this attribute does not support to set.
        :param pulumi.Input[str] host_replace_policy: The policy based on which the system handles host failures. Valid values:`Auto`,`Manual`
        :param pulumi.Input[int] mem_allocation_ratio: The Memory Allocation Ratio of the Dedicated Host Group.
        :param pulumi.Input[bool] open_permission: Whether to enable the feature that allows you to have OS permissions on the hosts in the dedicated cluster. Valid values: `true` and `false`.
               **NOTE:** The `open_permission` should be `true` when `engine = "SQLServer"`
        """
        pulumi.set(__self__, "engine", engine)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if allocation_policy is not None:
            pulumi.set(__self__, "allocation_policy", allocation_policy)
        if cpu_allocation_ratio is not None:
            pulumi.set(__self__, "cpu_allocation_ratio", cpu_allocation_ratio)
        if dedicated_host_group_desc is not None:
            pulumi.set(__self__, "dedicated_host_group_desc", dedicated_host_group_desc)
        if disk_allocation_ratio is not None:
            pulumi.set(__self__, "disk_allocation_ratio", disk_allocation_ratio)
        if host_replace_policy is not None:
            pulumi.set(__self__, "host_replace_policy", host_replace_policy)
        if mem_allocation_ratio is not None:
            pulumi.set(__self__, "mem_allocation_ratio", mem_allocation_ratio)
        if open_permission is not None:
            pulumi.set(__self__, "open_permission", open_permission)

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Input[str]:
        """
        Database Engine Type.The database engine of the dedicated cluster. Valid values:`Redis`, `SQLServer`, `MySQL`, `PostgreSQL`, `MongoDB`, `alisql`, `tair`, `mssql`. **NOTE:** Since v1.210.0., the `engine = SQLServer` was deprecated.
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The virtual private cloud (VPC) ID of the dedicated cluster.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="allocationPolicy")
    def allocation_policy(self) -> Optional[pulumi.Input[str]]:
        """
        AThe policy that is used to allocate resources in the dedicated cluster. Valid values:`Evenly`,`Intensively`
        """
        return pulumi.get(self, "allocation_policy")

    @allocation_policy.setter
    def allocation_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allocation_policy", value)

    @property
    @pulumi.getter(name="cpuAllocationRatio")
    def cpu_allocation_ratio(self) -> Optional[pulumi.Input[int]]:
        """
        The CPU overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        """
        return pulumi.get(self, "cpu_allocation_ratio")

    @cpu_allocation_ratio.setter
    def cpu_allocation_ratio(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cpu_allocation_ratio", value)

    @property
    @pulumi.getter(name="dedicatedHostGroupDesc")
    def dedicated_host_group_desc(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        """
        return pulumi.get(self, "dedicated_host_group_desc")

    @dedicated_host_group_desc.setter
    def dedicated_host_group_desc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dedicated_host_group_desc", value)

    @property
    @pulumi.getter(name="diskAllocationRatio")
    def disk_allocation_ratio(self) -> Optional[pulumi.Input[int]]:
        """
        The Disk Allocation Ratio of the Dedicated Host Group. **NOTE:** When `engine = SQLServer`, this attribute does not support to set.
        """
        return pulumi.get(self, "disk_allocation_ratio")

    @disk_allocation_ratio.setter
    def disk_allocation_ratio(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_allocation_ratio", value)

    @property
    @pulumi.getter(name="hostReplacePolicy")
    def host_replace_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The policy based on which the system handles host failures. Valid values:`Auto`,`Manual`
        """
        return pulumi.get(self, "host_replace_policy")

    @host_replace_policy.setter
    def host_replace_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_replace_policy", value)

    @property
    @pulumi.getter(name="memAllocationRatio")
    def mem_allocation_ratio(self) -> Optional[pulumi.Input[int]]:
        """
        The Memory Allocation Ratio of the Dedicated Host Group.
        """
        return pulumi.get(self, "mem_allocation_ratio")

    @mem_allocation_ratio.setter
    def mem_allocation_ratio(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mem_allocation_ratio", value)

    @property
    @pulumi.getter(name="openPermission")
    def open_permission(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable the feature that allows you to have OS permissions on the hosts in the dedicated cluster. Valid values: `true` and `false`.
        **NOTE:** The `open_permission` should be `true` when `engine = "SQLServer"`
        """
        return pulumi.get(self, "open_permission")

    @open_permission.setter
    def open_permission(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "open_permission", value)


@pulumi.input_type
class _DedicatedHostGroupState:
    def __init__(__self__, *,
                 allocation_policy: Optional[pulumi.Input[str]] = None,
                 cpu_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 dedicated_host_group_desc: Optional[pulumi.Input[str]] = None,
                 disk_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 host_replace_policy: Optional[pulumi.Input[str]] = None,
                 mem_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 open_permission: Optional[pulumi.Input[bool]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DedicatedHostGroup resources.
        :param pulumi.Input[str] allocation_policy: AThe policy that is used to allocate resources in the dedicated cluster. Valid values:`Evenly`,`Intensively`
        :param pulumi.Input[int] cpu_allocation_ratio: The CPU overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        :param pulumi.Input[str] dedicated_host_group_desc: The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        :param pulumi.Input[int] disk_allocation_ratio: The Disk Allocation Ratio of the Dedicated Host Group. **NOTE:** When `engine = SQLServer`, this attribute does not support to set.
        :param pulumi.Input[str] engine: Database Engine Type.The database engine of the dedicated cluster. Valid values:`Redis`, `SQLServer`, `MySQL`, `PostgreSQL`, `MongoDB`, `alisql`, `tair`, `mssql`. **NOTE:** Since v1.210.0., the `engine = SQLServer` was deprecated.
        :param pulumi.Input[str] host_replace_policy: The policy based on which the system handles host failures. Valid values:`Auto`,`Manual`
        :param pulumi.Input[int] mem_allocation_ratio: The Memory Allocation Ratio of the Dedicated Host Group.
        :param pulumi.Input[bool] open_permission: Whether to enable the feature that allows you to have OS permissions on the hosts in the dedicated cluster. Valid values: `true` and `false`.
               **NOTE:** The `open_permission` should be `true` when `engine = "SQLServer"`
        :param pulumi.Input[str] vpc_id: The virtual private cloud (VPC) ID of the dedicated cluster.
        """
        if allocation_policy is not None:
            pulumi.set(__self__, "allocation_policy", allocation_policy)
        if cpu_allocation_ratio is not None:
            pulumi.set(__self__, "cpu_allocation_ratio", cpu_allocation_ratio)
        if dedicated_host_group_desc is not None:
            pulumi.set(__self__, "dedicated_host_group_desc", dedicated_host_group_desc)
        if disk_allocation_ratio is not None:
            pulumi.set(__self__, "disk_allocation_ratio", disk_allocation_ratio)
        if engine is not None:
            pulumi.set(__self__, "engine", engine)
        if host_replace_policy is not None:
            pulumi.set(__self__, "host_replace_policy", host_replace_policy)
        if mem_allocation_ratio is not None:
            pulumi.set(__self__, "mem_allocation_ratio", mem_allocation_ratio)
        if open_permission is not None:
            pulumi.set(__self__, "open_permission", open_permission)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="allocationPolicy")
    def allocation_policy(self) -> Optional[pulumi.Input[str]]:
        """
        AThe policy that is used to allocate resources in the dedicated cluster. Valid values:`Evenly`,`Intensively`
        """
        return pulumi.get(self, "allocation_policy")

    @allocation_policy.setter
    def allocation_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allocation_policy", value)

    @property
    @pulumi.getter(name="cpuAllocationRatio")
    def cpu_allocation_ratio(self) -> Optional[pulumi.Input[int]]:
        """
        The CPU overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        """
        return pulumi.get(self, "cpu_allocation_ratio")

    @cpu_allocation_ratio.setter
    def cpu_allocation_ratio(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cpu_allocation_ratio", value)

    @property
    @pulumi.getter(name="dedicatedHostGroupDesc")
    def dedicated_host_group_desc(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        """
        return pulumi.get(self, "dedicated_host_group_desc")

    @dedicated_host_group_desc.setter
    def dedicated_host_group_desc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dedicated_host_group_desc", value)

    @property
    @pulumi.getter(name="diskAllocationRatio")
    def disk_allocation_ratio(self) -> Optional[pulumi.Input[int]]:
        """
        The Disk Allocation Ratio of the Dedicated Host Group. **NOTE:** When `engine = SQLServer`, this attribute does not support to set.
        """
        return pulumi.get(self, "disk_allocation_ratio")

    @disk_allocation_ratio.setter
    def disk_allocation_ratio(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_allocation_ratio", value)

    @property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[str]]:
        """
        Database Engine Type.The database engine of the dedicated cluster. Valid values:`Redis`, `SQLServer`, `MySQL`, `PostgreSQL`, `MongoDB`, `alisql`, `tair`, `mssql`. **NOTE:** Since v1.210.0., the `engine = SQLServer` was deprecated.
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="hostReplacePolicy")
    def host_replace_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The policy based on which the system handles host failures. Valid values:`Auto`,`Manual`
        """
        return pulumi.get(self, "host_replace_policy")

    @host_replace_policy.setter
    def host_replace_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_replace_policy", value)

    @property
    @pulumi.getter(name="memAllocationRatio")
    def mem_allocation_ratio(self) -> Optional[pulumi.Input[int]]:
        """
        The Memory Allocation Ratio of the Dedicated Host Group.
        """
        return pulumi.get(self, "mem_allocation_ratio")

    @mem_allocation_ratio.setter
    def mem_allocation_ratio(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mem_allocation_ratio", value)

    @property
    @pulumi.getter(name="openPermission")
    def open_permission(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enable the feature that allows you to have OS permissions on the hosts in the dedicated cluster. Valid values: `true` and `false`.
        **NOTE:** The `open_permission` should be `true` when `engine = "SQLServer"`
        """
        return pulumi.get(self, "open_permission")

    @open_permission.setter
    def open_permission(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "open_permission", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        The virtual private cloud (VPC) ID of the dedicated cluster.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class DedicatedHostGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_policy: Optional[pulumi.Input[str]] = None,
                 cpu_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 dedicated_host_group_desc: Optional[pulumi.Input[str]] = None,
                 disk_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 host_replace_policy: Optional[pulumi.Input[str]] = None,
                 mem_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 open_permission: Optional[pulumi.Input[bool]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a ApsaraDB for MyBase Dedicated Host Group resource.

        For information about ApsaraDB for MyBase Dedicated Host Group and how to use it, see [What is Dedicated Host Group](https://www.alibabacloud.com/help/en/apsaradb-for-mybase/latest/creatededicatedhostgroup).

        > **NOTE:** Available since v1.132.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default = alicloud.vpc.Network("default",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_dedicated_host_group = alicloud.cddc.DedicatedHostGroup("default",
            engine="MySQL",
            vpc_id=default.id,
            cpu_allocation_ratio=101,
            mem_allocation_ratio=50,
            disk_allocation_ratio=200,
            allocation_policy="Evenly",
            host_replace_policy="Manual",
            dedicated_host_group_desc=name)
        ```

        ## Import

        ApsaraDB for MyBase Dedicated Host Group can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cddc/dedicatedHostGroup:DedicatedHostGroup example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allocation_policy: AThe policy that is used to allocate resources in the dedicated cluster. Valid values:`Evenly`,`Intensively`
        :param pulumi.Input[int] cpu_allocation_ratio: The CPU overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        :param pulumi.Input[str] dedicated_host_group_desc: The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        :param pulumi.Input[int] disk_allocation_ratio: The Disk Allocation Ratio of the Dedicated Host Group. **NOTE:** When `engine = SQLServer`, this attribute does not support to set.
        :param pulumi.Input[str] engine: Database Engine Type.The database engine of the dedicated cluster. Valid values:`Redis`, `SQLServer`, `MySQL`, `PostgreSQL`, `MongoDB`, `alisql`, `tair`, `mssql`. **NOTE:** Since v1.210.0., the `engine = SQLServer` was deprecated.
        :param pulumi.Input[str] host_replace_policy: The policy based on which the system handles host failures. Valid values:`Auto`,`Manual`
        :param pulumi.Input[int] mem_allocation_ratio: The Memory Allocation Ratio of the Dedicated Host Group.
        :param pulumi.Input[bool] open_permission: Whether to enable the feature that allows you to have OS permissions on the hosts in the dedicated cluster. Valid values: `true` and `false`.
               **NOTE:** The `open_permission` should be `true` when `engine = "SQLServer"`
        :param pulumi.Input[str] vpc_id: The virtual private cloud (VPC) ID of the dedicated cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DedicatedHostGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a ApsaraDB for MyBase Dedicated Host Group resource.

        For information about ApsaraDB for MyBase Dedicated Host Group and how to use it, see [What is Dedicated Host Group](https://www.alibabacloud.com/help/en/apsaradb-for-mybase/latest/creatededicatedhostgroup).

        > **NOTE:** Available since v1.132.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default = alicloud.vpc.Network("default",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_dedicated_host_group = alicloud.cddc.DedicatedHostGroup("default",
            engine="MySQL",
            vpc_id=default.id,
            cpu_allocation_ratio=101,
            mem_allocation_ratio=50,
            disk_allocation_ratio=200,
            allocation_policy="Evenly",
            host_replace_policy="Manual",
            dedicated_host_group_desc=name)
        ```

        ## Import

        ApsaraDB for MyBase Dedicated Host Group can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cddc/dedicatedHostGroup:DedicatedHostGroup example <id>
        ```

        :param str resource_name: The name of the resource.
        :param DedicatedHostGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DedicatedHostGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_policy: Optional[pulumi.Input[str]] = None,
                 cpu_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 dedicated_host_group_desc: Optional[pulumi.Input[str]] = None,
                 disk_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 host_replace_policy: Optional[pulumi.Input[str]] = None,
                 mem_allocation_ratio: Optional[pulumi.Input[int]] = None,
                 open_permission: Optional[pulumi.Input[bool]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DedicatedHostGroupArgs.__new__(DedicatedHostGroupArgs)

            __props__.__dict__["allocation_policy"] = allocation_policy
            __props__.__dict__["cpu_allocation_ratio"] = cpu_allocation_ratio
            __props__.__dict__["dedicated_host_group_desc"] = dedicated_host_group_desc
            __props__.__dict__["disk_allocation_ratio"] = disk_allocation_ratio
            if engine is None and not opts.urn:
                raise TypeError("Missing required property 'engine'")
            __props__.__dict__["engine"] = engine
            __props__.__dict__["host_replace_policy"] = host_replace_policy
            __props__.__dict__["mem_allocation_ratio"] = mem_allocation_ratio
            __props__.__dict__["open_permission"] = open_permission
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
        super(DedicatedHostGroup, __self__).__init__(
            'alicloud:cddc/dedicatedHostGroup:DedicatedHostGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allocation_policy: Optional[pulumi.Input[str]] = None,
            cpu_allocation_ratio: Optional[pulumi.Input[int]] = None,
            dedicated_host_group_desc: Optional[pulumi.Input[str]] = None,
            disk_allocation_ratio: Optional[pulumi.Input[int]] = None,
            engine: Optional[pulumi.Input[str]] = None,
            host_replace_policy: Optional[pulumi.Input[str]] = None,
            mem_allocation_ratio: Optional[pulumi.Input[int]] = None,
            open_permission: Optional[pulumi.Input[bool]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'DedicatedHostGroup':
        """
        Get an existing DedicatedHostGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allocation_policy: AThe policy that is used to allocate resources in the dedicated cluster. Valid values:`Evenly`,`Intensively`
        :param pulumi.Input[int] cpu_allocation_ratio: The CPU overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        :param pulumi.Input[str] dedicated_host_group_desc: The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        :param pulumi.Input[int] disk_allocation_ratio: The Disk Allocation Ratio of the Dedicated Host Group. **NOTE:** When `engine = SQLServer`, this attribute does not support to set.
        :param pulumi.Input[str] engine: Database Engine Type.The database engine of the dedicated cluster. Valid values:`Redis`, `SQLServer`, `MySQL`, `PostgreSQL`, `MongoDB`, `alisql`, `tair`, `mssql`. **NOTE:** Since v1.210.0., the `engine = SQLServer` was deprecated.
        :param pulumi.Input[str] host_replace_policy: The policy based on which the system handles host failures. Valid values:`Auto`,`Manual`
        :param pulumi.Input[int] mem_allocation_ratio: The Memory Allocation Ratio of the Dedicated Host Group.
        :param pulumi.Input[bool] open_permission: Whether to enable the feature that allows you to have OS permissions on the hosts in the dedicated cluster. Valid values: `true` and `false`.
               **NOTE:** The `open_permission` should be `true` when `engine = "SQLServer"`
        :param pulumi.Input[str] vpc_id: The virtual private cloud (VPC) ID of the dedicated cluster.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DedicatedHostGroupState.__new__(_DedicatedHostGroupState)

        __props__.__dict__["allocation_policy"] = allocation_policy
        __props__.__dict__["cpu_allocation_ratio"] = cpu_allocation_ratio
        __props__.__dict__["dedicated_host_group_desc"] = dedicated_host_group_desc
        __props__.__dict__["disk_allocation_ratio"] = disk_allocation_ratio
        __props__.__dict__["engine"] = engine
        __props__.__dict__["host_replace_policy"] = host_replace_policy
        __props__.__dict__["mem_allocation_ratio"] = mem_allocation_ratio
        __props__.__dict__["open_permission"] = open_permission
        __props__.__dict__["vpc_id"] = vpc_id
        return DedicatedHostGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocationPolicy")
    def allocation_policy(self) -> pulumi.Output[str]:
        """
        AThe policy that is used to allocate resources in the dedicated cluster. Valid values:`Evenly`,`Intensively`
        """
        return pulumi.get(self, "allocation_policy")

    @property
    @pulumi.getter(name="cpuAllocationRatio")
    def cpu_allocation_ratio(self) -> pulumi.Output[int]:
        """
        The CPU overcommitment ratio of the dedicated cluster.Valid values: 100 to 300. Default value: 200.
        """
        return pulumi.get(self, "cpu_allocation_ratio")

    @property
    @pulumi.getter(name="dedicatedHostGroupDesc")
    def dedicated_host_group_desc(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the dedicated cluster. The name must be 1 to 64 characters in length and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        """
        return pulumi.get(self, "dedicated_host_group_desc")

    @property
    @pulumi.getter(name="diskAllocationRatio")
    def disk_allocation_ratio(self) -> pulumi.Output[int]:
        """
        The Disk Allocation Ratio of the Dedicated Host Group. **NOTE:** When `engine = SQLServer`, this attribute does not support to set.
        """
        return pulumi.get(self, "disk_allocation_ratio")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[str]:
        """
        Database Engine Type.The database engine of the dedicated cluster. Valid values:`Redis`, `SQLServer`, `MySQL`, `PostgreSQL`, `MongoDB`, `alisql`, `tair`, `mssql`. **NOTE:** Since v1.210.0., the `engine = SQLServer` was deprecated.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="hostReplacePolicy")
    def host_replace_policy(self) -> pulumi.Output[str]:
        """
        The policy based on which the system handles host failures. Valid values:`Auto`,`Manual`
        """
        return pulumi.get(self, "host_replace_policy")

    @property
    @pulumi.getter(name="memAllocationRatio")
    def mem_allocation_ratio(self) -> pulumi.Output[int]:
        """
        The Memory Allocation Ratio of the Dedicated Host Group.
        """
        return pulumi.get(self, "mem_allocation_ratio")

    @property
    @pulumi.getter(name="openPermission")
    def open_permission(self) -> pulumi.Output[bool]:
        """
        Whether to enable the feature that allows you to have OS permissions on the hosts in the dedicated cluster. Valid values: `true` and `false`.
        **NOTE:** The `open_permission` should be `true` when `engine = "SQLServer"`
        """
        return pulumi.get(self, "open_permission")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The virtual private cloud (VPC) ID of the dedicated cluster.
        """
        return pulumi.get(self, "vpc_id")

