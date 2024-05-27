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


def lat_lon_to_cell_id(expr: pl.Expr, *, level: int = 30) -> pl.Expr:
    if level < 1 or level > 30:
        raise ValueError("`level` parameter must be between 1 and 30!")

    return register_plugin(
        args=[
            expr,
        ],
        symbol="s2_lat_lon_to_cell_id",
        is_elementwise=True,
        lib=lib,
        kwargs={
            "level": level,
        },
    )


def cell_id_to_lat_lon(expr: pl.Expr) -> pl.Expr:
    return register_plugin(
        args=[
            expr,
        ],
        symbol="s2_cell_id_to_lat_lon",
        is_elementwise=True,
        lib=lib,
    )
