"""
This module provides type definition, interface and documentation about common arguments


match_criteria: :obj:`sentineltoolkit.typedefs.PathMatchingCriteria`
    - ``"last_creation_date"`` the product creation date (last part of filename)
      is used to define the most recent data
    - ``"last_modified_time"`` the file/directory modified time (in sense of file system mtime)
      is used to define the most recent data

path_or_pattern: :obj:`sentineltoolkit.typedefs.PathOrPattern`
    example of path:
        - ``"s3://s2-input/Auxiliary/MSI/S2A_ADF_REOB2_xxxxxxx.json"``
        - ``"s3://s3-input/Auxiliary/OL1/S3A_ADF_OLINS_xxxxxxx.zarr"``
        - ``"/home/username/data/S3A_ADF_OLINS_xxxxxxx.zarr"``
        - ``"/d/data/S3A_ADF_OLINS_xxxxxxx.zarr"``
        - ``"D:\\data\\S3A_ADF_OLINS_xxxxxxx.zarr"`` <-- WARNING, don't forget to escape backslash
    example of patterns:
        - ``"s3://s2-input/Auxiliary/MSI/S2A_ADF_REOB2_*.json"``


This module also provide convenience functions to convert Union of types to canonical type.
For example, for input paths:
  - user input can be Path, list of Path, str, list of str and Path. This is defined by type `T_Paths`
  - in code we want to manipulate only list[Path] (our canonical type) and do not write this boring code each time ...

=> this module provide a convenience function for that (:obj:`~sentineltoolkit.typedefs.fix_paths`)
return type of this function also propose the canonical type to use in your code

"""

__all__ = ["Credentials", "PathMatchingCriteria", "PathOrPattern"]

from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Literal, Protocol, TypeAlias

# -----------------------------------------------------------------------------
# SIMPLE ALIASES
# -----------------------------------------------------------------------------

PathMatchingCriteria: TypeAlias = Literal["last_creation_date", "last_modified_time"]  # can be extended


PathOrPattern: TypeAlias = Any  # Need to support at least str, Path, cpm Adf, cpm AnyPath. Data can be zipped or not!

T_DateTime: TypeAlias = datetime | str | int
T_TimeDelta: TypeAlias = timedelta | int

L_DataFileNamePattern = Literal[
    # S3A_OL_0_EFR____20221101T162118_20221101T162318_20221101T180111_0119_091_311______PS1_O_NR_002.SEN3
    "product/s3-legacy",
    "product/s2-legacy",  # S2A_MSIL1C_20231001T094031_N0509_R036_T33RUJ_20231002T065101
    "product/eopf-legacy",  # S3OLCEFR_20230506T015316_0180_B117_T931.zarr
    "product/eopf",  # S03OLCEFR_20230506T015316_0180_B117_T931.zarr
    "product/permissive",  # S03OLCEFR*
    # S3__AX___CLM_AX_20000101T000000_20991231T235959_20151214T120000___________________MPC_O_AL_001.SEN3
    "adf/s3-legacy",
    "adf/s2-legacy",  # S2__OPER_AUX_CAMSAN_ADG__20220330T000000_V20220330T000000_20220331T120000
    "adf/eopf-legacy",  # S3__ADF_SLBDF_20160216T000000_20991231T235959_20231102T155016.zarr
    "adf/eopf",  # S03__ADF_SLBDF_20160216T000000_20991231T235959_20231102T155016.zarr
    "adf/permissive",  # *ADF_SLBDF*,
    "unknown/unknown",
]

T_Paths: TypeAlias = Path | str | list[Path] | list[str] | list[Path | str]

# -----------------------------------------------------------------------------
# INTERFACES / ABSTRACT CLASSES
# -----------------------------------------------------------------------------


class Credentials(Protocol):
    """
    Class storing credential information
    """

    """List of targets available for :meth:`to_kwargs`. Each derived class must define this list."""
    available_targets: list[Any] = []

    def to_kwargs(self, *, url: str | None = None, target: Any = None, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError

    @classmethod
    def from_env(cls) -> "Credentials":
        """
        Tries to generate credential instance from environment variables
        """
        raise NotImplementedError

    @classmethod
    def from_kwargs(cls, **kwargs: Any) -> "Credentials":
        """
        Tries to generate credential instance from given kwargs
        """
        raise NotImplementedError


class FileNameGenerator(Protocol):
    @staticmethod
    def from_string(filename: str, **kwargs: Any) -> "FileNameGenerator":
        """
        Generate a FileNameGenerator from filename string.
        If filename is a legacy filename, you must specify `semantic` to specify the new format semantic.
        """
        raise NotImplementedError

    def is_valid(self) -> bool:
        """
        return True if all required data are set, else retrun False
        """
        raise NotImplementedError

    def to_string(self, **kwargs: Any) -> str:
        """Generate a filename from data and arguments passed by user"""
        raise NotImplementedError


# -----------------------------------------------------------------------------
# INTERFACES / ABSTRACT CLASSES
# -----------------------------------------------------------------------------


def fix_paths(paths: T_Paths) -> list[Path]:
    """Convenience function to convert user paths to canonical list[Path]"""
    if isinstance(paths, (str, Path)):
        path_list = [Path(paths)]
    else:
        path_list = [Path(path) for path in paths]
    return path_list


def fix_datetime(date: T_DateTime) -> datetime:
    """Convenience function to convert date to canonical :class:`datetime.datetime`

    Conversion depends on input type:
      - datetime: no change
      - int: consider it's a timestamp
      - str: consider it's a date str following ISO format YYYYMMDDTHHMMSS
    """
    if isinstance(date, datetime):
        return date
    elif isinstance(date, int):
        return datetime.fromtimestamp(date)
    else:
        return datetime.fromisoformat(date)


def fix_timedelta(delta: T_TimeDelta) -> timedelta:
    """Convenience function to convert time delta to canonical :class:`datetime.timedelta`

    Conversion depends on input type:
      - timedelta: no change
      - int: consider it a delta in seconds
    """
    if isinstance(delta, timedelta):
        return delta
    else:
        return timedelta(seconds=delta)
