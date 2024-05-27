from __future__ import annotations

import os
from pathlib import Path

import polars as pl

from ..utils import parse_version, register_plugin

if parse_version(pl.__version__) < parse_version("0.20.16"):
    from polars.utils.udfs import _get_shared_lib_location

    lib: str | Path = _get_shared_lib_location(os.path.dirname(__file__))
else:
    lib = Path(os.path.dirname(__file__)).parent


def lat_lon_to_cell_id(expr: pl.Expr, *, resolution: int = 15) -> pl.Expr:
    """Convert column contains lat and lon coords to a h3 cell ID.

    Args:
        expr (pl.Expr): Struct column consists of two float types representes coordinates.
        resolution (int, optional): H3 resolution of cell. Defaults to 15.

    Raises:
        ValueError: When resolution is not an integer, is < 0 or is > 15.

    Returns:
        pl.Expr: _description_
    """
    if not isinstance(resolution, int):
        raise ValueError("`resolution` parameter must be integer valu")

    if resolution < 1 or resolution > 15:
        raise ValueError("`resolution` parameter must be integer value from 1 to 15")
    return register_plugin(
        args=[
            expr,
        ],
        symbol="h3_lat_lon_to_cell_id",
        is_elementwise=True,
        lib=lib,
        kwargs={
            "resolution": resolution,
        },
    )


def cell_id_to_lat_lon(expr: pl.Expr) -> pl.Expr:
    return register_plugin(
        args=[
            expr,
        ],
        symbol="h3_cell_id_to_lat_lon",
        is_elementwise=True,
        lib=lib,
    )
