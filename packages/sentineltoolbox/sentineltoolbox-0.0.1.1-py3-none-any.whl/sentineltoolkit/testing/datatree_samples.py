import shutil
from pathlib import Path
from typing import Any

import numpy as np
import xarray as xr
import zarr
from datatree import DataTree


def fix_path(path: Path | None, **kwargs: Any) -> Path | None:
    if path is None:
        return None
    path = Path(path).absolute()
    if path.exists():
        force = kwargs.get("force", False)
        ask = kwargs.get("ask", False)
        if ask:
            force = input(f"  -> replace {path} ? [n]") == "y"
        if force:
            if path.is_dir():
                shutil.rmtree(str(path))
            elif path.is_file():
                path.unlink()
            else:
                raise NotImplementedError
            print(f"REMOVE {path}")
            return path
        else:
            print(f"KEEP existing path {path}")
            return None
    else:
        return path


def _save_on_disk(dt: DataTree[Any], **kwargs: Any) -> None:
    zarr_path = fix_path(kwargs.get("url"), **kwargs)
    zip_path = fix_path(kwargs.get("url_zip"), **kwargs)

    if zarr_path:
        print(f"CREATE {zarr_path!r}")
        dt.to_zarr(zarr_path)

    if zip_path:
        with zarr.ZipStore(zip_path) as store:
            print(f"CREATE {zip_path!r}")
            dt.to_zarr(store)


def check_datatree_sample(dt: DataTree[Any]) -> None:
    assert "other_metadata" in dt.attrs  # nosec
    assert "measurements" in dt  # nosec
    assert "coarse" in dt["measurements"]  # nosec
    assert "fine" in dt["measurements"]  # nosec
    assert "var1" in dt["measurements/coarse"].variables  # nosec
    var1 = dt["measurements/coarse/var1"]
    assert var1.shape == (2, 3)  # nosec


def create_datatree_sample(**kwargs: Any) -> DataTree[Any]:
    data = xr.DataArray(
        np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
        dims=("x", "y"),
        coords={"x": [10, 20], "y": [10, 20, 30]},
    )

    ds_coarse = xr.Dataset({"var1": data})
    ds_fine: xr.Dataset = ds_coarse.interp(coords={"x": [10, 15, 20], "y": [10, 15, 20, 25, 30]})
    ds_root = xr.Dataset(attrs={"other_metadata": {}})

    dt = DataTree.from_dict({"measurements/coarse": ds_coarse, "measurements/fine": ds_fine, "/": ds_root})

    _save_on_disk(dt, **kwargs)

    return dt
