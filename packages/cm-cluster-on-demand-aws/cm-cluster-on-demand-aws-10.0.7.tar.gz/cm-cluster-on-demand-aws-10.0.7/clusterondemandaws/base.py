# Copyright 2004-2024 Bright Computing Holding BV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import logging

from clusterondemand.exceptions import UserReportableException, ValidationException
from clusterondemand.paramvalidation import ParamValidator
from clusterondemandaws.paramvalidation import AWSParamValidator
from clusterondemandconfig import config

log = logging.getLogger("cluster-on-demand")


class ClusterCommandBase:
    """Base class for all AWS cluster commands.

    This class only contains non-public validator methods that are intended to be used by
    descendant classes to validate user input. The general contract for all these methods is
    to perform various input sanitization checks, raising an Exception in the case of a failed
    check. If the check passes the _validate_xxx methods will simply return control to the
    caller with no return value.
    """
    def _validate_cluster_names_len_and_regex(self, names):
        validate_max_name_len = config["validate_max_cluster_name_length"]
        for name in names:
            ParamValidator.validate_cluster_name(name, validate_max_name_len)

    def _validate_aws_access_credentials(self):
        if not AWSParamValidator.validate_region(config["aws_region"]):
            raise ValidationException(
                "Region {region} does not exist.".format(
                    region=config["aws_region"]))

        if ("ssh_key_pair" in config and config["ssh_key_pair"] and not
            AWSParamValidator.validate_ssh_key_pair(
                config["ssh_key_pair"],
                config["aws_region"],
                config["aws_access_key_id"],
                config["aws_secret_key"])):
            raise ValidationException(
                "SSH Key pair '{keypair}' does not exist in region '{region}'".format(
                    keypair=config["ssh_key_pair"],
                    region=config["aws_region"]))

        if ("aws_availability_zone" in config and config["aws_availability_zone"] and not
                AWSParamValidator.validate_availability_zone(
                    config["aws_availability_zone"],
                    config["aws_region"],
                    config["aws_access_key_id"],
                    config["aws_secret_key"])):
            raise ValidationException(
                "Availability zone '{zone}' does not exist in region '{region}'".format(
                    zone=config["aws_availability_zone"],
                    region=config["aws_region"]))

    def _validate_instance_types(self):
        if not AWSParamValidator.validate_instance_type(
                config["aws_region"],
                config["head_node_type"]):
            raise UserReportableException(
                "Instance type '{itype}' does not exist in region '{region}'".format(
                    itype=config["head_node_type"],
                    region=config["aws_region"]))

        if not AWSParamValidator.validate_instance_type(
                config["aws_region"],
                config["node_type"]):
            raise UserReportableException(
                "Instance type '{itype}' does not exist in region '{region}'" .format(
                    itype=config["node_type"],
                    region=config["aws_region"]))
