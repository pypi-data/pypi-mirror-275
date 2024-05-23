# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['LayerVersionArgs', 'LayerVersion']

@pulumi.input_type
class LayerVersionArgs:
    def __init__(__self__, *,
                 compatible_runtimes: pulumi.Input[Sequence[pulumi.Input[str]]],
                 layer_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 oss_bucket_name: Optional[pulumi.Input[str]] = None,
                 oss_object_name: Optional[pulumi.Input[str]] = None,
                 skip_destroy: Optional[pulumi.Input[bool]] = None,
                 zip_file: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LayerVersion resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] compatible_runtimes: The list of runtime environments that are supported by the layer. Valid values: `nodejs14`, `nodejs12`, `nodejs10`, `nodejs8`, `nodejs6`, `python3.9`, `python3`, `python2.7`, `java11`, `java8`, `php7.2`, `go1`,`dotnetcore2.1`, `custom`.
        :param pulumi.Input[str] layer_name: The name of the layer.
        :param pulumi.Input[str] description: The description of the layer version.
        :param pulumi.Input[str] oss_bucket_name: The name of the OSS bucket that stores the ZIP package of the function code.
        :param pulumi.Input[str] oss_object_name: The name of the OSS object (ZIP package) that contains the function code.
        :param pulumi.Input[bool] skip_destroy: Whether to retain the old version of a previously deployed Lambda Layer. Default is `false`. When this is not set to `true`, changing any of `compatible_runtimes`, `description`, `layer_name`, `oss_bucket_name`,  `oss_object_name`, or `zip_file` forces deletion of the existing layer version and creation of a new layer version.
        :param pulumi.Input[str] zip_file: The ZIP package of the function code that is encoded in the Base64 format.
               
               > **NOTE:** `zip_file` and `oss_bucket_name`, `oss_object_name` cannot be used together.
        """
        pulumi.set(__self__, "compatible_runtimes", compatible_runtimes)
        pulumi.set(__self__, "layer_name", layer_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if oss_bucket_name is not None:
            pulumi.set(__self__, "oss_bucket_name", oss_bucket_name)
        if oss_object_name is not None:
            pulumi.set(__self__, "oss_object_name", oss_object_name)
        if skip_destroy is not None:
            pulumi.set(__self__, "skip_destroy", skip_destroy)
        if zip_file is not None:
            pulumi.set(__self__, "zip_file", zip_file)

    @property
    @pulumi.getter(name="compatibleRuntimes")
    def compatible_runtimes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of runtime environments that are supported by the layer. Valid values: `nodejs14`, `nodejs12`, `nodejs10`, `nodejs8`, `nodejs6`, `python3.9`, `python3`, `python2.7`, `java11`, `java8`, `php7.2`, `go1`,`dotnetcore2.1`, `custom`.
        """
        return pulumi.get(self, "compatible_runtimes")

    @compatible_runtimes.setter
    def compatible_runtimes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "compatible_runtimes", value)

    @property
    @pulumi.getter(name="layerName")
    def layer_name(self) -> pulumi.Input[str]:
        """
        The name of the layer.
        """
        return pulumi.get(self, "layer_name")

    @layer_name.setter
    def layer_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "layer_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the layer version.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ossBucketName")
    def oss_bucket_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OSS bucket that stores the ZIP package of the function code.
        """
        return pulumi.get(self, "oss_bucket_name")

    @oss_bucket_name.setter
    def oss_bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oss_bucket_name", value)

    @property
    @pulumi.getter(name="ossObjectName")
    def oss_object_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OSS object (ZIP package) that contains the function code.
        """
        return pulumi.get(self, "oss_object_name")

    @oss_object_name.setter
    def oss_object_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oss_object_name", value)

    @property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to retain the old version of a previously deployed Lambda Layer. Default is `false`. When this is not set to `true`, changing any of `compatible_runtimes`, `description`, `layer_name`, `oss_bucket_name`,  `oss_object_name`, or `zip_file` forces deletion of the existing layer version and creation of a new layer version.
        """
        return pulumi.get(self, "skip_destroy")

    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_destroy", value)

    @property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> Optional[pulumi.Input[str]]:
        """
        The ZIP package of the function code that is encoded in the Base64 format.

        > **NOTE:** `zip_file` and `oss_bucket_name`, `oss_object_name` cannot be used together.
        """
        return pulumi.get(self, "zip_file")

    @zip_file.setter
    def zip_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zip_file", value)


@pulumi.input_type
class _LayerVersionState:
    def __init__(__self__, *,
                 acl: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 code_check_sum: Optional[pulumi.Input[str]] = None,
                 compatible_runtimes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 layer_name: Optional[pulumi.Input[str]] = None,
                 oss_bucket_name: Optional[pulumi.Input[str]] = None,
                 oss_object_name: Optional[pulumi.Input[str]] = None,
                 skip_destroy: Optional[pulumi.Input[bool]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 zip_file: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LayerVersion resources.
        :param pulumi.Input[str] acl: The access mode of Layer Version.
        :param pulumi.Input[str] arn: The arn of Layer Version.
        :param pulumi.Input[str] code_check_sum: The checksum of the layer code package.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] compatible_runtimes: The list of runtime environments that are supported by the layer. Valid values: `nodejs14`, `nodejs12`, `nodejs10`, `nodejs8`, `nodejs6`, `python3.9`, `python3`, `python2.7`, `java11`, `java8`, `php7.2`, `go1`,`dotnetcore2.1`, `custom`.
        :param pulumi.Input[str] description: The description of the layer version.
        :param pulumi.Input[str] layer_name: The name of the layer.
        :param pulumi.Input[str] oss_bucket_name: The name of the OSS bucket that stores the ZIP package of the function code.
        :param pulumi.Input[str] oss_object_name: The name of the OSS object (ZIP package) that contains the function code.
        :param pulumi.Input[bool] skip_destroy: Whether to retain the old version of a previously deployed Lambda Layer. Default is `false`. When this is not set to `true`, changing any of `compatible_runtimes`, `description`, `layer_name`, `oss_bucket_name`,  `oss_object_name`, or `zip_file` forces deletion of the existing layer version and creation of a new layer version.
        :param pulumi.Input[str] version: The version of Layer Version.
        :param pulumi.Input[str] zip_file: The ZIP package of the function code that is encoded in the Base64 format.
               
               > **NOTE:** `zip_file` and `oss_bucket_name`, `oss_object_name` cannot be used together.
        """
        if acl is not None:
            pulumi.set(__self__, "acl", acl)
        if arn is not None:
            pulumi.set(__self__, "arn", arn)
        if code_check_sum is not None:
            pulumi.set(__self__, "code_check_sum", code_check_sum)
        if compatible_runtimes is not None:
            pulumi.set(__self__, "compatible_runtimes", compatible_runtimes)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if layer_name is not None:
            pulumi.set(__self__, "layer_name", layer_name)
        if oss_bucket_name is not None:
            pulumi.set(__self__, "oss_bucket_name", oss_bucket_name)
        if oss_object_name is not None:
            pulumi.set(__self__, "oss_object_name", oss_object_name)
        if skip_destroy is not None:
            pulumi.set(__self__, "skip_destroy", skip_destroy)
        if version is not None:
            pulumi.set(__self__, "version", version)
        if zip_file is not None:
            pulumi.set(__self__, "zip_file", zip_file)

    @property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input[str]]:
        """
        The access mode of Layer Version.
        """
        return pulumi.get(self, "acl")

    @acl.setter
    def acl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The arn of Layer Version.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="codeCheckSum")
    def code_check_sum(self) -> Optional[pulumi.Input[str]]:
        """
        The checksum of the layer code package.
        """
        return pulumi.get(self, "code_check_sum")

    @code_check_sum.setter
    def code_check_sum(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code_check_sum", value)

    @property
    @pulumi.getter(name="compatibleRuntimes")
    def compatible_runtimes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of runtime environments that are supported by the layer. Valid values: `nodejs14`, `nodejs12`, `nodejs10`, `nodejs8`, `nodejs6`, `python3.9`, `python3`, `python2.7`, `java11`, `java8`, `php7.2`, `go1`,`dotnetcore2.1`, `custom`.
        """
        return pulumi.get(self, "compatible_runtimes")

    @compatible_runtimes.setter
    def compatible_runtimes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "compatible_runtimes", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the layer version.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="layerName")
    def layer_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the layer.
        """
        return pulumi.get(self, "layer_name")

    @layer_name.setter
    def layer_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "layer_name", value)

    @property
    @pulumi.getter(name="ossBucketName")
    def oss_bucket_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OSS bucket that stores the ZIP package of the function code.
        """
        return pulumi.get(self, "oss_bucket_name")

    @oss_bucket_name.setter
    def oss_bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oss_bucket_name", value)

    @property
    @pulumi.getter(name="ossObjectName")
    def oss_object_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OSS object (ZIP package) that contains the function code.
        """
        return pulumi.get(self, "oss_object_name")

    @oss_object_name.setter
    def oss_object_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oss_object_name", value)

    @property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to retain the old version of a previously deployed Lambda Layer. Default is `false`. When this is not set to `true`, changing any of `compatible_runtimes`, `description`, `layer_name`, `oss_bucket_name`,  `oss_object_name`, or `zip_file` forces deletion of the existing layer version and creation of a new layer version.
        """
        return pulumi.get(self, "skip_destroy")

    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_destroy", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of Layer Version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> Optional[pulumi.Input[str]]:
        """
        The ZIP package of the function code that is encoded in the Base64 format.

        > **NOTE:** `zip_file` and `oss_bucket_name`, `oss_object_name` cannot be used together.
        """
        return pulumi.get(self, "zip_file")

    @zip_file.setter
    def zip_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zip_file", value)


class LayerVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compatible_runtimes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 layer_name: Optional[pulumi.Input[str]] = None,
                 oss_bucket_name: Optional[pulumi.Input[str]] = None,
                 oss_object_name: Optional[pulumi.Input[str]] = None,
                 skip_destroy: Optional[pulumi.Input[bool]] = None,
                 zip_file: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud
        import pulumi_random as random

        default = random.index.Integer("default",
            max=99999,
            min=10000)
        default_bucket = alicloud.oss.Bucket("default", bucket=f"terraform-example-{default['result']}")
        # If you upload the function by OSS Bucket, you need to specify path can't upload by content.
        default_bucket_object = alicloud.oss.BucketObject("default",
            bucket=default_bucket.id,
            key="index.py",
            content=\"\"\"import logging 
        def handler(event, context): 
        logger = logging.getLogger() 
        logger.info('hello world') 
        return 'hello world'\"\"\")
        example = alicloud.fc.LayerVersion("example",
            layer_name=f"terraform-example-{default['result']}",
            compatible_runtimes=["python2.7"],
            oss_bucket_name=default_bucket.bucket,
            oss_object_name=default_bucket_object.key)
        ```

        ## Import

        Function Compute Layer Version can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:fc/layerVersion:LayerVersion example my_function
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] compatible_runtimes: The list of runtime environments that are supported by the layer. Valid values: `nodejs14`, `nodejs12`, `nodejs10`, `nodejs8`, `nodejs6`, `python3.9`, `python3`, `python2.7`, `java11`, `java8`, `php7.2`, `go1`,`dotnetcore2.1`, `custom`.
        :param pulumi.Input[str] description: The description of the layer version.
        :param pulumi.Input[str] layer_name: The name of the layer.
        :param pulumi.Input[str] oss_bucket_name: The name of the OSS bucket that stores the ZIP package of the function code.
        :param pulumi.Input[str] oss_object_name: The name of the OSS object (ZIP package) that contains the function code.
        :param pulumi.Input[bool] skip_destroy: Whether to retain the old version of a previously deployed Lambda Layer. Default is `false`. When this is not set to `true`, changing any of `compatible_runtimes`, `description`, `layer_name`, `oss_bucket_name`,  `oss_object_name`, or `zip_file` forces deletion of the existing layer version and creation of a new layer version.
        :param pulumi.Input[str] zip_file: The ZIP package of the function code that is encoded in the Base64 format.
               
               > **NOTE:** `zip_file` and `oss_bucket_name`, `oss_object_name` cannot be used together.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LayerVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud
        import pulumi_random as random

        default = random.index.Integer("default",
            max=99999,
            min=10000)
        default_bucket = alicloud.oss.Bucket("default", bucket=f"terraform-example-{default['result']}")
        # If you upload the function by OSS Bucket, you need to specify path can't upload by content.
        default_bucket_object = alicloud.oss.BucketObject("default",
            bucket=default_bucket.id,
            key="index.py",
            content=\"\"\"import logging 
        def handler(event, context): 
        logger = logging.getLogger() 
        logger.info('hello world') 
        return 'hello world'\"\"\")
        example = alicloud.fc.LayerVersion("example",
            layer_name=f"terraform-example-{default['result']}",
            compatible_runtimes=["python2.7"],
            oss_bucket_name=default_bucket.bucket,
            oss_object_name=default_bucket_object.key)
        ```

        ## Import

        Function Compute Layer Version can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:fc/layerVersion:LayerVersion example my_function
        ```

        :param str resource_name: The name of the resource.
        :param LayerVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LayerVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compatible_runtimes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 layer_name: Optional[pulumi.Input[str]] = None,
                 oss_bucket_name: Optional[pulumi.Input[str]] = None,
                 oss_object_name: Optional[pulumi.Input[str]] = None,
                 skip_destroy: Optional[pulumi.Input[bool]] = None,
                 zip_file: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LayerVersionArgs.__new__(LayerVersionArgs)

            if compatible_runtimes is None and not opts.urn:
                raise TypeError("Missing required property 'compatible_runtimes'")
            __props__.__dict__["compatible_runtimes"] = compatible_runtimes
            __props__.__dict__["description"] = description
            if layer_name is None and not opts.urn:
                raise TypeError("Missing required property 'layer_name'")
            __props__.__dict__["layer_name"] = layer_name
            __props__.__dict__["oss_bucket_name"] = oss_bucket_name
            __props__.__dict__["oss_object_name"] = oss_object_name
            __props__.__dict__["skip_destroy"] = skip_destroy
            __props__.__dict__["zip_file"] = zip_file
            __props__.__dict__["acl"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["code_check_sum"] = None
            __props__.__dict__["version"] = None
        super(LayerVersion, __self__).__init__(
            'alicloud:fc/layerVersion:LayerVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            code_check_sum: Optional[pulumi.Input[str]] = None,
            compatible_runtimes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            layer_name: Optional[pulumi.Input[str]] = None,
            oss_bucket_name: Optional[pulumi.Input[str]] = None,
            oss_object_name: Optional[pulumi.Input[str]] = None,
            skip_destroy: Optional[pulumi.Input[bool]] = None,
            version: Optional[pulumi.Input[str]] = None,
            zip_file: Optional[pulumi.Input[str]] = None) -> 'LayerVersion':
        """
        Get an existing LayerVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl: The access mode of Layer Version.
        :param pulumi.Input[str] arn: The arn of Layer Version.
        :param pulumi.Input[str] code_check_sum: The checksum of the layer code package.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] compatible_runtimes: The list of runtime environments that are supported by the layer. Valid values: `nodejs14`, `nodejs12`, `nodejs10`, `nodejs8`, `nodejs6`, `python3.9`, `python3`, `python2.7`, `java11`, `java8`, `php7.2`, `go1`,`dotnetcore2.1`, `custom`.
        :param pulumi.Input[str] description: The description of the layer version.
        :param pulumi.Input[str] layer_name: The name of the layer.
        :param pulumi.Input[str] oss_bucket_name: The name of the OSS bucket that stores the ZIP package of the function code.
        :param pulumi.Input[str] oss_object_name: The name of the OSS object (ZIP package) that contains the function code.
        :param pulumi.Input[bool] skip_destroy: Whether to retain the old version of a previously deployed Lambda Layer. Default is `false`. When this is not set to `true`, changing any of `compatible_runtimes`, `description`, `layer_name`, `oss_bucket_name`,  `oss_object_name`, or `zip_file` forces deletion of the existing layer version and creation of a new layer version.
        :param pulumi.Input[str] version: The version of Layer Version.
        :param pulumi.Input[str] zip_file: The ZIP package of the function code that is encoded in the Base64 format.
               
               > **NOTE:** `zip_file` and `oss_bucket_name`, `oss_object_name` cannot be used together.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LayerVersionState.__new__(_LayerVersionState)

        __props__.__dict__["acl"] = acl
        __props__.__dict__["arn"] = arn
        __props__.__dict__["code_check_sum"] = code_check_sum
        __props__.__dict__["compatible_runtimes"] = compatible_runtimes
        __props__.__dict__["description"] = description
        __props__.__dict__["layer_name"] = layer_name
        __props__.__dict__["oss_bucket_name"] = oss_bucket_name
        __props__.__dict__["oss_object_name"] = oss_object_name
        __props__.__dict__["skip_destroy"] = skip_destroy
        __props__.__dict__["version"] = version
        __props__.__dict__["zip_file"] = zip_file
        return LayerVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def acl(self) -> pulumi.Output[str]:
        """
        The access mode of Layer Version.
        """
        return pulumi.get(self, "acl")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The arn of Layer Version.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="codeCheckSum")
    def code_check_sum(self) -> pulumi.Output[str]:
        """
        The checksum of the layer code package.
        """
        return pulumi.get(self, "code_check_sum")

    @property
    @pulumi.getter(name="compatibleRuntimes")
    def compatible_runtimes(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of runtime environments that are supported by the layer. Valid values: `nodejs14`, `nodejs12`, `nodejs10`, `nodejs8`, `nodejs6`, `python3.9`, `python3`, `python2.7`, `java11`, `java8`, `php7.2`, `go1`,`dotnetcore2.1`, `custom`.
        """
        return pulumi.get(self, "compatible_runtimes")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the layer version.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="layerName")
    def layer_name(self) -> pulumi.Output[str]:
        """
        The name of the layer.
        """
        return pulumi.get(self, "layer_name")

    @property
    @pulumi.getter(name="ossBucketName")
    def oss_bucket_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the OSS bucket that stores the ZIP package of the function code.
        """
        return pulumi.get(self, "oss_bucket_name")

    @property
    @pulumi.getter(name="ossObjectName")
    def oss_object_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the OSS object (ZIP package) that contains the function code.
        """
        return pulumi.get(self, "oss_object_name")

    @property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to retain the old version of a previously deployed Lambda Layer. Default is `false`. When this is not set to `true`, changing any of `compatible_runtimes`, `description`, `layer_name`, `oss_bucket_name`,  `oss_object_name`, or `zip_file` forces deletion of the existing layer version and creation of a new layer version.
        """
        return pulumi.get(self, "skip_destroy")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of Layer Version.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="zipFile")
    def zip_file(self) -> pulumi.Output[Optional[str]]:
        """
        The ZIP package of the function code that is encoded in the Base64 format.

        > **NOTE:** `zip_file` and `oss_bucket_name`, `oss_object_name` cannot be used together.
        """
        return pulumi.get(self, "zip_file")

