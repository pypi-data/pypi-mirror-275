"""
No public API here.
Use root package to import public function and classes
"""

import os
from dataclasses import dataclass, field
from typing import Any

from sentineltoolkit._utils import fix_url
from sentineltoolkit.exceptions import (
    CredentialTargetNotSupportedError,
    S3BucketCredentialNotFoundError,
)
from sentineltoolkit.typedefs import Credentials

__all__: list[str] = []


def _s3_env_variables_found() -> bool:
    for envvar in {"S3_KEY", "S3_SECRET", "S3_URL"}:
        if envvar not in os.environ:
            return False
    return True


def _aws_env_variables_found() -> bool:
    for envvar in {"AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_ENDPOINT_URL"}:
        if envvar not in os.environ:
            return False
    return True


# docstr-coverage: inherited
def _to_fsspec_filesystem_kwargs(credentials: Credentials, *, url: str | None = None, **kwargs: Any) -> dict[str, Any]:
    """
    Use it like this:

    .. code-block:: python

        import fsspec
        credentials = Credentials(...)
        fsspec.filesystem(**to_fsspec_filesystem_kwargs(credentials))

    Parameters
    ----------
    url, optional
        - if url is set, extract information from url to generate kwargs, including url argument
        - if url is None, generate only credential kwargs. url, filename, store, ...
        must be pass explicitly to open function in this case

    Returns
    -------
        kwargs to pass to function
    """
    kwargs = credentials.to_kwargs(url=url, **kwargs)
    kwargs["protocol"] = "s3"
    return kwargs


# docstr-coverage: inherited
def _to_zarr_open_kwargs(credentials: Credentials, *, url: str | None = None, **kwargs: Any) -> dict[str, Any]:
    """
    Use it like this:

    .. code-block:: python

        import zarr
        credentials = Credentials(...)
        url = "s3://data/xxx.zarr"
        zarr.open_consolidated(**to_zarr_open_kwargs(credentials, url=url))

    Parameters
    ----------
    url, optional
        - if url is set, extract information from url to generate kwargs, including url argument
        - if url is None, generate only credential kwargs. url, filename, store, ...
        must be pass explicitly to open function in this case

    Returns
    -------
        kwargs to pass to function
    """
    if url is None:
        kwargs = {"storage_options": {"s3": _to_fsspec_filesystem_kwargs(credentials, **kwargs)}}
        del kwargs["storage_options"]["s3"]["protocol"]
        return kwargs
    else:
        kwargs = _to_zarr_open_kwargs(credentials, **kwargs)
        kwargs["store"] = fix_url(url)
        return kwargs


# docstr-coverage: inherited
def _to_datatree_open_kwargs(credentials: Credentials, *, url: str | None = None, **kwargs: Any) -> dict[str, Any]:
    """
    Use it like this:

    .. code-block:: python

        import datatree
        credentials = Credentials(...)
        url = "s3://data/xxx.zarr"
        datatree.open_datatree(**to_datatree_open_kwargs(credentials, url=url))

    Parameters
    ----------
    url, optional
        - if url is set, extract information from url to generate kwargs, including url argument
        - if url is None, generate only credential kwargs. url, filename, store, ...
        must be pass explicitly to open function in this case

    Returns
    -------
        kwargs to pass to function
    """
    # backend_kwargs = dict(consolidated=True, compression="infer", decode_cf=True)
    kwargs = dict(
        engine="zarr",
        # backend_kwargs=backend_kwargs,
        consolidated=True,
        # compression="infer",
        decode_cf=True,
    )
    if url is not None:
        import s3fs
        from fsspec import filesystem

        fs = filesystem(**_to_fsspec_filesystem_kwargs(credentials, **kwargs))
        kwargs["filename_or_obj"] = s3fs.S3Map(root=url, s3=fs, check=False)
    return kwargs


# docstr-coverage: inherited
def _to_xarray_open_zarr_kwargs(credentials: Credentials, *, url: str | None = None, **kwargs: Any) -> dict[str, Any]:
    """
    Use it like this:

    .. code-block:: python

        import xarray
        credentials = Credentials(...)
        url = "s3://data/xxx.zarr"
        xarray.open_zarr(**to_xarray_open_zarr_kwargs(credentials, url=url))

    Parameters
    ----------
    url, optional
        - if url is set, extract information from url to generate kwargs, including url argument
        - if url is None, generate only credential kwargs. url, filename, store, ...
        must be pass explicitly to open function in this case

    Returns
    -------
        kwargs to pass to function
    """
    backend_kwargs = _to_zarr_open_kwargs(credentials, **kwargs)
    group = kwargs.get("group", "/")

    kwargs = dict(
        backend_kwargs=backend_kwargs,
        engine="zarr",
        group=group,
        consolidated=True,
        **kwargs,
    )
    if url is not None:
        kwargs["filename_or_obj"] = url

    return kwargs


