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

__all__ = [
    'GetNasFileSystemsResult',
    'AwaitableGetNasFileSystemsResult',
    'get_nas_file_systems',
    'get_nas_file_systems_output',
]

@pulumi.output_type
class GetNasFileSystemsResult:
    """
    A collection of values returned by getNasFileSystems.
    """
    def __init__(__self__, id=None, ids=None, name_regex=None, names=None, office_site_id=None, output_file=None, status=None, systems=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if office_site_id and not isinstance(office_site_id, str):
            raise TypeError("Expected argument 'office_site_id' to be a str")
        pulumi.set(__self__, "office_site_id", office_site_id)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if systems and not isinstance(systems, list):
            raise TypeError("Expected argument 'systems' to be a list")
        pulumi.set(__self__, "systems", systems)

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
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="officeSiteId")
    def office_site_id(self) -> Optional[str]:
        return pulumi.get(self, "office_site_id")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def systems(self) -> Sequence['outputs.GetNasFileSystemsSystemResult']:
        return pulumi.get(self, "systems")


class AwaitableGetNasFileSystemsResult(GetNasFileSystemsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNasFileSystemsResult(
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            office_site_id=self.office_site_id,
            output_file=self.output_file,
            status=self.status,
            systems=self.systems)


def get_nas_file_systems(ids: Optional[Sequence[str]] = None,
                         name_regex: Optional[str] = None,
                         office_site_id: Optional[str] = None,
                         output_file: Optional[str] = None,
                         status: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNasFileSystemsResult:
    """
    This data source provides the Ecd Nas File Systems of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.141.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.eds.SimpleOfficeSite("default",
        cidr_block="172.16.0.0/12",
        desktop_access_type="Internet",
        office_site_name="your_office_site_name",
        enable_internet_access=False)
    default_nas_file_system = alicloud.eds.NasFileSystem("default",
        description="your_description",
        office_site_id=default.id,
        nas_file_system_name="your_nas_file_system_name")
    ids = alicloud.eds.get_nas_file_systems()
    pulumi.export("ecdNasFileSystemId1", ids.systems[0].id)
    name_regex = default_nas_file_system.nas_file_system_name.apply(lambda nas_file_system_name: alicloud.eds.get_nas_file_systems_output(name_regex=nas_file_system_name))
    pulumi.export("ecdNasFileSystemId2", name_regex.systems[0].id)
    ```


    :param Sequence[str] ids: A list of Nas File System IDs.
    :param str name_regex: A regex string to filter results by Nas File System name.
    :param str office_site_id: The ID of office site.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of nas file system. Valid values: `Pending`, `Running`, `Stopped`,`Deleting`, `Deleted`, `Invalid`.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['officeSiteId'] = office_site_id
    __args__['outputFile'] = output_file
    __args__['status'] = status
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('alicloud:eds/getNasFileSystems:getNasFileSystems', __args__, opts=opts, typ=GetNasFileSystemsResult).value

    return AwaitableGetNasFileSystemsResult(
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        name_regex=pulumi.get(__ret__, 'name_regex'),
        names=pulumi.get(__ret__, 'names'),
        office_site_id=pulumi.get(__ret__, 'office_site_id'),
        output_file=pulumi.get(__ret__, 'output_file'),
        status=pulumi.get(__ret__, 'status'),
        systems=pulumi.get(__ret__, 'systems'))


@_utilities.lift_output_func(get_nas_file_systems)
def get_nas_file_systems_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                office_site_id: Optional[pulumi.Input[Optional[str]]] = None,
                                output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                status: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNasFileSystemsResult]:
    """
    This data source provides the Ecd Nas File Systems of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.141.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.eds.SimpleOfficeSite("default",
        cidr_block="172.16.0.0/12",
        desktop_access_type="Internet",
        office_site_name="your_office_site_name",
        enable_internet_access=False)
    default_nas_file_system = alicloud.eds.NasFileSystem("default",
        description="your_description",
        office_site_id=default.id,
        nas_file_system_name="your_nas_file_system_name")
    ids = alicloud.eds.get_nas_file_systems()
    pulumi.export("ecdNasFileSystemId1", ids.systems[0].id)
    name_regex = default_nas_file_system.nas_file_system_name.apply(lambda nas_file_system_name: alicloud.eds.get_nas_file_systems_output(name_regex=nas_file_system_name))
    pulumi.export("ecdNasFileSystemId2", name_regex.systems[0].id)
    ```


    :param Sequence[str] ids: A list of Nas File System IDs.
    :param str name_regex: A regex string to filter results by Nas File System name.
    :param str office_site_id: The ID of office site.
    :param str output_file: File name where to save data source results (after running `pulumi preview`).
    :param str status: The status of nas file system. Valid values: `Pending`, `Running`, `Stopped`,`Deleting`, `Deleted`, `Invalid`.
    """
    ...
