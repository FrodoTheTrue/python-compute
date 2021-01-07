# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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
#

import abc
import typing
import pkg_resources

from google import auth  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore

from google.cloud.compute_v1.types import compute


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-compute",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


class BackendServicesTransport(abc.ABC):
    """Abstract transport class for BackendServices."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/compute",
        "https://www.googleapis.com/auth/cloud-platform",
    )

    def __init__(
        self,
        *,
        host: str = "compute.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: typing.Optional[str] = None,
        scopes: typing.Optional[typing.Sequence[str]] = AUTH_SCOPES,
        quota_project_id: typing.Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scope (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):	
                The client info used to send a user-agent string along with	
                API requests. If ``None``, then default info will be used.	
                Generally, you only need to set this if you're developing	
                your own client library.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = auth.load_credentials_from_file(
                credentials_file, scopes=scopes, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = auth.default(
                scopes=scopes, quota_project_id=quota_project_id
            )

        # Save the credentials.
        self._credentials = credentials

        # Lifted into its own function so it can be stubbed out during tests.
        self._prep_wrapped_messages(client_info)

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.add_signed_url_key: gapic_v1.method.wrap_method(
                self.add_signed_url_key, default_timeout=None, client_info=client_info,
            ),
            self.aggregated_list: gapic_v1.method.wrap_method(
                self.aggregated_list, default_timeout=None, client_info=client_info,
            ),
            self.delete: gapic_v1.method.wrap_method(
                self.delete, default_timeout=None, client_info=client_info,
            ),
            self.delete_signed_url_key: gapic_v1.method.wrap_method(
                self.delete_signed_url_key,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get: gapic_v1.method.wrap_method(
                self.get, default_timeout=None, client_info=client_info,
            ),
            self.get_health: gapic_v1.method.wrap_method(
                self.get_health, default_timeout=None, client_info=client_info,
            ),
            self.insert: gapic_v1.method.wrap_method(
                self.insert, default_timeout=None, client_info=client_info,
            ),
            self.list: gapic_v1.method.wrap_method(
                self.list, default_timeout=None, client_info=client_info,
            ),
            self.patch: gapic_v1.method.wrap_method(
                self.patch, default_timeout=None, client_info=client_info,
            ),
            self.set_security_policy: gapic_v1.method.wrap_method(
                self.set_security_policy, default_timeout=None, client_info=client_info,
            ),
            self.update: gapic_v1.method.wrap_method(
                self.update, default_timeout=None, client_info=client_info,
            ),
        }

    @property
    def add_signed_url_key(
        self,
    ) -> typing.Callable[
        [compute.AddSignedUrlKeyBackendServiceRequest],
        typing.Union[compute.Operation, typing.Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def aggregated_list(
        self,
    ) -> typing.Callable[
        [compute.AggregatedListBackendServicesRequest],
        typing.Union[
            compute.BackendServiceAggregatedList,
            typing.Awaitable[compute.BackendServiceAggregatedList],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete(
        self,
    ) -> typing.Callable[
        [compute.DeleteBackendServiceRequest],
        typing.Union[compute.Operation, typing.Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_signed_url_key(
        self,
    ) -> typing.Callable[
        [compute.DeleteSignedUrlKeyBackendServiceRequest],
        typing.Union[compute.Operation, typing.Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get(
        self,
    ) -> typing.Callable[
        [compute.GetBackendServiceRequest],
        typing.Union[compute.BackendService, typing.Awaitable[compute.BackendService]],
    ]:
        raise NotImplementedError()

    @property
    def get_health(
        self,
    ) -> typing.Callable[
        [compute.GetHealthBackendServiceRequest],
        typing.Union[
            compute.BackendServiceGroupHealth,
            typing.Awaitable[compute.BackendServiceGroupHealth],
        ],
    ]:
        raise NotImplementedError()

    @property
    def insert(
        self,
    ) -> typing.Callable[
        [compute.InsertBackendServiceRequest],
        typing.Union[compute.Operation, typing.Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list(
        self,
    ) -> typing.Callable[
        [compute.ListBackendServicesRequest],
        typing.Union[
            compute.BackendServiceList, typing.Awaitable[compute.BackendServiceList]
        ],
    ]:
        raise NotImplementedError()

    @property
    def patch(
        self,
    ) -> typing.Callable[
        [compute.PatchBackendServiceRequest],
        typing.Union[compute.Operation, typing.Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_security_policy(
        self,
    ) -> typing.Callable[
        [compute.SetSecurityPolicyBackendServiceRequest],
        typing.Union[compute.Operation, typing.Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update(
        self,
    ) -> typing.Callable[
        [compute.UpdateBackendServiceRequest],
        typing.Union[compute.Operation, typing.Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()


__all__ = ("BackendServicesTransport",)
