"""VAST database session.

It should be used to interact with a specific VAST cluster.
For more details see:
- [Virtual IP pool configured with DNS service](https://support.vastdata.com/s/topic/0TOV40000000FThOAM/configuring-network-access-v50)
- [S3 access & secret keys on VAST cluster](https://support.vastdata.com/s/article/UUID-4d2e7e23-b2fb-7900-d98f-96c31a499626)
- [Tabular identity policy with the proper permissions](https://support.vastdata.com/s/article/UUID-14322b60-d6a2-89ac-3df0-3dfbb6974182)
"""

import logging
import os

import boto3

from . import errors, internal_commands, transaction

log = logging.getLogger()


class Features:
    """VAST database features - check if server is already support a feature."""

    def __init__(self, vast_version):
        """Save the server version."""
        self.vast_version = vast_version

        self.check_imports_table = self._check(
            "Imported objects' table feature requires 5.2+ VAST release",
            vast_version >= (5, 2))

        self.check_return_row_ids = self._check(
            "Returning row IDs requires 5.1+ VAST release",
            vast_version >= (5, 1))

        self.check_enforce_semisorted_projection = self._check(
            "Semi-sorted projection enforcement requires 5.1+ VAST release",
            vast_version >= (5, 1))

    def _check(self, msg, supported):
        log.debug("%s (current version is %s): supported=%s", msg, self.vast_version, supported)
        if not supported:
            def fail():
                raise errors.NotSupportedVersion(msg, self.vast_version)
            return fail

        def noop():
            pass
        return noop


class Session:
    """VAST database session."""

    def __init__(self, access=None, secret=None, endpoint=None, ssl_verify=True):
        """Connect to a VAST Database endpoint, using specified credentials."""
        if access is None:
            access = os.environ['AWS_ACCESS_KEY_ID']
        if secret is None:
            secret = os.environ['AWS_SECRET_ACCESS_KEY']
        if endpoint is None:
            endpoint = os.environ['AWS_S3_ENDPOINT_URL']

        self.api = internal_commands.VastdbApi(endpoint, access, secret, ssl_verify=ssl_verify)
        version_tuple = tuple(int(part) for part in self.api.vast_version.split('.'))
        self.features = Features(version_tuple)
        self.s3 = boto3.client('s3',
            aws_access_key_id=access,
            aws_secret_access_key=secret,
            endpoint_url=endpoint)

    def __repr__(self):
        """Don't show the secret key."""
        return f'{self.__class__.__name__}(endpoint={self.api.url}, access={self.api.access_key})'

    def transaction(self):
        """Create a non-initialized transaction object.

        It should be used as a context manager:

            with session.transaction() as tx:
                tx.bucket("bucket").create_schema("schema")
        """
        return transaction.Transaction(self)
