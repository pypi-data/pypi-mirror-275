# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BackupPolicyArgs', 'BackupPolicy']

@pulumi.input_type
class BackupPolicyArgs:
    def __init__(__self__, *,
                 backup_policy_name: pulumi.Input[str],
                 policy: pulumi.Input[str],
                 policy_version: pulumi.Input[str],
                 uuid_lists: pulumi.Input[Sequence[pulumi.Input[str]]],
                 policy_region_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BackupPolicy resource.
        :param pulumi.Input[str] backup_policy_name: Protection of the Name of the Policy.
        :param pulumi.Input[str] policy: The Specified Protection Policies of the Specific Configuration. see [how to use it](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createbackuppolicy).
        :param pulumi.Input[str] policy_version: Anti-Blackmail Policy Version. Valid values: `1.0.0`, `2.0.0`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] uuid_lists: Specify the Protection of Server UUID List.
        :param pulumi.Input[str] policy_region_id: The region ID of the non-Alibaba cloud server. You can call the [DescribeSupportRegion](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-describesupportregion) interface to view the region supported by anti-ransomware, and then select the region supported by anti-ransomware according to the region where your non-Alibaba cloud server is located.
        """
        pulumi.set(__self__, "backup_policy_name", backup_policy_name)
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "policy_version", policy_version)
        pulumi.set(__self__, "uuid_lists", uuid_lists)
        if policy_region_id is not None:
            pulumi.set(__self__, "policy_region_id", policy_region_id)

    @property
    @pulumi.getter(name="backupPolicyName")
    def backup_policy_name(self) -> pulumi.Input[str]:
        """
        Protection of the Name of the Policy.
        """
        return pulumi.get(self, "backup_policy_name")

    @backup_policy_name.setter
    def backup_policy_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "backup_policy_name", value)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input[str]:
        """
        The Specified Protection Policies of the Specific Configuration. see [how to use it](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createbackuppolicy).
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="policyVersion")
    def policy_version(self) -> pulumi.Input[str]:
        """
        Anti-Blackmail Policy Version. Valid values: `1.0.0`, `2.0.0`.
        """
        return pulumi.get(self, "policy_version")

    @policy_version.setter
    def policy_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_version", value)

    @property
    @pulumi.getter(name="uuidLists")
    def uuid_lists(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Specify the Protection of Server UUID List.
        """
        return pulumi.get(self, "uuid_lists")

    @uuid_lists.setter
    def uuid_lists(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "uuid_lists", value)

    @property
    @pulumi.getter(name="policyRegionId")
    def policy_region_id(self) -> Optional[pulumi.Input[str]]:
        """
        The region ID of the non-Alibaba cloud server. You can call the [DescribeSupportRegion](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-describesupportregion) interface to view the region supported by anti-ransomware, and then select the region supported by anti-ransomware according to the region where your non-Alibaba cloud server is located.
        """
        return pulumi.get(self, "policy_region_id")

    @policy_region_id.setter
    def policy_region_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_region_id", value)


@pulumi.input_type
class _BackupPolicyState:
    def __init__(__self__, *,
                 backup_policy_name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 policy_region_id: Optional[pulumi.Input[str]] = None,
                 policy_version: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 uuid_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering BackupPolicy resources.
        :param pulumi.Input[str] backup_policy_name: Protection of the Name of the Policy.
        :param pulumi.Input[str] policy: The Specified Protection Policies of the Specific Configuration. see [how to use it](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createbackuppolicy).
        :param pulumi.Input[str] policy_region_id: The region ID of the non-Alibaba cloud server. You can call the [DescribeSupportRegion](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-describesupportregion) interface to view the region supported by anti-ransomware, and then select the region supported by anti-ransomware according to the region where your non-Alibaba cloud server is located.
        :param pulumi.Input[str] policy_version: Anti-Blackmail Policy Version. Valid values: `1.0.0`, `2.0.0`.
        :param pulumi.Input[str] status: The status of the Backup Policy instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] uuid_lists: Specify the Protection of Server UUID List.
        """
        if backup_policy_name is not None:
            pulumi.set(__self__, "backup_policy_name", backup_policy_name)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if policy_region_id is not None:
            pulumi.set(__self__, "policy_region_id", policy_region_id)
        if policy_version is not None:
            pulumi.set(__self__, "policy_version", policy_version)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if uuid_lists is not None:
            pulumi.set(__self__, "uuid_lists", uuid_lists)

    @property
    @pulumi.getter(name="backupPolicyName")
    def backup_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Protection of the Name of the Policy.
        """
        return pulumi.get(self, "backup_policy_name")

    @backup_policy_name.setter
    def backup_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_policy_name", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        The Specified Protection Policies of the Specific Configuration. see [how to use it](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createbackuppolicy).
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="policyRegionId")
    def policy_region_id(self) -> Optional[pulumi.Input[str]]:
        """
        The region ID of the non-Alibaba cloud server. You can call the [DescribeSupportRegion](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-describesupportregion) interface to view the region supported by anti-ransomware, and then select the region supported by anti-ransomware according to the region where your non-Alibaba cloud server is located.
        """
        return pulumi.get(self, "policy_region_id")

    @policy_region_id.setter
    def policy_region_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_region_id", value)

    @property
    @pulumi.getter(name="policyVersion")
    def policy_version(self) -> Optional[pulumi.Input[str]]:
        """
        Anti-Blackmail Policy Version. Valid values: `1.0.0`, `2.0.0`.
        """
        return pulumi.get(self, "policy_version")

    @policy_version.setter
    def policy_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_version", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Backup Policy instance.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="uuidLists")
    def uuid_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specify the Protection of Server UUID List.
        """
        return pulumi.get(self, "uuid_lists")

    @uuid_lists.setter
    def uuid_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "uuid_lists", value)


class BackupPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_policy_name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 policy_region_id: Optional[pulumi.Input[str]] = None,
                 policy_version: Optional[pulumi.Input[str]] = None,
                 uuid_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Threat Detection Backup Policy resource.

        For information about Threat Detection Backup Policy and how to use it, see [What is Backup Policy](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createbackuppolicy).

        > **NOTE:** Available in v1.195.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.threatdetection.get_assets(machine_types="ecs")
        default_backup_policy = alicloud.threatdetection.BackupPolicy("default",
            backup_policy_name="tf-example-name",
            policy="{\\"Exclude\\":[\\"/bin/\\",\\"/usr/bin/\\",\\"/sbin/\\",\\"/boot/\\",\\"/proc/\\",\\"/sys/\\",\\"/srv/\\",\\"/lib/\\",\\"/selinux/\\",\\"/usr/sbin/\\",\\"/run/\\",\\"/lib32/\\",\\"/lib64/\\",\\"/lost+found/\\",\\"/var/lib/kubelet/\\",\\"/var/lib/ntp/proc\\",\\"/var/lib/container\\"],\\"ExcludeSystemPath\\":true,\\"Include\\":[],\\"IsDefault\\":1,\\"Retention\\":7,\\"Schedule\\":\\"I|1668703620|PT24H\\",\\"Source\\":[],\\"SpeedLimiter\\":\\"\\",\\"UseVss\\":true}",
            policy_version="2.0.0",
            uuid_lists=[default.ids[0]])
        ```

        ## Import

        Threat Detection Backup Policy can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:threatdetection/backupPolicy:BackupPolicy example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_policy_name: Protection of the Name of the Policy.
        :param pulumi.Input[str] policy: The Specified Protection Policies of the Specific Configuration. see [how to use it](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createbackuppolicy).
        :param pulumi.Input[str] policy_region_id: The region ID of the non-Alibaba cloud server. You can call the [DescribeSupportRegion](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-describesupportregion) interface to view the region supported by anti-ransomware, and then select the region supported by anti-ransomware according to the region where your non-Alibaba cloud server is located.
        :param pulumi.Input[str] policy_version: Anti-Blackmail Policy Version. Valid values: `1.0.0`, `2.0.0`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] uuid_lists: Specify the Protection of Server UUID List.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackupPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Threat Detection Backup Policy resource.

        For information about Threat Detection Backup Policy and how to use it, see [What is Backup Policy](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createbackuppolicy).

        > **NOTE:** Available in v1.195.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.threatdetection.get_assets(machine_types="ecs")
        default_backup_policy = alicloud.threatdetection.BackupPolicy("default",
            backup_policy_name="tf-example-name",
            policy="{\\"Exclude\\":[\\"/bin/\\",\\"/usr/bin/\\",\\"/sbin/\\",\\"/boot/\\",\\"/proc/\\",\\"/sys/\\",\\"/srv/\\",\\"/lib/\\",\\"/selinux/\\",\\"/usr/sbin/\\",\\"/run/\\",\\"/lib32/\\",\\"/lib64/\\",\\"/lost+found/\\",\\"/var/lib/kubelet/\\",\\"/var/lib/ntp/proc\\",\\"/var/lib/container\\"],\\"ExcludeSystemPath\\":true,\\"Include\\":[],\\"IsDefault\\":1,\\"Retention\\":7,\\"Schedule\\":\\"I|1668703620|PT24H\\",\\"Source\\":[],\\"SpeedLimiter\\":\\"\\",\\"UseVss\\":true}",
            policy_version="2.0.0",
            uuid_lists=[default.ids[0]])
        ```

        ## Import

        Threat Detection Backup Policy can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:threatdetection/backupPolicy:BackupPolicy example <id>
        ```

        :param str resource_name: The name of the resource.
        :param BackupPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackupPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_policy_name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 policy_region_id: Optional[pulumi.Input[str]] = None,
                 policy_version: Optional[pulumi.Input[str]] = None,
                 uuid_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackupPolicyArgs.__new__(BackupPolicyArgs)

            if backup_policy_name is None and not opts.urn:
                raise TypeError("Missing required property 'backup_policy_name'")
            __props__.__dict__["backup_policy_name"] = backup_policy_name
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            __props__.__dict__["policy_region_id"] = policy_region_id
            if policy_version is None and not opts.urn:
                raise TypeError("Missing required property 'policy_version'")
            __props__.__dict__["policy_version"] = policy_version
            if uuid_lists is None and not opts.urn:
                raise TypeError("Missing required property 'uuid_lists'")
            __props__.__dict__["uuid_lists"] = uuid_lists
            __props__.__dict__["status"] = None
        super(BackupPolicy, __self__).__init__(
            'alicloud:threatdetection/backupPolicy:BackupPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backup_policy_name: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            policy_region_id: Optional[pulumi.Input[str]] = None,
            policy_version: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            uuid_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'BackupPolicy':
        """
        Get an existing BackupPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_policy_name: Protection of the Name of the Policy.
        :param pulumi.Input[str] policy: The Specified Protection Policies of the Specific Configuration. see [how to use it](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createbackuppolicy).
        :param pulumi.Input[str] policy_region_id: The region ID of the non-Alibaba cloud server. You can call the [DescribeSupportRegion](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-describesupportregion) interface to view the region supported by anti-ransomware, and then select the region supported by anti-ransomware according to the region where your non-Alibaba cloud server is located.
        :param pulumi.Input[str] policy_version: Anti-Blackmail Policy Version. Valid values: `1.0.0`, `2.0.0`.
        :param pulumi.Input[str] status: The status of the Backup Policy instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] uuid_lists: Specify the Protection of Server UUID List.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BackupPolicyState.__new__(_BackupPolicyState)

        __props__.__dict__["backup_policy_name"] = backup_policy_name
        __props__.__dict__["policy"] = policy
        __props__.__dict__["policy_region_id"] = policy_region_id
        __props__.__dict__["policy_version"] = policy_version
        __props__.__dict__["status"] = status
        __props__.__dict__["uuid_lists"] = uuid_lists
        return BackupPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupPolicyName")
    def backup_policy_name(self) -> pulumi.Output[str]:
        """
        Protection of the Name of the Policy.
        """
        return pulumi.get(self, "backup_policy_name")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        The Specified Protection Policies of the Specific Configuration. see [how to use it](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-createbackuppolicy).
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="policyRegionId")
    def policy_region_id(self) -> pulumi.Output[Optional[str]]:
        """
        The region ID of the non-Alibaba cloud server. You can call the [DescribeSupportRegion](https://www.alibabacloud.com/help/en/security-center/developer-reference/api-sas-2018-12-03-describesupportregion) interface to view the region supported by anti-ransomware, and then select the region supported by anti-ransomware according to the region where your non-Alibaba cloud server is located.
        """
        return pulumi.get(self, "policy_region_id")

    @property
    @pulumi.getter(name="policyVersion")
    def policy_version(self) -> pulumi.Output[str]:
        """
        Anti-Blackmail Policy Version. Valid values: `1.0.0`, `2.0.0`.
        """
        return pulumi.get(self, "policy_version")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the Backup Policy instance.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="uuidLists")
    def uuid_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        Specify the Protection of Server UUID List.
        """
        return pulumi.get(self, "uuid_lists")

