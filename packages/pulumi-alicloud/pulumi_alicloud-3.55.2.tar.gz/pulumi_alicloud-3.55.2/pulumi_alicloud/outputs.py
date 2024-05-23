# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetMscSubContactsContactResult',
    'GetMscSubSubscriptionsSubscriptionResult',
    'GetMscSubWebhooksWebhookResult',
    'GetRegionsRegionResult',
    'GetZonesZoneResult',
]

@pulumi.output_type
class GetMscSubContactsContactResult(dict):
    def __init__(__self__, *,
                 account_uid: str,
                 contact_id: str,
                 contact_name: str,
                 email: str,
                 id: str,
                 is_account: bool,
                 is_obsolete: bool,
                 is_verified_email: bool,
                 is_verified_mobile: bool,
                 last_email_verification_time_stamp: str,
                 last_mobile_verification_time_stamp: str,
                 mobile: str,
                 position: str):
        """
        :param str account_uid: UID.
        :param str contact_id: The first ID of the resource.
        :param str contact_name: The User's Contact Name. **Note:** The name must be 2 to 12 characters in length, and can contain uppercase and lowercase letters.
        :param str email: The User's Contact Email Address.
        :param str id: The ID of the Contact.
        :param bool is_account: Indicates Whether the BGP Group Is the Account Itself.
        :param bool is_obsolete: Whether They Have Expired Or Not.
        :param bool is_verified_email: Email Validation for.
        :param bool is_verified_mobile: If the Phone Verification.
        :param str last_email_verification_time_stamp: Last Verification Email Transmission Time.
        :param str last_mobile_verification_time_stamp: The Pieces of Authentication SMS Sending Time.
        :param str mobile: The User's Telephone.
        :param str position: The User's Position. Valid values: `CEO`, `Technical Director`, `Maintenance Director`, `Project Director`,`Finance Director` and `Other`.
        """
        pulumi.set(__self__, "account_uid", account_uid)
        pulumi.set(__self__, "contact_id", contact_id)
        pulumi.set(__self__, "contact_name", contact_name)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "is_account", is_account)
        pulumi.set(__self__, "is_obsolete", is_obsolete)
        pulumi.set(__self__, "is_verified_email", is_verified_email)
        pulumi.set(__self__, "is_verified_mobile", is_verified_mobile)
        pulumi.set(__self__, "last_email_verification_time_stamp", last_email_verification_time_stamp)
        pulumi.set(__self__, "last_mobile_verification_time_stamp", last_mobile_verification_time_stamp)
        pulumi.set(__self__, "mobile", mobile)
        pulumi.set(__self__, "position", position)

    @property
    @pulumi.getter(name="accountUid")
    def account_uid(self) -> str:
        """
        UID.
        """
        return pulumi.get(self, "account_uid")

    @property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> str:
        """
        The first ID of the resource.
        """
        return pulumi.get(self, "contact_id")

    @property
    @pulumi.getter(name="contactName")
    def contact_name(self) -> str:
        """
        The User's Contact Name. **Note:** The name must be 2 to 12 characters in length, and can contain uppercase and lowercase letters.
        """
        return pulumi.get(self, "contact_name")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The User's Contact Email Address.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Contact.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAccount")
    def is_account(self) -> bool:
        """
        Indicates Whether the BGP Group Is the Account Itself.
        """
        return pulumi.get(self, "is_account")

    @property
    @pulumi.getter(name="isObsolete")
    def is_obsolete(self) -> bool:
        """
        Whether They Have Expired Or Not.
        """
        return pulumi.get(self, "is_obsolete")

    @property
    @pulumi.getter(name="isVerifiedEmail")
    def is_verified_email(self) -> bool:
        """
        Email Validation for.
        """
        return pulumi.get(self, "is_verified_email")

    @property
    @pulumi.getter(name="isVerifiedMobile")
    def is_verified_mobile(self) -> bool:
        """
        If the Phone Verification.
        """
        return pulumi.get(self, "is_verified_mobile")

    @property
    @pulumi.getter(name="lastEmailVerificationTimeStamp")
    def last_email_verification_time_stamp(self) -> str:
        """
        Last Verification Email Transmission Time.
        """
        return pulumi.get(self, "last_email_verification_time_stamp")

    @property
    @pulumi.getter(name="lastMobileVerificationTimeStamp")
    def last_mobile_verification_time_stamp(self) -> str:
        """
        The Pieces of Authentication SMS Sending Time.
        """
        return pulumi.get(self, "last_mobile_verification_time_stamp")

    @property
    @pulumi.getter
    def mobile(self) -> str:
        """
        The User's Telephone.
        """
        return pulumi.get(self, "mobile")

    @property
    @pulumi.getter
    def position(self) -> str:
        """
        The User's Position. Valid values: `CEO`, `Technical Director`, `Maintenance Director`, `Project Director`,`Finance Director` and `Other`.
        """
        return pulumi.get(self, "position")


