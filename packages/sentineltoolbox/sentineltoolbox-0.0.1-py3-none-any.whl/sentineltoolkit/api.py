# all function are loaded in api module instead of in sentineltoolkit/__init__.py
# to avoid to load all dependencies each time.
# For example, pip loads sentineltoolkit to extract __version__ information.
# In this case, we don't want to load all sub packages and associated dependencies

from .data.flat_data import load_dataset, open_dataset
from .data.tree_data import load_datatree, open_datatree
from .models.credentials import S3BucketCredentials
from .models.filename_generator import (
    AdfFileNameGenerator,
    ProductFileNameGenerator,
    detect_filename_pattern,
)

__all__: list[str] = [
    "S3BucketCredentials",
    "open_dataset",
    "open_datatree",
    "load_dataset",
    "load_datatree",
    "AdfFileNameGenerator",
    "ProductFileNameGenerator",
    "detect_filename_pattern",
]
