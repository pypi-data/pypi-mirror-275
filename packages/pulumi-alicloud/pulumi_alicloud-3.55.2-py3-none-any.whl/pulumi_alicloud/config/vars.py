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

import types

__config__ = pulumi.Config('alicloud')


class _ExportableConfig(types.ModuleType):
    @property
    def access_key(self) -> Optional[str]:
        """
        The access key for API operations. You can retrieve this from the 'Security Management' section of the Alibaba Cloud
        console.
        """
        return __config__.get('accessKey')

    @property
    def account_id(self) -> Optional[str]:
        """
        The account ID for some service API operations. You can retrieve this from the 'Security Settings' section of the
        Alibaba Cloud console.
        """
        return __config__.get('accountId')

    @property
    def assume_role(self) -> Optional[str]:
        return __config__.get('assumeRole')

    @property
    def assume_role_with_oidc(self) -> Optional[str]:
        return __config__.get('assumeRoleWithOidc')

    @property
    def client_connect_timeout(self) -> Optional[int]:
        """
        The maximum timeout of the client connection server.
        """
        return __config__.get_int('clientConnectTimeout')

    @property
    def client_read_timeout(self) -> Optional[int]:
        """
        The maximum timeout of the client read request.
        """
        return __config__.get_int('clientReadTimeout')

    @property
    def configuration_source(self) -> Optional[str]:
        return __config__.get('configurationSource')

    @property
    def credentials_uri(self) -> Optional[str]:
        """
        The URI of sidecar credentials service.
        """
        return __config__.get('credentialsUri')

    @property
    def ecs_role_name(self) -> Optional[str]:
        """
        The RAM Role Name attached on a ECS instance for API operations. You can retrieve this from the 'Access Control' section
        of the Alibaba Cloud console.
        """
        return __config__.get('ecsRoleName') or _utilities.get_env('ALICLOUD_ECS_ROLE_NAME')

    @property
    def endpoints(self) -> Optional[str]:
        return __config__.get('endpoints')

    @property
    def fc(self) -> Optional[str]:
        return __config__.get('fc')

    @property
    def log_endpoint(self) -> Optional[str]:
        return __config__.get('logEndpoint')

    @property
    def max_retry_timeout(self) -> Optional[int]:
        """
        The maximum retry timeout of the request.
        """
        return __config__.get_int('maxRetryTimeout')

    @property
    def mns_endpoint(self) -> Optional[str]:
        return __config__.get('mnsEndpoint')

    @property
    def ots_instance_name(self) -> Optional[str]:
        return __config__.get('otsInstanceName')

    @property
    def profile(self) -> Optional[str]:
        """
        The profile for API operations. If not set, the default profile created with `aliyun configure` will be used.
        """
        return __config__.get('profile') or _utilities.get_env('ALICLOUD_PROFILE')

    @property
    def protocol(self) -> Optional[str]:
        return __config__.get('protocol')

    @property
    def region(self) -> Optional[str]:
        """
        The region where Alibaba Cloud operations will take place. Examples are cn-beijing, cn-hangzhou, eu-central-1, etc.
        """
        return __config__.get('region') or _utilities.get_env('ALICLOUD_REGION')

    @property
    def secret_key(self) -> Optional[str]:
        """
        The secret key for API operations. You can retrieve this from the 'Security Management' section of the Alibaba Cloud
        console.
        """
        return __config__.get('secretKey')

    @property
    def secure_transport(self) -> Optional[str]:
        """
        The security transport for the assume role invoking.
        """
        return __config__.get('secureTransport')

    @property
    def security_token(self) -> Optional[str]:
        """
        security token. A security token is only required if you are using Security Token Service.
        """
        return __config__.get('securityToken')

    @property
    def security_transport(self) -> Optional[str]:
        return __config__.get('securityTransport')

    @property
    def shared_credentials_file(self) -> Optional[str]:
        """
        The path to the shared credentials file. If not set this defaults to ~/.aliyun/config.json
        """
        return __config__.get('sharedCredentialsFile')

    @property
    def sign_version(self) -> Optional[str]:
        return __config__.get('signVersion')

    @property
    def skip_region_validation(self) -> Optional[bool]:
        """
        Skip static validation of region ID. Used by users of alternative AlibabaCloud-like APIs or users w/ access to regions
        that are not public (yet).
        """
        return __config__.get_bool('skipRegionValidation')

    @property
    def source_ip(self) -> Optional[str]:
        """
        The source ip for the assume role invoking.
        """
        return __config__.get('sourceIp')

