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
import typing

import boto3

from clusterondemandconfig import config

if typing.TYPE_CHECKING:
    from mypy_boto3_ec2.client import EC2Client
    from mypy_boto3_ec2.service_resource import EC2ServiceResource

log = logging.getLogger("cluster-on-demand")


def establish_connection_to_aws():
    log.debug("Establish session with AWS region '%s'" % config["aws_region"])
    session = boto3.session.Session(config["aws_access_key_id"],
                                    config["aws_secret_key"],
                                    region_name=config["aws_region"])
    return session


def create_ec2_resource_client(session: boto3.session.Session) -> tuple[EC2ServiceResource, EC2Client]:
    return session.resource(
        "ec2", api_version="2016-11-15"
    ), session.client(
        "ec2", api_version="2016-11-15"
    )
