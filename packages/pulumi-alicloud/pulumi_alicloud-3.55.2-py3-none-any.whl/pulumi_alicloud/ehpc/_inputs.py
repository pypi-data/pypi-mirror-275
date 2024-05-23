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
    'ClusterAdditionalVolumeArgs',
    'ClusterAdditionalVolumeRoleArgs',
    'ClusterApplicationArgs',
    'ClusterPostInstallScriptArgs',
]

@pulumi.input_type
class ClusterAdditionalVolumeArgs:
    def __init__(__self__, *,
                 job_queue: Optional[pulumi.Input[str]] = None,
                 local_directory: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 remote_directory: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterAdditionalVolumeRoleArgs']]]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None,
                 volume_mount_option: Optional[pulumi.Input[str]] = None,
                 volume_mountpoint: Optional[pulumi.Input[str]] = None,
                 volume_protocol: Optional[pulumi.Input[str]] = None,
                 volume_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] job_queue: The queue of the nodes to which the additional file system is attached.
        :param pulumi.Input[str] local_directory: The local directory on which the additional file system is mounted.
        :param pulumi.Input[str] location: The type of the cluster. Valid value: `PublicCloud`.
        :param pulumi.Input[str] remote_directory: The remote directory to which the additional file system is mounted.
        :param pulumi.Input[Sequence[pulumi.Input['ClusterAdditionalVolumeRoleArgs']]] roles: The roles. See `roles` below.
        :param pulumi.Input[str] volume_id: The ID of the additional file system.
        :param pulumi.Input[str] volume_mount_option: The mount options of the file system.
        :param pulumi.Input[str] volume_mountpoint: The mount target of the additional file system.
        :param pulumi.Input[str] volume_protocol: The type of the protocol that is used by the additional file system. Valid values: `NFS`, `SMB`. Default value: `NFS`
        :param pulumi.Input[str] volume_type: The type of the additional shared storage. Only NAS file systems are supported.
        """
        if job_queue is not None:
            pulumi.set(__self__, "job_queue", job_queue)
        if local_directory is not None:
            pulumi.set(__self__, "local_directory", local_directory)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if remote_directory is not None:
            pulumi.set(__self__, "remote_directory", remote_directory)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if volume_id is not None:
            pulumi.set(__self__, "volume_id", volume_id)
        if volume_mount_option is not None:
            pulumi.set(__self__, "volume_mount_option", volume_mount_option)
        if volume_mountpoint is not None:
            pulumi.set(__self__, "volume_mountpoint", volume_mountpoint)
        if volume_protocol is not None:
            pulumi.set(__self__, "volume_protocol", volume_protocol)
        if volume_type is not None:
            pulumi.set(__self__, "volume_type", volume_type)

    @property
    @pulumi.getter(name="jobQueue")
    def job_queue(self) -> Optional[pulumi.Input[str]]:
        """
        The queue of the nodes to which the additional file system is attached.
        """
        return pulumi.get(self, "job_queue")

    @job_queue.setter
    def job_queue(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "job_queue", value)

    @property
    @pulumi.getter(name="localDirectory")
    def local_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The local directory on which the additional file system is mounted.
        """
        return pulumi.get(self, "local_directory")

    @local_directory.setter
    def local_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "local_directory", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the cluster. Valid value: `PublicCloud`.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="remoteDirectory")
    def remote_directory(self) -> Optional[pulumi.Input[str]]:
        """
        The remote directory to which the additional file system is mounted.
        """
        return pulumi.get(self, "remote_directory")

    @remote_directory.setter
    def remote_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_directory", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ClusterAdditionalVolumeRoleArgs']]]]:
        """
        The roles. See `roles` below.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterAdditionalVolumeRoleArgs']]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the additional file system.
        """
        return pulumi.get(self, "volume_id")

    @volume_id.setter
    def volume_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_id", value)

    @property
    @pulumi.getter(name="volumeMountOption")
    def volume_mount_option(self) -> Optional[pulumi.Input[str]]:
        """
        The mount options of the file system.
        """
        return pulumi.get(self, "volume_mount_option")

    @volume_mount_option.setter
    def volume_mount_option(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_mount_option", value)

    @property
    @pulumi.getter(name="volumeMountpoint")
    def volume_mountpoint(self) -> Optional[pulumi.Input[str]]:
        """
        The mount target of the additional file system.
        """
        return pulumi.get(self, "volume_mountpoint")

    @volume_mountpoint.setter
    def volume_mountpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_mountpoint", value)

    @property
    @pulumi.getter(name="volumeProtocol")
    def volume_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the protocol that is used by the additional file system. Valid values: `NFS`, `SMB`. Default value: `NFS`
        """
        return pulumi.get(self, "volume_protocol")

    @volume_protocol.setter
    def volume_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_protocol", value)

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the additional shared storage. Only NAS file systems are supported.
        """
        return pulumi.get(self, "volume_type")

    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_type", value)


@pulumi.input_type
class ClusterAdditionalVolumeRoleArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None):
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class ClusterApplicationArgs:
    def __init__(__self__, *,
                 tag: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] tag: The tag of the software.
        """
        if tag is not None:
            pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[str]]:
        """
        The tag of the software.
        """
        return pulumi.get(self, "tag")

    @tag.setter
    def tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag", value)


@pulumi.input_type
class ClusterPostInstallScriptArgs:
    def __init__(__self__, *,
                 args: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] args: The parameter that is used to run the script after the cluster is created.
        :param pulumi.Input[str] url: The URL that is used to download the script after the cluster is created.
        """
        if args is not None:
            pulumi.set(__self__, "args", args)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[str]]:
        """
        The parameter that is used to run the script after the cluster is created.
        """
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "args", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL that is used to download the script after the cluster is created.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


