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

__all__ = ['AppTemplateArgs', 'AppTemplate']

@pulumi.input_type
class AppTemplateArgs:
    def __init__(__self__, *,
                 app_template_name: pulumi.Input[str],
                 component_lists: pulumi.Input[Sequence[pulumi.Input[str]]],
                 config_lists: Optional[pulumi.Input[Sequence[pulumi.Input['AppTemplateConfigListArgs']]]] = None,
                 integration_mode: Optional[pulumi.Input[str]] = None,
                 scene: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AppTemplate resource.
        :param pulumi.Input[str] app_template_name: The name of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] component_lists: List of components. Its element valid values: ["component.live","component.liveRecord","component.liveBeauty","component.rtc","component.rtcRecord","component.im","component.whiteboard","component.liveSecurity","component.chatSecurity"].
        :param pulumi.Input[Sequence[pulumi.Input['AppTemplateConfigListArgs']]] config_lists: Configuration list. It have several default configs after the resource is created. See the following `Block config_list`.
        :param pulumi.Input[str] integration_mode: Integration mode. Valid values:
               * paasSDK: Integrated SDK.
               * standardRoom: Model Room.
        :param pulumi.Input[str] scene: Application Template scenario. Valid values: ["business", "classroom"].
        """
        pulumi.set(__self__, "app_template_name", app_template_name)
        pulumi.set(__self__, "component_lists", component_lists)
        if config_lists is not None:
            pulumi.set(__self__, "config_lists", config_lists)
        if integration_mode is not None:
            pulumi.set(__self__, "integration_mode", integration_mode)
        if scene is not None:
            pulumi.set(__self__, "scene", scene)

    @property
    @pulumi.getter(name="appTemplateName")
    def app_template_name(self) -> pulumi.Input[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "app_template_name")

    @app_template_name.setter
    def app_template_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_template_name", value)

    @property
    @pulumi.getter(name="componentLists")
    def component_lists(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of components. Its element valid values: ["component.live","component.liveRecord","component.liveBeauty","component.rtc","component.rtcRecord","component.im","component.whiteboard","component.liveSecurity","component.chatSecurity"].
        """
        return pulumi.get(self, "component_lists")

    @component_lists.setter
    def component_lists(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "component_lists", value)

    @property
    @pulumi.getter(name="configLists")
    def config_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppTemplateConfigListArgs']]]]:
        """
        Configuration list. It have several default configs after the resource is created. See the following `Block config_list`.
        """
        return pulumi.get(self, "config_lists")

    @config_lists.setter
    def config_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppTemplateConfigListArgs']]]]):
        pulumi.set(self, "config_lists", value)

    @property
    @pulumi.getter(name="integrationMode")
    def integration_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Integration mode. Valid values:
        * paasSDK: Integrated SDK.
        * standardRoom: Model Room.
        """
        return pulumi.get(self, "integration_mode")

    @integration_mode.setter
    def integration_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_mode", value)

    @property
    @pulumi.getter
    def scene(self) -> Optional[pulumi.Input[str]]:
        """
        Application Template scenario. Valid values: ["business", "classroom"].
        """
        return pulumi.get(self, "scene")

    @scene.setter
    def scene(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scene", value)


@pulumi.input_type
class _AppTemplateState:
    def __init__(__self__, *,
                 app_template_name: Optional[pulumi.Input[str]] = None,
                 component_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 config_lists: Optional[pulumi.Input[Sequence[pulumi.Input['AppTemplateConfigListArgs']]]] = None,
                 integration_mode: Optional[pulumi.Input[str]] = None,
                 scene: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AppTemplate resources.
        :param pulumi.Input[str] app_template_name: The name of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] component_lists: List of components. Its element valid values: ["component.live","component.liveRecord","component.liveBeauty","component.rtc","component.rtcRecord","component.im","component.whiteboard","component.liveSecurity","component.chatSecurity"].
        :param pulumi.Input[Sequence[pulumi.Input['AppTemplateConfigListArgs']]] config_lists: Configuration list. It have several default configs after the resource is created. See the following `Block config_list`.
        :param pulumi.Input[str] integration_mode: Integration mode. Valid values:
               * paasSDK: Integrated SDK.
               * standardRoom: Model Room.
        :param pulumi.Input[str] scene: Application Template scenario. Valid values: ["business", "classroom"].
        :param pulumi.Input[str] status: Application template usage status.
        """
        if app_template_name is not None:
            pulumi.set(__self__, "app_template_name", app_template_name)
        if component_lists is not None:
            pulumi.set(__self__, "component_lists", component_lists)
        if config_lists is not None:
            pulumi.set(__self__, "config_lists", config_lists)
        if integration_mode is not None:
            pulumi.set(__self__, "integration_mode", integration_mode)
        if scene is not None:
            pulumi.set(__self__, "scene", scene)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="appTemplateName")
    def app_template_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "app_template_name")

    @app_template_name.setter
    def app_template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_template_name", value)

    @property
    @pulumi.getter(name="componentLists")
    def component_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of components. Its element valid values: ["component.live","component.liveRecord","component.liveBeauty","component.rtc","component.rtcRecord","component.im","component.whiteboard","component.liveSecurity","component.chatSecurity"].
        """
        return pulumi.get(self, "component_lists")

    @component_lists.setter
    def component_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "component_lists", value)

    @property
    @pulumi.getter(name="configLists")
    def config_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppTemplateConfigListArgs']]]]:
        """
        Configuration list. It have several default configs after the resource is created. See the following `Block config_list`.
        """
        return pulumi.get(self, "config_lists")

    @config_lists.setter
    def config_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppTemplateConfigListArgs']]]]):
        pulumi.set(self, "config_lists", value)

    @property
    @pulumi.getter(name="integrationMode")
    def integration_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Integration mode. Valid values:
        * paasSDK: Integrated SDK.
        * standardRoom: Model Room.
        """
        return pulumi.get(self, "integration_mode")

    @integration_mode.setter
    def integration_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_mode", value)

    @property
    @pulumi.getter
    def scene(self) -> Optional[pulumi.Input[str]]:
        """
        Application Template scenario. Valid values: ["business", "classroom"].
        """
        return pulumi.get(self, "scene")

    @scene.setter
    def scene(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scene", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Application template usage status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class AppTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_template_name: Optional[pulumi.Input[str]] = None,
                 component_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 config_lists: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTemplateConfigListArgs']]]]] = None,
                 integration_mode: Optional[pulumi.Input[str]] = None,
                 scene: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Apsara Agile Live (IMP) App Template resource.

        For information about Apsara Agile Live (IMP) App Template and how to use it, see [What is App Template](https://help.aliyun.com/document_detail/270121.html).

        > **NOTE:** Available in v1.137.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.imp.AppTemplate("example",
            app_template_name="example_value",
            component_lists=[
                "component.live",
                "component.liveRecord",
            ],
            integration_mode="paasSDK",
            scene="business")
        ```

        ## Import

        Apsara Agile Live (IMP) App Template can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:imp/appTemplate:AppTemplate example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_template_name: The name of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] component_lists: List of components. Its element valid values: ["component.live","component.liveRecord","component.liveBeauty","component.rtc","component.rtcRecord","component.im","component.whiteboard","component.liveSecurity","component.chatSecurity"].
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTemplateConfigListArgs']]]] config_lists: Configuration list. It have several default configs after the resource is created. See the following `Block config_list`.
        :param pulumi.Input[str] integration_mode: Integration mode. Valid values:
               * paasSDK: Integrated SDK.
               * standardRoom: Model Room.
        :param pulumi.Input[str] scene: Application Template scenario. Valid values: ["business", "classroom"].
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Apsara Agile Live (IMP) App Template resource.

        For information about Apsara Agile Live (IMP) App Template and how to use it, see [What is App Template](https://help.aliyun.com/document_detail/270121.html).

        > **NOTE:** Available in v1.137.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.imp.AppTemplate("example",
            app_template_name="example_value",
            component_lists=[
                "component.live",
                "component.liveRecord",
            ],
            integration_mode="paasSDK",
            scene="business")
        ```

        ## Import

        Apsara Agile Live (IMP) App Template can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:imp/appTemplate:AppTemplate example <id>
        ```

        :param str resource_name: The name of the resource.
        :param AppTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_template_name: Optional[pulumi.Input[str]] = None,
                 component_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 config_lists: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTemplateConfigListArgs']]]]] = None,
                 integration_mode: Optional[pulumi.Input[str]] = None,
                 scene: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppTemplateArgs.__new__(AppTemplateArgs)

            if app_template_name is None and not opts.urn:
                raise TypeError("Missing required property 'app_template_name'")
            __props__.__dict__["app_template_name"] = app_template_name
            if component_lists is None and not opts.urn:
                raise TypeError("Missing required property 'component_lists'")
            __props__.__dict__["component_lists"] = component_lists
            __props__.__dict__["config_lists"] = config_lists
            __props__.__dict__["integration_mode"] = integration_mode
            __props__.__dict__["scene"] = scene
            __props__.__dict__["status"] = None
        super(AppTemplate, __self__).__init__(
            'alicloud:imp/appTemplate:AppTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_template_name: Optional[pulumi.Input[str]] = None,
            component_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            config_lists: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTemplateConfigListArgs']]]]] = None,
            integration_mode: Optional[pulumi.Input[str]] = None,
            scene: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'AppTemplate':
        """
        Get an existing AppTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_template_name: The name of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] component_lists: List of components. Its element valid values: ["component.live","component.liveRecord","component.liveBeauty","component.rtc","component.rtcRecord","component.im","component.whiteboard","component.liveSecurity","component.chatSecurity"].
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AppTemplateConfigListArgs']]]] config_lists: Configuration list. It have several default configs after the resource is created. See the following `Block config_list`.
        :param pulumi.Input[str] integration_mode: Integration mode. Valid values:
               * paasSDK: Integrated SDK.
               * standardRoom: Model Room.
        :param pulumi.Input[str] scene: Application Template scenario. Valid values: ["business", "classroom"].
        :param pulumi.Input[str] status: Application template usage status.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppTemplateState.__new__(_AppTemplateState)

        __props__.__dict__["app_template_name"] = app_template_name
        __props__.__dict__["component_lists"] = component_lists
        __props__.__dict__["config_lists"] = config_lists
        __props__.__dict__["integration_mode"] = integration_mode
        __props__.__dict__["scene"] = scene
        __props__.__dict__["status"] = status
        return AppTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appTemplateName")
    def app_template_name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "app_template_name")

    @property
    @pulumi.getter(name="componentLists")
    def component_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        List of components. Its element valid values: ["component.live","component.liveRecord","component.liveBeauty","component.rtc","component.rtcRecord","component.im","component.whiteboard","component.liveSecurity","component.chatSecurity"].
        """
        return pulumi.get(self, "component_lists")

    @property
    @pulumi.getter(name="configLists")
    def config_lists(self) -> pulumi.Output[Sequence['outputs.AppTemplateConfigList']]:
        """
        Configuration list. It have several default configs after the resource is created. See the following `Block config_list`.
        """
        return pulumi.get(self, "config_lists")

    @property
    @pulumi.getter(name="integrationMode")
    def integration_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Integration mode. Valid values:
        * paasSDK: Integrated SDK.
        * standardRoom: Model Room.
        """
        return pulumi.get(self, "integration_mode")

    @property
    @pulumi.getter
    def scene(self) -> pulumi.Output[Optional[str]]:
        """
        Application Template scenario. Valid values: ["business", "classroom"].
        """
        return pulumi.get(self, "scene")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Application template usage status.
        """
        return pulumi.get(self, "status")

