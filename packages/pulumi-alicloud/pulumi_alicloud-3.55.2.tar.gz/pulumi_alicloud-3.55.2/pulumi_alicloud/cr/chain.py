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

__all__ = ['ChainArgs', 'Chain']

@pulumi.input_type
class ChainArgs:
    def __init__(__self__, *,
                 chain_name: pulumi.Input[str],
                 instance_id: pulumi.Input[str],
                 chain_configs: Optional[pulumi.Input[Sequence[pulumi.Input['ChainChainConfigArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 repo_name: Optional[pulumi.Input[str]] = None,
                 repo_namespace_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Chain resource.
        :param pulumi.Input[str] chain_name: The name of delivery chain. The length of the name is 1-64 characters, lowercase English letters and numbers, and the separators "_", "-", "." can be used, noted that the separator cannot be at the first or last position.
        :param pulumi.Input[str] instance_id: The ID of CR Enterprise Edition instance.
        :param pulumi.Input[Sequence[pulumi.Input['ChainChainConfigArgs']]] chain_configs: The configuration of delivery chain. See `chain_config` below. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        :param pulumi.Input[str] description: The description delivery chain.
        :param pulumi.Input[str] repo_name: The name of CR Enterprise Edition repository. **NOTE:** This parameter must specify a correct value, otherwise the created resource will be incorrect.
        :param pulumi.Input[str] repo_namespace_name: The name of CR Enterprise Edition namespace. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        pulumi.set(__self__, "chain_name", chain_name)
        pulumi.set(__self__, "instance_id", instance_id)
        if chain_configs is not None:
            pulumi.set(__self__, "chain_configs", chain_configs)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if repo_name is not None:
            pulumi.set(__self__, "repo_name", repo_name)
        if repo_namespace_name is not None:
            pulumi.set(__self__, "repo_namespace_name", repo_namespace_name)

    @property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> pulumi.Input[str]:
        """
        The name of delivery chain. The length of the name is 1-64 characters, lowercase English letters and numbers, and the separators "_", "-", "." can be used, noted that the separator cannot be at the first or last position.
        """
        return pulumi.get(self, "chain_name")

    @chain_name.setter
    def chain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "chain_name", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        The ID of CR Enterprise Edition instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="chainConfigs")
    def chain_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChainChainConfigArgs']]]]:
        """
        The configuration of delivery chain. See `chain_config` below. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        return pulumi.get(self, "chain_configs")

    @chain_configs.setter
    def chain_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChainChainConfigArgs']]]]):
        pulumi.set(self, "chain_configs", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description delivery chain.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of CR Enterprise Edition repository. **NOTE:** This parameter must specify a correct value, otherwise the created resource will be incorrect.
        """
        return pulumi.get(self, "repo_name")

    @repo_name.setter
    def repo_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_name", value)

    @property
    @pulumi.getter(name="repoNamespaceName")
    def repo_namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of CR Enterprise Edition namespace. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        return pulumi.get(self, "repo_namespace_name")

    @repo_namespace_name.setter
    def repo_namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_namespace_name", value)


@pulumi.input_type
class _ChainState:
    def __init__(__self__, *,
                 chain_configs: Optional[pulumi.Input[Sequence[pulumi.Input['ChainChainConfigArgs']]]] = None,
                 chain_id: Optional[pulumi.Input[str]] = None,
                 chain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 repo_name: Optional[pulumi.Input[str]] = None,
                 repo_namespace_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Chain resources.
        :param pulumi.Input[Sequence[pulumi.Input['ChainChainConfigArgs']]] chain_configs: The configuration of delivery chain. See `chain_config` below. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        :param pulumi.Input[str] chain_id: Delivery chain ID.
        :param pulumi.Input[str] chain_name: The name of delivery chain. The length of the name is 1-64 characters, lowercase English letters and numbers, and the separators "_", "-", "." can be used, noted that the separator cannot be at the first or last position.
        :param pulumi.Input[str] description: The description delivery chain.
        :param pulumi.Input[str] instance_id: The ID of CR Enterprise Edition instance.
        :param pulumi.Input[str] repo_name: The name of CR Enterprise Edition repository. **NOTE:** This parameter must specify a correct value, otherwise the created resource will be incorrect.
        :param pulumi.Input[str] repo_namespace_name: The name of CR Enterprise Edition namespace. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        if chain_configs is not None:
            pulumi.set(__self__, "chain_configs", chain_configs)
        if chain_id is not None:
            pulumi.set(__self__, "chain_id", chain_id)
        if chain_name is not None:
            pulumi.set(__self__, "chain_name", chain_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if repo_name is not None:
            pulumi.set(__self__, "repo_name", repo_name)
        if repo_namespace_name is not None:
            pulumi.set(__self__, "repo_namespace_name", repo_namespace_name)

    @property
    @pulumi.getter(name="chainConfigs")
    def chain_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ChainChainConfigArgs']]]]:
        """
        The configuration of delivery chain. See `chain_config` below. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        return pulumi.get(self, "chain_configs")

    @chain_configs.setter
    def chain_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ChainChainConfigArgs']]]]):
        pulumi.set(self, "chain_configs", value)

    @property
    @pulumi.getter(name="chainId")
    def chain_id(self) -> Optional[pulumi.Input[str]]:
        """
        Delivery chain ID.
        """
        return pulumi.get(self, "chain_id")

    @chain_id.setter
    def chain_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "chain_id", value)

    @property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of delivery chain. The length of the name is 1-64 characters, lowercase English letters and numbers, and the separators "_", "-", "." can be used, noted that the separator cannot be at the first or last position.
        """
        return pulumi.get(self, "chain_name")

    @chain_name.setter
    def chain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "chain_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description delivery chain.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of CR Enterprise Edition instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of CR Enterprise Edition repository. **NOTE:** This parameter must specify a correct value, otherwise the created resource will be incorrect.
        """
        return pulumi.get(self, "repo_name")

    @repo_name.setter
    def repo_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_name", value)

    @property
    @pulumi.getter(name="repoNamespaceName")
    def repo_namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of CR Enterprise Edition namespace. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        return pulumi.get(self, "repo_namespace_name")

    @repo_namespace_name.setter
    def repo_namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_namespace_name", value)


class Chain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 chain_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChainChainConfigArgs']]]]] = None,
                 chain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 repo_name: Optional[pulumi.Input[str]] = None,
                 repo_namespace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a CR Chain resource.

        For information about CR Chain and how to use it, see [What is Chain](https://www.alibabacloud.com/help/en/acr/developer-reference/api-cr-2018-12-01-createchain).

        > **NOTE:** Available since v1.161.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default = alicloud.cr.RegistryEnterpriseInstance("default",
            payment_type="Subscription",
            period=1,
            renew_period=0,
            renewal_status="ManualRenewal",
            instance_type="Advanced",
            instance_name=name)
        default_registry_enterprise_namespace = alicloud.cs.RegistryEnterpriseNamespace("default",
            instance_id=default.id,
            name=name,
            auto_create=False,
            default_visibility="PUBLIC")
        default_registry_enterprise_repo = alicloud.cs.RegistryEnterpriseRepo("default",
            instance_id=default.id,
            namespace=default_registry_enterprise_namespace.name,
            name=name,
            summary="this is summary of my new repo",
            repo_type="PUBLIC",
            detail="this is a public repo")
        default_chain = alicloud.cr.Chain("default",
            chain_configs=[alicloud.cr.ChainChainConfigArgs(
                nodes=[
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=True,
                        node_name="DOCKER_IMAGE_BUILD",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=True,
                        node_name="DOCKER_IMAGE_PUSH",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        enable=True,
                        node_name="VULNERABILITY_SCANNING",
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs(
                                issue_level="MEDIUM",
                                issue_count="1",
                                action="BLOCK_DELETE_TAG",
                                logic="AND",
                            )],
                        )],
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=True,
                        node_name="ACTIVATE_REPLICATION",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=True,
                        node_name="TRIGGER",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=False,
                        node_name="SNAPSHOT",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=False,
                        node_name="TRIGGER_SNAPSHOT",
                    ),
                ],
                routers=[
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="DOCKER_IMAGE_BUILD",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="DOCKER_IMAGE_PUSH",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="DOCKER_IMAGE_PUSH",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="VULNERABILITY_SCANNING",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="VULNERABILITY_SCANNING",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="ACTIVATE_REPLICATION",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="ACTIVATE_REPLICATION",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="TRIGGER",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="VULNERABILITY_SCANNING",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="SNAPSHOT",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="SNAPSHOT",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="TRIGGER_SNAPSHOT",
                        )],
                    ),
                ],
            )],
            chain_name=name,
            description=name,
            instance_id=default_registry_enterprise_namespace.instance_id,
            repo_name=default_registry_enterprise_repo.name,
            repo_namespace_name=default_registry_enterprise_namespace.name)
        ```

        ## Import

        CR Chain can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cr/chain:Chain example <instance_id>:<chain_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChainChainConfigArgs']]]] chain_configs: The configuration of delivery chain. See `chain_config` below. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        :param pulumi.Input[str] chain_name: The name of delivery chain. The length of the name is 1-64 characters, lowercase English letters and numbers, and the separators "_", "-", "." can be used, noted that the separator cannot be at the first or last position.
        :param pulumi.Input[str] description: The description delivery chain.
        :param pulumi.Input[str] instance_id: The ID of CR Enterprise Edition instance.
        :param pulumi.Input[str] repo_name: The name of CR Enterprise Edition repository. **NOTE:** This parameter must specify a correct value, otherwise the created resource will be incorrect.
        :param pulumi.Input[str] repo_namespace_name: The name of CR Enterprise Edition namespace. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a CR Chain resource.

        For information about CR Chain and how to use it, see [What is Chain](https://www.alibabacloud.com/help/en/acr/developer-reference/api-cr-2018-12-01-createchain).

        > **NOTE:** Available since v1.161.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default = alicloud.cr.RegistryEnterpriseInstance("default",
            payment_type="Subscription",
            period=1,
            renew_period=0,
            renewal_status="ManualRenewal",
            instance_type="Advanced",
            instance_name=name)
        default_registry_enterprise_namespace = alicloud.cs.RegistryEnterpriseNamespace("default",
            instance_id=default.id,
            name=name,
            auto_create=False,
            default_visibility="PUBLIC")
        default_registry_enterprise_repo = alicloud.cs.RegistryEnterpriseRepo("default",
            instance_id=default.id,
            namespace=default_registry_enterprise_namespace.name,
            name=name,
            summary="this is summary of my new repo",
            repo_type="PUBLIC",
            detail="this is a public repo")
        default_chain = alicloud.cr.Chain("default",
            chain_configs=[alicloud.cr.ChainChainConfigArgs(
                nodes=[
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=True,
                        node_name="DOCKER_IMAGE_BUILD",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=True,
                        node_name="DOCKER_IMAGE_PUSH",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        enable=True,
                        node_name="VULNERABILITY_SCANNING",
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs(
                                issue_level="MEDIUM",
                                issue_count="1",
                                action="BLOCK_DELETE_TAG",
                                logic="AND",
                            )],
                        )],
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=True,
                        node_name="ACTIVATE_REPLICATION",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=True,
                        node_name="TRIGGER",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=False,
                        node_name="SNAPSHOT",
                    ),
                    alicloud.cr.ChainChainConfigNodeArgs(
                        node_configs=[alicloud.cr.ChainChainConfigNodeNodeConfigArgs(
                            deny_policies=[alicloud.cr.ChainChainConfigNodeNodeConfigDenyPolicyArgs()],
                        )],
                        enable=False,
                        node_name="TRIGGER_SNAPSHOT",
                    ),
                ],
                routers=[
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="DOCKER_IMAGE_BUILD",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="DOCKER_IMAGE_PUSH",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="DOCKER_IMAGE_PUSH",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="VULNERABILITY_SCANNING",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="VULNERABILITY_SCANNING",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="ACTIVATE_REPLICATION",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="ACTIVATE_REPLICATION",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="TRIGGER",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="VULNERABILITY_SCANNING",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="SNAPSHOT",
                        )],
                    ),
                    alicloud.cr.ChainChainConfigRouterArgs(
                        froms=[alicloud.cr.ChainChainConfigRouterFromArgs(
                            node_name="SNAPSHOT",
                        )],
                        tos=[alicloud.cr.ChainChainConfigRouterToArgs(
                            node_name="TRIGGER_SNAPSHOT",
                        )],
                    ),
                ],
            )],
            chain_name=name,
            description=name,
            instance_id=default_registry_enterprise_namespace.instance_id,
            repo_name=default_registry_enterprise_repo.name,
            repo_namespace_name=default_registry_enterprise_namespace.name)
        ```

        ## Import

        CR Chain can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cr/chain:Chain example <instance_id>:<chain_id>
        ```

        :param str resource_name: The name of the resource.
        :param ChainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 chain_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChainChainConfigArgs']]]]] = None,
                 chain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 repo_name: Optional[pulumi.Input[str]] = None,
                 repo_namespace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ChainArgs.__new__(ChainArgs)

            __props__.__dict__["chain_configs"] = chain_configs
            if chain_name is None and not opts.urn:
                raise TypeError("Missing required property 'chain_name'")
            __props__.__dict__["chain_name"] = chain_name
            __props__.__dict__["description"] = description
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["repo_name"] = repo_name
            __props__.__dict__["repo_namespace_name"] = repo_namespace_name
            __props__.__dict__["chain_id"] = None
        super(Chain, __self__).__init__(
            'alicloud:cr/chain:Chain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            chain_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChainChainConfigArgs']]]]] = None,
            chain_id: Optional[pulumi.Input[str]] = None,
            chain_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            repo_name: Optional[pulumi.Input[str]] = None,
            repo_namespace_name: Optional[pulumi.Input[str]] = None) -> 'Chain':
        """
        Get an existing Chain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ChainChainConfigArgs']]]] chain_configs: The configuration of delivery chain. See `chain_config` below. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        :param pulumi.Input[str] chain_id: Delivery chain ID.
        :param pulumi.Input[str] chain_name: The name of delivery chain. The length of the name is 1-64 characters, lowercase English letters and numbers, and the separators "_", "-", "." can be used, noted that the separator cannot be at the first or last position.
        :param pulumi.Input[str] description: The description delivery chain.
        :param pulumi.Input[str] instance_id: The ID of CR Enterprise Edition instance.
        :param pulumi.Input[str] repo_name: The name of CR Enterprise Edition repository. **NOTE:** This parameter must specify a correct value, otherwise the created resource will be incorrect.
        :param pulumi.Input[str] repo_namespace_name: The name of CR Enterprise Edition namespace. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ChainState.__new__(_ChainState)

        __props__.__dict__["chain_configs"] = chain_configs
        __props__.__dict__["chain_id"] = chain_id
        __props__.__dict__["chain_name"] = chain_name
        __props__.__dict__["description"] = description
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["repo_name"] = repo_name
        __props__.__dict__["repo_namespace_name"] = repo_namespace_name
        return Chain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="chainConfigs")
    def chain_configs(self) -> pulumi.Output[Optional[Sequence['outputs.ChainChainConfig']]]:
        """
        The configuration of delivery chain. See `chain_config` below. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        return pulumi.get(self, "chain_configs")

    @property
    @pulumi.getter(name="chainId")
    def chain_id(self) -> pulumi.Output[str]:
        """
        Delivery chain ID.
        """
        return pulumi.get(self, "chain_id")

    @property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> pulumi.Output[str]:
        """
        The name of delivery chain. The length of the name is 1-64 characters, lowercase English letters and numbers, and the separators "_", "-", "." can be used, noted that the separator cannot be at the first or last position.
        """
        return pulumi.get(self, "chain_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description delivery chain.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The ID of CR Enterprise Edition instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of CR Enterprise Edition repository. **NOTE:** This parameter must specify a correct value, otherwise the created resource will be incorrect.
        """
        return pulumi.get(self, "repo_name")

    @property
    @pulumi.getter(name="repoNamespaceName")
    def repo_namespace_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of CR Enterprise Edition namespace. **NOTE:** This parameter must specify the correct value, otherwise the created resource will be incorrect.
        """
        return pulumi.get(self, "repo_namespace_name")

