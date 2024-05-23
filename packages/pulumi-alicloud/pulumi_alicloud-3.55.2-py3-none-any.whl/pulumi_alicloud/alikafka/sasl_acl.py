# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SaslAclArgs', 'SaslAcl']

@pulumi.input_type
class SaslAclArgs:
    def __init__(__self__, *,
                 acl_operation_type: pulumi.Input[str],
                 acl_resource_name: pulumi.Input[str],
                 acl_resource_pattern_type: pulumi.Input[str],
                 acl_resource_type: pulumi.Input[str],
                 instance_id: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        The set of arguments for constructing a SaslAcl resource.
        :param pulumi.Input[str] acl_operation_type: Operation type for this acl. The operation type can only be "Write" and "Read".
        :param pulumi.Input[str] acl_resource_name: Resource name for this acl. The resource name should be a topic or consumer group name.
        :param pulumi.Input[str] acl_resource_pattern_type: Resource pattern type for this acl. The resource pattern support two types "LITERAL" and "PREFIXED". "LITERAL": A literal name defines the full name of a resource. The special wildcard character "*" can be used to represent a resource with any name. "PREFIXED": A prefixed name defines a prefix for a resource.
        :param pulumi.Input[str] acl_resource_type: Resource type for this acl. The resource type can only be "Topic" and "Group".
        :param pulumi.Input[str] instance_id: ID of the ALIKAFKA Instance that owns the groups.
        :param pulumi.Input[str] username: Username for the sasl user. The length should between 1 to 64 characters. The user should be an existed sasl user.
        """
        pulumi.set(__self__, "acl_operation_type", acl_operation_type)
        pulumi.set(__self__, "acl_resource_name", acl_resource_name)
        pulumi.set(__self__, "acl_resource_pattern_type", acl_resource_pattern_type)
        pulumi.set(__self__, "acl_resource_type", acl_resource_type)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="aclOperationType")
    def acl_operation_type(self) -> pulumi.Input[str]:
        """
        Operation type for this acl. The operation type can only be "Write" and "Read".
        """
        return pulumi.get(self, "acl_operation_type")

    @acl_operation_type.setter
    def acl_operation_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_operation_type", value)

    @property
    @pulumi.getter(name="aclResourceName")
    def acl_resource_name(self) -> pulumi.Input[str]:
        """
        Resource name for this acl. The resource name should be a topic or consumer group name.
        """
        return pulumi.get(self, "acl_resource_name")

    @acl_resource_name.setter
    def acl_resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_resource_name", value)

    @property
    @pulumi.getter(name="aclResourcePatternType")
    def acl_resource_pattern_type(self) -> pulumi.Input[str]:
        """
        Resource pattern type for this acl. The resource pattern support two types "LITERAL" and "PREFIXED". "LITERAL": A literal name defines the full name of a resource. The special wildcard character "*" can be used to represent a resource with any name. "PREFIXED": A prefixed name defines a prefix for a resource.
        """
        return pulumi.get(self, "acl_resource_pattern_type")

    @acl_resource_pattern_type.setter
    def acl_resource_pattern_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_resource_pattern_type", value)

    @property
    @pulumi.getter(name="aclResourceType")
    def acl_resource_type(self) -> pulumi.Input[str]:
        """
        Resource type for this acl. The resource type can only be "Topic" and "Group".
        """
        return pulumi.get(self, "acl_resource_type")

    @acl_resource_type.setter
    def acl_resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_resource_type", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        ID of the ALIKAFKA Instance that owns the groups.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        Username for the sasl user. The length should between 1 to 64 characters. The user should be an existed sasl user.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class _SaslAclState:
    def __init__(__self__, *,
                 acl_operation_type: Optional[pulumi.Input[str]] = None,
                 acl_resource_name: Optional[pulumi.Input[str]] = None,
                 acl_resource_pattern_type: Optional[pulumi.Input[str]] = None,
                 acl_resource_type: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SaslAcl resources.
        :param pulumi.Input[str] acl_operation_type: Operation type for this acl. The operation type can only be "Write" and "Read".
        :param pulumi.Input[str] acl_resource_name: Resource name for this acl. The resource name should be a topic or consumer group name.
        :param pulumi.Input[str] acl_resource_pattern_type: Resource pattern type for this acl. The resource pattern support two types "LITERAL" and "PREFIXED". "LITERAL": A literal name defines the full name of a resource. The special wildcard character "*" can be used to represent a resource with any name. "PREFIXED": A prefixed name defines a prefix for a resource.
        :param pulumi.Input[str] acl_resource_type: Resource type for this acl. The resource type can only be "Topic" and "Group".
        :param pulumi.Input[str] host: The host of the acl.
        :param pulumi.Input[str] instance_id: ID of the ALIKAFKA Instance that owns the groups.
        :param pulumi.Input[str] username: Username for the sasl user. The length should between 1 to 64 characters. The user should be an existed sasl user.
        """
        if acl_operation_type is not None:
            pulumi.set(__self__, "acl_operation_type", acl_operation_type)
        if acl_resource_name is not None:
            pulumi.set(__self__, "acl_resource_name", acl_resource_name)
        if acl_resource_pattern_type is not None:
            pulumi.set(__self__, "acl_resource_pattern_type", acl_resource_pattern_type)
        if acl_resource_type is not None:
            pulumi.set(__self__, "acl_resource_type", acl_resource_type)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="aclOperationType")
    def acl_operation_type(self) -> Optional[pulumi.Input[str]]:
        """
        Operation type for this acl. The operation type can only be "Write" and "Read".
        """
        return pulumi.get(self, "acl_operation_type")

    @acl_operation_type.setter
    def acl_operation_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_operation_type", value)

    @property
    @pulumi.getter(name="aclResourceName")
    def acl_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name for this acl. The resource name should be a topic or consumer group name.
        """
        return pulumi.get(self, "acl_resource_name")

    @acl_resource_name.setter
    def acl_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_resource_name", value)

    @property
    @pulumi.getter(name="aclResourcePatternType")
    def acl_resource_pattern_type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource pattern type for this acl. The resource pattern support two types "LITERAL" and "PREFIXED". "LITERAL": A literal name defines the full name of a resource. The special wildcard character "*" can be used to represent a resource with any name. "PREFIXED": A prefixed name defines a prefix for a resource.
        """
        return pulumi.get(self, "acl_resource_pattern_type")

    @acl_resource_pattern_type.setter
    def acl_resource_pattern_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_resource_pattern_type", value)

    @property
    @pulumi.getter(name="aclResourceType")
    def acl_resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type for this acl. The resource type can only be "Topic" and "Group".
        """
        return pulumi.get(self, "acl_resource_type")

    @acl_resource_type.setter
    def acl_resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_resource_type", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The host of the acl.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the ALIKAFKA Instance that owns the groups.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username for the sasl user. The length should between 1 to 64 characters. The user should be an existed sasl user.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class SaslAcl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_operation_type: Optional[pulumi.Input[str]] = None,
                 acl_resource_name: Optional[pulumi.Input[str]] = None,
                 acl_resource_pattern_type: Optional[pulumi.Input[str]] = None,
                 acl_resource_type: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an ALIKAFKA sasl acl resource, see [What is alikafka sasl acl](https://www.alibabacloud.com/help/en/message-queue-for-apache-kafka/latest/api-alikafka-2019-09-16-createacl).

        > **NOTE:** Available since v1.66.0.

        > **NOTE:**  Only the following regions support create alikafka sasl user.
        [`cn-hangzhou`,`cn-beijing`,`cn-shenzhen`,`cn-shanghai`,`cn-qingdao`,`cn-hongkong`,`cn-huhehaote`,`cn-zhangjiakou`,`cn-chengdu`,`cn-heyuan`,`ap-southeast-1`,`ap-southeast-3`,`ap-southeast-5`,`ap-northeast-1`,`eu-central-1`,`eu-west-1`,`us-west-1`,`us-east-1`]

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud
        import pulumi_random as random

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default = alicloud.get_zones(available_resource_creation="VSwitch")
        default_network = alicloud.vpc.Network("default",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("default",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default.zones[0].id)
        default_security_group = alicloud.ecs.SecurityGroup("default", vpc_id=default_network.id)
        default_integer = random.index.Integer("default",
            min=10000,
            max=99999)
        default_instance = alicloud.alikafka.Instance("default",
            name=f"{name}-{default_integer['result']}",
            partition_num=50,
            disk_type=1,
            disk_size=500,
            deploy_type=5,
            io_max=20,
            spec_type="professional",
            service_version="2.2.0",
            config="{\\"enable.acl\\":\\"true\\"}",
            vswitch_id=default_switch.id,
            security_group=default_security_group.id)
        default_topic = alicloud.alikafka.Topic("default",
            instance_id=default_instance.id,
            topic="example-topic",
            remark="topic-remark")
        default_sasl_user = alicloud.alikafka.SaslUser("default",
            instance_id=default_instance.id,
            username=name,
            password="tf_example123")
        default_sasl_acl = alicloud.alikafka.SaslAcl("default",
            instance_id=default_instance.id,
            username=default_sasl_user.username,
            acl_resource_type="Topic",
            acl_resource_name=default_topic.topic,
            acl_resource_pattern_type="LITERAL",
            acl_operation_type="Write")
        ```

        ## Import

        ALIKAFKA GROUP can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:alikafka/saslAcl:SaslAcl acl alikafka_post-cn-123455abc:username:Topic:test-topic:LITERAL:Write
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_operation_type: Operation type for this acl. The operation type can only be "Write" and "Read".
        :param pulumi.Input[str] acl_resource_name: Resource name for this acl. The resource name should be a topic or consumer group name.
        :param pulumi.Input[str] acl_resource_pattern_type: Resource pattern type for this acl. The resource pattern support two types "LITERAL" and "PREFIXED". "LITERAL": A literal name defines the full name of a resource. The special wildcard character "*" can be used to represent a resource with any name. "PREFIXED": A prefixed name defines a prefix for a resource.
        :param pulumi.Input[str] acl_resource_type: Resource type for this acl. The resource type can only be "Topic" and "Group".
        :param pulumi.Input[str] instance_id: ID of the ALIKAFKA Instance that owns the groups.
        :param pulumi.Input[str] username: Username for the sasl user. The length should between 1 to 64 characters. The user should be an existed sasl user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SaslAclArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an ALIKAFKA sasl acl resource, see [What is alikafka sasl acl](https://www.alibabacloud.com/help/en/message-queue-for-apache-kafka/latest/api-alikafka-2019-09-16-createacl).

        > **NOTE:** Available since v1.66.0.

        > **NOTE:**  Only the following regions support create alikafka sasl user.
        [`cn-hangzhou`,`cn-beijing`,`cn-shenzhen`,`cn-shanghai`,`cn-qingdao`,`cn-hongkong`,`cn-huhehaote`,`cn-zhangjiakou`,`cn-chengdu`,`cn-heyuan`,`ap-southeast-1`,`ap-southeast-3`,`ap-southeast-5`,`ap-northeast-1`,`eu-central-1`,`eu-west-1`,`us-west-1`,`us-east-1`]

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud
        import pulumi_random as random

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf_example"
        default = alicloud.get_zones(available_resource_creation="VSwitch")
        default_network = alicloud.vpc.Network("default",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("default",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default.zones[0].id)
        default_security_group = alicloud.ecs.SecurityGroup("default", vpc_id=default_network.id)
        default_integer = random.index.Integer("default",
            min=10000,
            max=99999)
        default_instance = alicloud.alikafka.Instance("default",
            name=f"{name}-{default_integer['result']}",
            partition_num=50,
            disk_type=1,
            disk_size=500,
            deploy_type=5,
            io_max=20,
            spec_type="professional",
            service_version="2.2.0",
            config="{\\"enable.acl\\":\\"true\\"}",
            vswitch_id=default_switch.id,
            security_group=default_security_group.id)
        default_topic = alicloud.alikafka.Topic("default",
            instance_id=default_instance.id,
            topic="example-topic",
            remark="topic-remark")
        default_sasl_user = alicloud.alikafka.SaslUser("default",
            instance_id=default_instance.id,
            username=name,
            password="tf_example123")
        default_sasl_acl = alicloud.alikafka.SaslAcl("default",
            instance_id=default_instance.id,
            username=default_sasl_user.username,
            acl_resource_type="Topic",
            acl_resource_name=default_topic.topic,
            acl_resource_pattern_type="LITERAL",
            acl_operation_type="Write")
        ```

        ## Import

        ALIKAFKA GROUP can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:alikafka/saslAcl:SaslAcl acl alikafka_post-cn-123455abc:username:Topic:test-topic:LITERAL:Write
        ```

        :param str resource_name: The name of the resource.
        :param SaslAclArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SaslAclArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_operation_type: Optional[pulumi.Input[str]] = None,
                 acl_resource_name: Optional[pulumi.Input[str]] = None,
                 acl_resource_pattern_type: Optional[pulumi.Input[str]] = None,
                 acl_resource_type: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SaslAclArgs.__new__(SaslAclArgs)

            if acl_operation_type is None and not opts.urn:
                raise TypeError("Missing required property 'acl_operation_type'")
            __props__.__dict__["acl_operation_type"] = acl_operation_type
            if acl_resource_name is None and not opts.urn:
                raise TypeError("Missing required property 'acl_resource_name'")
            __props__.__dict__["acl_resource_name"] = acl_resource_name
            if acl_resource_pattern_type is None and not opts.urn:
                raise TypeError("Missing required property 'acl_resource_pattern_type'")
            __props__.__dict__["acl_resource_pattern_type"] = acl_resource_pattern_type
            if acl_resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'acl_resource_type'")
            __props__.__dict__["acl_resource_type"] = acl_resource_type
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
            __props__.__dict__["host"] = None
        super(SaslAcl, __self__).__init__(
            'alicloud:alikafka/saslAcl:SaslAcl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl_operation_type: Optional[pulumi.Input[str]] = None,
            acl_resource_name: Optional[pulumi.Input[str]] = None,
            acl_resource_pattern_type: Optional[pulumi.Input[str]] = None,
            acl_resource_type: Optional[pulumi.Input[str]] = None,
            host: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'SaslAcl':
        """
        Get an existing SaslAcl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_operation_type: Operation type for this acl. The operation type can only be "Write" and "Read".
        :param pulumi.Input[str] acl_resource_name: Resource name for this acl. The resource name should be a topic or consumer group name.
        :param pulumi.Input[str] acl_resource_pattern_type: Resource pattern type for this acl. The resource pattern support two types "LITERAL" and "PREFIXED". "LITERAL": A literal name defines the full name of a resource. The special wildcard character "*" can be used to represent a resource with any name. "PREFIXED": A prefixed name defines a prefix for a resource.
        :param pulumi.Input[str] acl_resource_type: Resource type for this acl. The resource type can only be "Topic" and "Group".
        :param pulumi.Input[str] host: The host of the acl.
        :param pulumi.Input[str] instance_id: ID of the ALIKAFKA Instance that owns the groups.
        :param pulumi.Input[str] username: Username for the sasl user. The length should between 1 to 64 characters. The user should be an existed sasl user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SaslAclState.__new__(_SaslAclState)

        __props__.__dict__["acl_operation_type"] = acl_operation_type
        __props__.__dict__["acl_resource_name"] = acl_resource_name
        __props__.__dict__["acl_resource_pattern_type"] = acl_resource_pattern_type
        __props__.__dict__["acl_resource_type"] = acl_resource_type
        __props__.__dict__["host"] = host
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["username"] = username
        return SaslAcl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aclOperationType")
    def acl_operation_type(self) -> pulumi.Output[str]:
        """
        Operation type for this acl. The operation type can only be "Write" and "Read".
        """
        return pulumi.get(self, "acl_operation_type")

    @property
    @pulumi.getter(name="aclResourceName")
    def acl_resource_name(self) -> pulumi.Output[str]:
        """
        Resource name for this acl. The resource name should be a topic or consumer group name.
        """
        return pulumi.get(self, "acl_resource_name")

    @property
    @pulumi.getter(name="aclResourcePatternType")
    def acl_resource_pattern_type(self) -> pulumi.Output[str]:
        """
        Resource pattern type for this acl. The resource pattern support two types "LITERAL" and "PREFIXED". "LITERAL": A literal name defines the full name of a resource. The special wildcard character "*" can be used to represent a resource with any name. "PREFIXED": A prefixed name defines a prefix for a resource.
        """
        return pulumi.get(self, "acl_resource_pattern_type")

    @property
    @pulumi.getter(name="aclResourceType")
    def acl_resource_type(self) -> pulumi.Output[str]:
        """
        Resource type for this acl. The resource type can only be "Topic" and "Group".
        """
        return pulumi.get(self, "acl_resource_type")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        The host of the acl.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        ID of the ALIKAFKA Instance that owns the groups.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        Username for the sasl user. The length should between 1 to 64 characters. The user should be an existed sasl user.
        """
        return pulumi.get(self, "username")