@pulumi.output_type
class GetMscSubSubscriptionsSubscriptionResult(dict):
    def __init__(__self__, *,
                 channel: str,
                 contact_ids: Sequence[int],
                 description: str,
                 email_status: int,
                 id: str,
                 item_id: str,
                 item_name: str,
                 pmsg_status: int,
                 sms_status: int,
                 tts_status: int,
                 webhook_ids: Sequence[int],
                 webhook_status: int):
        """
        :param str channel: The channel the Subscription.
        :param Sequence[int] contact_ids: The ids of subscribed contacts.
        :param str description: The description of the Subscription.
        :param int email_status: The status of email subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        :param str id: The ID of the Subscription.
        :param str item_id: The ID of the Subscription.
        :param str item_name: The name of the Subscription.
        :param int pmsg_status: The status of pmsg subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        :param int sms_status: The status of sms subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        :param int tts_status: The status of tts subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        :param Sequence[int] webhook_ids: The ids of subscribed webhooks.
        :param int webhook_status: The status of webhook subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        """
        pulumi.set(__self__, "channel", channel)
        pulumi.set(__self__, "contact_ids", contact_ids)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "email_status", email_status)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "item_id", item_id)
        pulumi.set(__self__, "item_name", item_name)
        pulumi.set(__self__, "pmsg_status", pmsg_status)
        pulumi.set(__self__, "sms_status", sms_status)
        pulumi.set(__self__, "tts_status", tts_status)
        pulumi.set(__self__, "webhook_ids", webhook_ids)
        pulumi.set(__self__, "webhook_status", webhook_status)

    @property
    @pulumi.getter
    def channel(self) -> str:
        """
        The channel the Subscription.
        """
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter(name="contactIds")
    def contact_ids(self) -> Sequence[int]:
        """
        The ids of subscribed contacts.
        """
        return pulumi.get(self, "contact_ids")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the Subscription.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="emailStatus")
    def email_status(self) -> int:
        """
        The status of email subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        """
        return pulumi.get(self, "email_status")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Subscription.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="itemId")
    def item_id(self) -> str:
        """
        The ID of the Subscription.
        """
        return pulumi.get(self, "item_id")

    @property
    @pulumi.getter(name="itemName")
    def item_name(self) -> str:
        """
        The name of the Subscription.
        """
        return pulumi.get(self, "item_name")

    @property
    @pulumi.getter(name="pmsgStatus")
    def pmsg_status(self) -> int:
        """
        The status of pmsg subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        """
        return pulumi.get(self, "pmsg_status")

    @property
    @pulumi.getter(name="smsStatus")
    def sms_status(self) -> int:
        """
        The status of sms subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        """
        return pulumi.get(self, "sms_status")

    @property
    @pulumi.getter(name="ttsStatus")
    def tts_status(self) -> int:
        """
        The status of tts subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        """
        return pulumi.get(self, "tts_status")

    @property
    @pulumi.getter(name="webhookIds")
    def webhook_ids(self) -> Sequence[int]:
        """
        The ids of subscribed webhooks.
        """
        return pulumi.get(self, "webhook_ids")

    @property
    @pulumi.getter(name="webhookStatus")
    def webhook_status(self) -> int:
        """
        The status of webhook subscription. Valid values: `-1`, `-2`, `0`, `1`. `-1` means required, `-2` means banned; `1` means subscribed; `0` means not subscribed.
        """
        return pulumi.get(self, "webhook_status")


