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
    'ProvisionedProductOutputArgs',
    'ProvisionedProductParameterArgs',
]

@pulumi.input_type
class ProvisionedProductOutputArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 output_key: Optional[pulumi.Input[str]] = None,
                 output_value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] description: Description of the output value defined in the template.
        :param pulumi.Input[str] output_key: The name of the output value defined in the template.
        :param pulumi.Input[str] output_value: The content of the output value defined in the template.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if output_key is not None:
            pulumi.set(__self__, "output_key", output_key)
        if output_value is not None:
            pulumi.set(__self__, "output_value", output_value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the output value defined in the template.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="outputKey")
    def output_key(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the output value defined in the template.
        """
        return pulumi.get(self, "output_key")

    @output_key.setter
    def output_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output_key", value)

    @property
    @pulumi.getter(name="outputValue")
    def output_value(self) -> Optional[pulumi.Input[str]]:
        """
        The content of the output value defined in the template.
        """
        return pulumi.get(self, "output_value")

    @output_value.setter
    def output_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output_value", value)


@pulumi.input_type
class ProvisionedProductParameterArgs:
    def __init__(__self__, *,
                 parameter_key: Optional[pulumi.Input[str]] = None,
                 parameter_value: Optional[pulumi.Input[str]] = None):
        if parameter_key is not None:
            pulumi.set(__self__, "parameter_key", parameter_key)
        if parameter_value is not None:
            pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "parameter_key")

    @parameter_key.setter
    def parameter_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_key", value)

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "parameter_value")

    @parameter_value.setter
    def parameter_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_value", value)


