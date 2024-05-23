# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TransitRouterVbrAttachmentArgs', 'TransitRouterVbrAttachment']

@pulumi.input_type
class TransitRouterVbrAttachmentArgs:
    def __init__(__self__, *,
                 cen_id: pulumi.Input[str],
                 vbr_id: pulumi.Input[str],
                 auto_publish_route_enabled: Optional[pulumi.Input[bool]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 route_table_association_enabled: Optional[pulumi.Input[bool]] = None,
                 route_table_propagation_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 transit_router_attachment_description: Optional[pulumi.Input[str]] = None,
                 transit_router_attachment_name: Optional[pulumi.Input[str]] = None,
                 transit_router_id: Optional[pulumi.Input[str]] = None,
                 vbr_owner_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TransitRouterVbrAttachment resource.
        :param pulumi.Input[str] cen_id: The ID of the CEN.
        :param pulumi.Input[str] vbr_id: The ID of the VBR.
        :param pulumi.Input[bool] auto_publish_route_enabled: Auto publish route enabled.Default value is `false`.
        :param pulumi.Input[bool] dry_run: The dry run.
        :param pulumi.Input[str] resource_type: The resource type of the transit router vbr attachment.  Valid values: `VPC`, `CCN`, `VBR`, `TR`.
               
               ->**NOTE:** Ensure that the vbr is not used in Express Connect.
        :param pulumi.Input[bool] route_table_association_enabled: Whether to enabled route table association. The system default value is `true`.
        :param pulumi.Input[bool] route_table_propagation_enabled: Whether to enabled route table propagation. The system default value is `true`.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] transit_router_attachment_description: The description of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_attachment_name: The name of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_id: The ID of the transit router.
        :param pulumi.Input[str] vbr_owner_id: The owner id of the transit router vbr attachment.
        """
        pulumi.set(__self__, "cen_id", cen_id)
        pulumi.set(__self__, "vbr_id", vbr_id)
        if auto_publish_route_enabled is not None:
            pulumi.set(__self__, "auto_publish_route_enabled", auto_publish_route_enabled)
        if dry_run is not None:
            pulumi.set(__self__, "dry_run", dry_run)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)
        if route_table_association_enabled is not None:
            pulumi.set(__self__, "route_table_association_enabled", route_table_association_enabled)
        if route_table_propagation_enabled is not None:
            pulumi.set(__self__, "route_table_propagation_enabled", route_table_propagation_enabled)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if transit_router_attachment_description is not None:
            pulumi.set(__self__, "transit_router_attachment_description", transit_router_attachment_description)
        if transit_router_attachment_name is not None:
            pulumi.set(__self__, "transit_router_attachment_name", transit_router_attachment_name)
        if transit_router_id is not None:
            pulumi.set(__self__, "transit_router_id", transit_router_id)
        if vbr_owner_id is not None:
            pulumi.set(__self__, "vbr_owner_id", vbr_owner_id)

    @property
    @pulumi.getter(name="cenId")
    def cen_id(self) -> pulumi.Input[str]:
        """
        The ID of the CEN.
        """
        return pulumi.get(self, "cen_id")

    @cen_id.setter
    def cen_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cen_id", value)

    @property
    @pulumi.getter(name="vbrId")
    def vbr_id(self) -> pulumi.Input[str]:
        """
        The ID of the VBR.
        """
        return pulumi.get(self, "vbr_id")

    @vbr_id.setter
    def vbr_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vbr_id", value)

    @property
    @pulumi.getter(name="autoPublishRouteEnabled")
    def auto_publish_route_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Auto publish route enabled.Default value is `false`.
        """
        return pulumi.get(self, "auto_publish_route_enabled")

    @auto_publish_route_enabled.setter
    def auto_publish_route_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_publish_route_enabled", value)

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> Optional[pulumi.Input[bool]]:
        """
        The dry run.
        """
        return pulumi.get(self, "dry_run")

    @dry_run.setter
    def dry_run(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dry_run", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        The resource type of the transit router vbr attachment.  Valid values: `VPC`, `CCN`, `VBR`, `TR`.

        ->**NOTE:** Ensure that the vbr is not used in Express Connect.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter(name="routeTableAssociationEnabled")
    def route_table_association_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enabled route table association. The system default value is `true`.
        """
        return pulumi.get(self, "route_table_association_enabled")

    @route_table_association_enabled.setter
    def route_table_association_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "route_table_association_enabled", value)

    @property
    @pulumi.getter(name="routeTablePropagationEnabled")
    def route_table_propagation_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enabled route table propagation. The system default value is `true`.
        """
        return pulumi.get(self, "route_table_propagation_enabled")

    @route_table_propagation_enabled.setter
    def route_table_propagation_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "route_table_propagation_enabled", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="transitRouterAttachmentDescription")
    def transit_router_attachment_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the transit router vbr attachment.
        """
        return pulumi.get(self, "transit_router_attachment_description")

    @transit_router_attachment_description.setter
    def transit_router_attachment_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_router_attachment_description", value)

    @property
    @pulumi.getter(name="transitRouterAttachmentName")
    def transit_router_attachment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the transit router vbr attachment.
        """
        return pulumi.get(self, "transit_router_attachment_name")

    @transit_router_attachment_name.setter
    def transit_router_attachment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_router_attachment_name", value)

    @property
    @pulumi.getter(name="transitRouterId")
    def transit_router_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the transit router.
        """
        return pulumi.get(self, "transit_router_id")

    @transit_router_id.setter
    def transit_router_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_router_id", value)

    @property
    @pulumi.getter(name="vbrOwnerId")
    def vbr_owner_id(self) -> Optional[pulumi.Input[str]]:
        """
        The owner id of the transit router vbr attachment.
        """
        return pulumi.get(self, "vbr_owner_id")

    @vbr_owner_id.setter
    def vbr_owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vbr_owner_id", value)


@pulumi.input_type
class _TransitRouterVbrAttachmentState:
    def __init__(__self__, *,
                 auto_publish_route_enabled: Optional[pulumi.Input[bool]] = None,
                 cen_id: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 route_table_association_enabled: Optional[pulumi.Input[bool]] = None,
                 route_table_propagation_enabled: Optional[pulumi.Input[bool]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 transit_router_attachment_description: Optional[pulumi.Input[str]] = None,
                 transit_router_attachment_id: Optional[pulumi.Input[str]] = None,
                 transit_router_attachment_name: Optional[pulumi.Input[str]] = None,
                 transit_router_id: Optional[pulumi.Input[str]] = None,
                 vbr_id: Optional[pulumi.Input[str]] = None,
                 vbr_owner_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TransitRouterVbrAttachment resources.
        :param pulumi.Input[bool] auto_publish_route_enabled: Auto publish route enabled.Default value is `false`.
        :param pulumi.Input[str] cen_id: The ID of the CEN.
        :param pulumi.Input[bool] dry_run: The dry run.
        :param pulumi.Input[str] resource_type: The resource type of the transit router vbr attachment.  Valid values: `VPC`, `CCN`, `VBR`, `TR`.
               
               ->**NOTE:** Ensure that the vbr is not used in Express Connect.
        :param pulumi.Input[bool] route_table_association_enabled: Whether to enabled route table association. The system default value is `true`.
        :param pulumi.Input[bool] route_table_propagation_enabled: Whether to enabled route table propagation. The system default value is `true`.
        :param pulumi.Input[str] status: The associating status of the network.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] transit_router_attachment_description: The description of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_attachment_id: The id of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_attachment_name: The name of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_id: The ID of the transit router.
        :param pulumi.Input[str] vbr_id: The ID of the VBR.
        :param pulumi.Input[str] vbr_owner_id: The owner id of the transit router vbr attachment.
        """
        if auto_publish_route_enabled is not None:
            pulumi.set(__self__, "auto_publish_route_enabled", auto_publish_route_enabled)
        if cen_id is not None:
            pulumi.set(__self__, "cen_id", cen_id)
        if dry_run is not None:
            pulumi.set(__self__, "dry_run", dry_run)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)
        if route_table_association_enabled is not None:
            pulumi.set(__self__, "route_table_association_enabled", route_table_association_enabled)
        if route_table_propagation_enabled is not None:
            pulumi.set(__self__, "route_table_propagation_enabled", route_table_propagation_enabled)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if transit_router_attachment_description is not None:
            pulumi.set(__self__, "transit_router_attachment_description", transit_router_attachment_description)
        if transit_router_attachment_id is not None:
            pulumi.set(__self__, "transit_router_attachment_id", transit_router_attachment_id)
        if transit_router_attachment_name is not None:
            pulumi.set(__self__, "transit_router_attachment_name", transit_router_attachment_name)
        if transit_router_id is not None:
            pulumi.set(__self__, "transit_router_id", transit_router_id)
        if vbr_id is not None:
            pulumi.set(__self__, "vbr_id", vbr_id)
        if vbr_owner_id is not None:
            pulumi.set(__self__, "vbr_owner_id", vbr_owner_id)

    @property
    @pulumi.getter(name="autoPublishRouteEnabled")
    def auto_publish_route_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Auto publish route enabled.Default value is `false`.
        """
        return pulumi.get(self, "auto_publish_route_enabled")

    @auto_publish_route_enabled.setter
    def auto_publish_route_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_publish_route_enabled", value)

    @property
    @pulumi.getter(name="cenId")
    def cen_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the CEN.
        """
        return pulumi.get(self, "cen_id")

    @cen_id.setter
    def cen_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cen_id", value)

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> Optional[pulumi.Input[bool]]:
        """
        The dry run.
        """
        return pulumi.get(self, "dry_run")

    @dry_run.setter
    def dry_run(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dry_run", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        The resource type of the transit router vbr attachment.  Valid values: `VPC`, `CCN`, `VBR`, `TR`.

        ->**NOTE:** Ensure that the vbr is not used in Express Connect.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter(name="routeTableAssociationEnabled")
    def route_table_association_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enabled route table association. The system default value is `true`.
        """
        return pulumi.get(self, "route_table_association_enabled")

    @route_table_association_enabled.setter
    def route_table_association_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "route_table_association_enabled", value)

    @property
    @pulumi.getter(name="routeTablePropagationEnabled")
    def route_table_propagation_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to enabled route table propagation. The system default value is `true`.
        """
        return pulumi.get(self, "route_table_propagation_enabled")

    @route_table_propagation_enabled.setter
    def route_table_propagation_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "route_table_propagation_enabled", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The associating status of the network.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="transitRouterAttachmentDescription")
    def transit_router_attachment_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the transit router vbr attachment.
        """
        return pulumi.get(self, "transit_router_attachment_description")

    @transit_router_attachment_description.setter
    def transit_router_attachment_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_router_attachment_description", value)

    @property
    @pulumi.getter(name="transitRouterAttachmentId")
    def transit_router_attachment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the transit router vbr attachment.
        """
        return pulumi.get(self, "transit_router_attachment_id")

    @transit_router_attachment_id.setter
    def transit_router_attachment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_router_attachment_id", value)

    @property
    @pulumi.getter(name="transitRouterAttachmentName")
    def transit_router_attachment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the transit router vbr attachment.
        """
        return pulumi.get(self, "transit_router_attachment_name")

    @transit_router_attachment_name.setter
    def transit_router_attachment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_router_attachment_name", value)

    @property
    @pulumi.getter(name="transitRouterId")
    def transit_router_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the transit router.
        """
        return pulumi.get(self, "transit_router_id")

    @transit_router_id.setter
    def transit_router_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transit_router_id", value)

    @property
    @pulumi.getter(name="vbrId")
    def vbr_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the VBR.
        """
        return pulumi.get(self, "vbr_id")

    @vbr_id.setter
    def vbr_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vbr_id", value)

    @property
    @pulumi.getter(name="vbrOwnerId")
    def vbr_owner_id(self) -> Optional[pulumi.Input[str]]:
        """
        The owner id of the transit router vbr attachment.
        """
        return pulumi.get(self, "vbr_owner_id")

    @vbr_owner_id.setter
    def vbr_owner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vbr_owner_id", value)


class TransitRouterVbrAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_publish_route_enabled: Optional[pulumi.Input[bool]] = None,
                 cen_id: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 route_table_association_enabled: Optional[pulumi.Input[bool]] = None,
                 route_table_propagation_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 transit_router_attachment_description: Optional[pulumi.Input[str]] = None,
                 transit_router_attachment_name: Optional[pulumi.Input[str]] = None,
                 transit_router_id: Optional[pulumi.Input[str]] = None,
                 vbr_id: Optional[pulumi.Input[str]] = None,
                 vbr_owner_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a CEN transit router VBR attachment resource that associate the VBR with the CEN instance.[What is Cen Transit Router VBR Attachment](https://www.alibabacloud.com/help/en/cen/developer-reference/api-cbn-2017-09-12-createtransitroutervbrattachment)

        > **NOTE:** Available since v1.126.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default = alicloud.cen.Instance("default",
            cen_instance_name=name,
            protection_level="REDUCED")
        default_transit_router = alicloud.cen.TransitRouter("default", cen_id=default.id)
        name_regex = alicloud.expressconnect.get_physical_connections(name_regex="^preserved-NODELETING")
        default_virtual_border_router = alicloud.expressconnect.VirtualBorderRouter("default",
            local_gateway_ip="10.0.0.1",
            peer_gateway_ip="10.0.0.2",
            peering_subnet_mask="255.255.255.252",
            physical_connection_id=name_regex.connections[0].id,
            virtual_border_router_name=name,
            vlan_id=2420,
            min_rx_interval=1000,
            min_tx_interval=1000,
            detect_multiplier=10)
        default_transit_router_vbr_attachment = alicloud.cen.TransitRouterVbrAttachment("default",
            transit_router_id=default_transit_router.transit_router_id,
            transit_router_attachment_name="example",
            transit_router_attachment_description="example",
            vbr_id=default_virtual_border_router.id,
            cen_id=default.id)
        ```

        ## Import

        CEN transit router VBR attachment can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cen/transitRouterVbrAttachment:TransitRouterVbrAttachment example tr-********:tr-attach-********
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_publish_route_enabled: Auto publish route enabled.Default value is `false`.
        :param pulumi.Input[str] cen_id: The ID of the CEN.
        :param pulumi.Input[bool] dry_run: The dry run.
        :param pulumi.Input[str] resource_type: The resource type of the transit router vbr attachment.  Valid values: `VPC`, `CCN`, `VBR`, `TR`.
               
               ->**NOTE:** Ensure that the vbr is not used in Express Connect.
        :param pulumi.Input[bool] route_table_association_enabled: Whether to enabled route table association. The system default value is `true`.
        :param pulumi.Input[bool] route_table_propagation_enabled: Whether to enabled route table propagation. The system default value is `true`.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] transit_router_attachment_description: The description of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_attachment_name: The name of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_id: The ID of the transit router.
        :param pulumi.Input[str] vbr_id: The ID of the VBR.
        :param pulumi.Input[str] vbr_owner_id: The owner id of the transit router vbr attachment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TransitRouterVbrAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a CEN transit router VBR attachment resource that associate the VBR with the CEN instance.[What is Cen Transit Router VBR Attachment](https://www.alibabacloud.com/help/en/cen/developer-reference/api-cbn-2017-09-12-createtransitroutervbrattachment)

        > **NOTE:** Available since v1.126.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraform-example"
        default = alicloud.cen.Instance("default",
            cen_instance_name=name,
            protection_level="REDUCED")
        default_transit_router = alicloud.cen.TransitRouter("default", cen_id=default.id)
        name_regex = alicloud.expressconnect.get_physical_connections(name_regex="^preserved-NODELETING")
        default_virtual_border_router = alicloud.expressconnect.VirtualBorderRouter("default",
            local_gateway_ip="10.0.0.1",
            peer_gateway_ip="10.0.0.2",
            peering_subnet_mask="255.255.255.252",
            physical_connection_id=name_regex.connections[0].id,
            virtual_border_router_name=name,
            vlan_id=2420,
            min_rx_interval=1000,
            min_tx_interval=1000,
            detect_multiplier=10)
        default_transit_router_vbr_attachment = alicloud.cen.TransitRouterVbrAttachment("default",
            transit_router_id=default_transit_router.transit_router_id,
            transit_router_attachment_name="example",
            transit_router_attachment_description="example",
            vbr_id=default_virtual_border_router.id,
            cen_id=default.id)
        ```

        ## Import

        CEN transit router VBR attachment can be imported using the id, e.g.

        ```sh
        $ pulumi import alicloud:cen/transitRouterVbrAttachment:TransitRouterVbrAttachment example tr-********:tr-attach-********
        ```

        :param str resource_name: The name of the resource.
        :param TransitRouterVbrAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransitRouterVbrAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_publish_route_enabled: Optional[pulumi.Input[bool]] = None,
                 cen_id: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 route_table_association_enabled: Optional[pulumi.Input[bool]] = None,
                 route_table_propagation_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 transit_router_attachment_description: Optional[pulumi.Input[str]] = None,
                 transit_router_attachment_name: Optional[pulumi.Input[str]] = None,
                 transit_router_id: Optional[pulumi.Input[str]] = None,
                 vbr_id: Optional[pulumi.Input[str]] = None,
                 vbr_owner_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TransitRouterVbrAttachmentArgs.__new__(TransitRouterVbrAttachmentArgs)

            __props__.__dict__["auto_publish_route_enabled"] = auto_publish_route_enabled
            if cen_id is None and not opts.urn:
                raise TypeError("Missing required property 'cen_id'")
            __props__.__dict__["cen_id"] = cen_id
            __props__.__dict__["dry_run"] = dry_run
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["route_table_association_enabled"] = route_table_association_enabled
            __props__.__dict__["route_table_propagation_enabled"] = route_table_propagation_enabled
            __props__.__dict__["tags"] = tags
            __props__.__dict__["transit_router_attachment_description"] = transit_router_attachment_description
            __props__.__dict__["transit_router_attachment_name"] = transit_router_attachment_name
            __props__.__dict__["transit_router_id"] = transit_router_id
            if vbr_id is None and not opts.urn:
                raise TypeError("Missing required property 'vbr_id'")
            __props__.__dict__["vbr_id"] = vbr_id
            __props__.__dict__["vbr_owner_id"] = vbr_owner_id
            __props__.__dict__["status"] = None
            __props__.__dict__["transit_router_attachment_id"] = None
        super(TransitRouterVbrAttachment, __self__).__init__(
            'alicloud:cen/transitRouterVbrAttachment:TransitRouterVbrAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_publish_route_enabled: Optional[pulumi.Input[bool]] = None,
            cen_id: Optional[pulumi.Input[str]] = None,
            dry_run: Optional[pulumi.Input[bool]] = None,
            resource_type: Optional[pulumi.Input[str]] = None,
            route_table_association_enabled: Optional[pulumi.Input[bool]] = None,
            route_table_propagation_enabled: Optional[pulumi.Input[bool]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            transit_router_attachment_description: Optional[pulumi.Input[str]] = None,
            transit_router_attachment_id: Optional[pulumi.Input[str]] = None,
            transit_router_attachment_name: Optional[pulumi.Input[str]] = None,
            transit_router_id: Optional[pulumi.Input[str]] = None,
            vbr_id: Optional[pulumi.Input[str]] = None,
            vbr_owner_id: Optional[pulumi.Input[str]] = None) -> 'TransitRouterVbrAttachment':
        """
        Get an existing TransitRouterVbrAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_publish_route_enabled: Auto publish route enabled.Default value is `false`.
        :param pulumi.Input[str] cen_id: The ID of the CEN.
        :param pulumi.Input[bool] dry_run: The dry run.
        :param pulumi.Input[str] resource_type: The resource type of the transit router vbr attachment.  Valid values: `VPC`, `CCN`, `VBR`, `TR`.
               
               ->**NOTE:** Ensure that the vbr is not used in Express Connect.
        :param pulumi.Input[bool] route_table_association_enabled: Whether to enabled route table association. The system default value is `true`.
        :param pulumi.Input[bool] route_table_propagation_enabled: Whether to enabled route table propagation. The system default value is `true`.
        :param pulumi.Input[str] status: The associating status of the network.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] transit_router_attachment_description: The description of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_attachment_id: The id of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_attachment_name: The name of the transit router vbr attachment.
        :param pulumi.Input[str] transit_router_id: The ID of the transit router.
        :param pulumi.Input[str] vbr_id: The ID of the VBR.
        :param pulumi.Input[str] vbr_owner_id: The owner id of the transit router vbr attachment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TransitRouterVbrAttachmentState.__new__(_TransitRouterVbrAttachmentState)

        __props__.__dict__["auto_publish_route_enabled"] = auto_publish_route_enabled
        __props__.__dict__["cen_id"] = cen_id
        __props__.__dict__["dry_run"] = dry_run
        __props__.__dict__["resource_type"] = resource_type
        __props__.__dict__["route_table_association_enabled"] = route_table_association_enabled
        __props__.__dict__["route_table_propagation_enabled"] = route_table_propagation_enabled
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        __props__.__dict__["transit_router_attachment_description"] = transit_router_attachment_description
        __props__.__dict__["transit_router_attachment_id"] = transit_router_attachment_id
        __props__.__dict__["transit_router_attachment_name"] = transit_router_attachment_name
        __props__.__dict__["transit_router_id"] = transit_router_id
        __props__.__dict__["vbr_id"] = vbr_id
        __props__.__dict__["vbr_owner_id"] = vbr_owner_id
        return TransitRouterVbrAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoPublishRouteEnabled")
    def auto_publish_route_enabled(self) -> pulumi.Output[bool]:
        """
        Auto publish route enabled.Default value is `false`.
        """
        return pulumi.get(self, "auto_publish_route_enabled")

    @property
    @pulumi.getter(name="cenId")
    def cen_id(self) -> pulumi.Output[str]:
        """
        The ID of the CEN.
        """
        return pulumi.get(self, "cen_id")

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> pulumi.Output[Optional[bool]]:
        """
        The dry run.
        """
        return pulumi.get(self, "dry_run")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[Optional[str]]:
        """
        The resource type of the transit router vbr attachment.  Valid values: `VPC`, `CCN`, `VBR`, `TR`.

        ->**NOTE:** Ensure that the vbr is not used in Express Connect.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="routeTableAssociationEnabled")
    def route_table_association_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enabled route table association. The system default value is `true`.
        """
        return pulumi.get(self, "route_table_association_enabled")

    @property
    @pulumi.getter(name="routeTablePropagationEnabled")
    def route_table_propagation_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enabled route table propagation. The system default value is `true`.
        """
        return pulumi.get(self, "route_table_propagation_enabled")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The associating status of the network.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transitRouterAttachmentDescription")
    def transit_router_attachment_description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the transit router vbr attachment.
        """
        return pulumi.get(self, "transit_router_attachment_description")

    @property
    @pulumi.getter(name="transitRouterAttachmentId")
    def transit_router_attachment_id(self) -> pulumi.Output[str]:
        """
        The id of the transit router vbr attachment.
        """
        return pulumi.get(self, "transit_router_attachment_id")

    @property
    @pulumi.getter(name="transitRouterAttachmentName")
    def transit_router_attachment_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the transit router vbr attachment.
        """
        return pulumi.get(self, "transit_router_attachment_name")

    @property
    @pulumi.getter(name="transitRouterId")
    def transit_router_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the transit router.
        """
        return pulumi.get(self, "transit_router_id")

    @property
    @pulumi.getter(name="vbrId")
    def vbr_id(self) -> pulumi.Output[str]:
        """
        The ID of the VBR.
        """
        return pulumi.get(self, "vbr_id")

    @property
    @pulumi.getter(name="vbrOwnerId")
    def vbr_owner_id(self) -> pulumi.Output[str]:
        """
        The owner id of the transit router vbr attachment.
        """
        return pulumi.get(self, "vbr_owner_id")