@dataclass(kw_only=True, frozen=True, repr=False)
class S3BucketCredentials(Credentials):
    key: str
    secret: str
    endpoint_url: str
    region_name: str

    available_targets: Any = field(
        default=(
            "fsspec.filesystem",
            "zarr.open_consolidated",
            "datatree.open_datatree",
            "xarray.open_dataset",
        ),
        init=False,
        repr=False,
    )

    @classmethod
    def from_kwargs(cls, **kwargs: Any) -> "S3BucketCredentials":
        """
        extract credential from kwargs
        """
        # return S3BucketCredentials(key="", secret="", endpoint_url="", region_name="")
        raise NotImplementedError

    @classmethod
    def from_env(cls) -> "S3BucketCredentials":
        """
        First look if env variable are defined ...

        **EOPF env variables**

        * S3_KEY
        * S3_SECRET
        * S3_URL
        * S3_REGION


        **AWS env variables**

        * AWS_ACCESS_KEY_ID - The access key for your AWS account.
        * AWS_SECRET_ACCESS_KEY - The secret key for your AWS account.
        * AWS_DEFAULT_REGION
        * AWS_ENDPOINT_URL

        * AWS_SHARED_CREDENTIALS_FILE. If not set ~/.aws/credentials
        * AWS_CONFIG_FILE. If not set ~/.aws/config
        * AWS_PROFILE: define which env to use in AWS_CONFIG_FILE / AWS_SHARED_CREDENTIALS_FILE

        See
        `Boto 3 doc <BOTO>`_ and `AWS Cli doc <AWS>`_

        Sample of AWS config file

        .. code-block:: ini

            [default]
            aws_access_key_id=foo
            aws_secret_access_key=bar

            [profile dev]
            aws_access_key_id=foo2
            aws_secret_access_key=bar2

        Resolve order is ... (tries first, if not found tries seconds, ...)

        #. EOPF env variables
        #. AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, ...
        #. AWS_CONFIG_FILE + AWS_PROFILE
        #. AWS_SHARED_CREDENTIALS_FILE + AWS_PROFILE

        If all fails, raise :obj:`~sentineltoolkit.exceptions.S3BucketCredentialNotFoundError`

        .. _AWS: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html
        .. _BOTO: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#environment-variables
        """

        if _s3_env_variables_found():
            return S3BucketCredentials(
                key=os.environ["S3_KEY"],
                secret=os.environ["S3_SECRET"],
                endpoint_url=os.environ["S3_URL"],
                region_name=os.environ.get("S3_REGION", ""),
            )
        elif _aws_env_variables_found():
            return S3BucketCredentials(
                key=os.environ["AWS_ACCESS_KEY_ID"],
                secret=os.environ["AWS_SECRET_ACCESS_KEY"],
                endpoint_url=os.environ["AWS_ENDPOINT_URL"],
                region_name=os.environ.get("AWS_DEFAULT_REGION", ""),
            )
        else:
            raise S3BucketCredentialNotFoundError()

    def to_kwargs(self, *, url: str | None = None, target: Any = None, **kwargs: Any) -> dict[str, Any]:

        if target is not None:
            if not isinstance(target, str):
                try:
                    target = target.__module__ + "." + target.__name__
                except AttributeError:
                    pass

        if target:
            # could be extended using entry point if necessary
            if target in ("fsspec.registry.filesystem", "fsspec.filesystem"):
                return _to_fsspec_filesystem_kwargs(self, url=url, **kwargs)
            elif target in ("zarr.convenience.open_consolidated", "zarr.open_consolidated"):
                return _to_zarr_open_kwargs(self, url=url, **kwargs)
            elif target in ("datatree.io.open_datatree", "datatree.open_datatree"):
                return _to_datatree_open_kwargs(self, url=url, **kwargs)
            elif target in ("xarray.backends.api.open_dataset", "xarray.open_dataset"):
                return _to_xarray_open_zarr_kwargs(self, url=url, **kwargs)
            else:
                str_targets = ", ".join(sorted(self.available_targets))
                msg = f"Credentials.to_wargs does not support {target=}. Supported targets are {str_targets}"
                raise CredentialTargetNotSupportedError(msg)
        else:
            kwargs = {
                "key": self.key,
                "secret": self.secret,
                "client_kwargs": {"endpoint_url": self.endpoint_url},
            }
            if self.region_name:
                kwargs["client_kwargs"]["region_name"] = self.region_name
            return kwargs