@pulumi.output_type
class GetMscSubWebhooksWebhookResult(dict):
    def __init__(__self__, *,
                 id: str,
                 server_url: str,
                 webhook_id: str,
                 webhook_name: str):
        """
        :param str id: The ID of the Webhook.
        :param str server_url: The serverUrl of the Subscription.
        :param str webhook_id: The first ID of the resource.
        :param str webhook_name: The name of the Webhook. **Note:** The name must be `2` to `12` characters in length, and can contain uppercase and lowercase letters.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "server_url", server_url)
        pulumi.set(__self__, "webhook_id", webhook_id)
        pulumi.set(__self__, "webhook_name", webhook_name)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Webhook.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="serverUrl")
    def server_url(self) -> str:
        """
        The serverUrl of the Subscription.
        """
        return pulumi.get(self, "server_url")

    @property
    @pulumi.getter(name="webhookId")
    def webhook_id(self) -> str:
        """
        The first ID of the resource.
        """
        return pulumi.get(self, "webhook_id")

    @property
    @pulumi.getter(name="webhookName")
    def webhook_name(self) -> str:
        """
        The name of the Webhook. **Note:** The name must be `2` to `12` characters in length, and can contain uppercase and lowercase letters.
        """
        return pulumi.get(self, "webhook_name")


@pulumi.output_type
class GetRegionsRegionResult(dict):
    def __init__(__self__, *,
                 id: str,
                 local_name: str,
                 region_id: str):
        """
        :param str id: ID of the region.
        :param str local_name: Name of the region in the local language.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "local_name", local_name)
        pulumi.set(__self__, "region_id", region_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the region.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="localName")
    def local_name(self) -> str:
        """
        Name of the region in the local language.
        """
        return pulumi.get(self, "local_name")

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> str:
        return pulumi.get(self, "region_id")


@pulumi.output_type
class GetZonesZoneResult(dict):
    def __init__(__self__, *,
                 available_disk_categories: Sequence[str],
                 available_instance_types: Sequence[str],
                 available_resource_creations: Sequence[str],
                 id: str,
                 local_name: str,
                 multi_zone_ids: Sequence[str],
                 slb_slave_zone_ids: Sequence[str]):
        """
        :param Sequence[str] available_disk_categories: Set of supported disk categories.
        :param Sequence[str] available_instance_types: Allowed instance types.
        :param Sequence[str] available_resource_creations: Filter the results by a specific resource type.
               Valid values: `Instance`, `Disk`, `VSwitch`, `Rds`, `KVStore`, `FunctionCompute`, `Elasticsearch`, `Slb`.
               
               > **NOTE:** From version 1.134.0, the `available_resource_creation` value "Rds" has been deprecated.
               If you want to fetch the available zones for RDS instance, you can use datasource alicloud_db_zones
        :param str id: ID of the zone.
        :param str local_name: Name of the zone in the local language.
        :param Sequence[str] multi_zone_ids: A list of zone ids in which the multi zone.
        :param Sequence[str] slb_slave_zone_ids: A list of slb slave zone ids in which the slb master zone.
        """
        pulumi.set(__self__, "available_disk_categories", available_disk_categories)
        pulumi.set(__self__, "available_instance_types", available_instance_types)
        pulumi.set(__self__, "available_resource_creations", available_resource_creations)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "local_name", local_name)
        pulumi.set(__self__, "multi_zone_ids", multi_zone_ids)
        pulumi.set(__self__, "slb_slave_zone_ids", slb_slave_zone_ids)

    @property
    @pulumi.getter(name="availableDiskCategories")
    def available_disk_categories(self) -> Sequence[str]:
        """
        Set of supported disk categories.
        """
        return pulumi.get(self, "available_disk_categories")

    @property
    @pulumi.getter(name="availableInstanceTypes")
    def available_instance_types(self) -> Sequence[str]:
        """
        Allowed instance types.
        """
        return pulumi.get(self, "available_instance_types")

    @property
    @pulumi.getter(name="availableResourceCreations")
    def available_resource_creations(self) -> Sequence[str]:
        """
        Filter the results by a specific resource type.
        Valid values: `Instance`, `Disk`, `VSwitch`, `Rds`, `KVStore`, `FunctionCompute`, `Elasticsearch`, `Slb`.

        > **NOTE:** From version 1.134.0, the `available_resource_creation` value "Rds" has been deprecated.
        If you want to fetch the available zones for RDS instance, you can use datasource alicloud_db_zones
        """
        return pulumi.get(self, "available_resource_creations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the zone.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="localName")
    def local_name(self) -> str:
        """
        Name of the zone in the local language.
        """
        return pulumi.get(self, "local_name")

    @property
    @pulumi.getter(name="multiZoneIds")
    def multi_zone_ids(self) -> Sequence[str]:
        """
        A list of zone ids in which the multi zone.
        """
        return pulumi.get(self, "multi_zone_ids")

    @property
    @pulumi.getter(name="slbSlaveZoneIds")
    def slb_slave_zone_ids(self) -> Sequence[str]:
        """
        A list of slb slave zone ids in which the slb master zone.
        """
        return pulumi.get(self, "slb_slave_zone_ids")


