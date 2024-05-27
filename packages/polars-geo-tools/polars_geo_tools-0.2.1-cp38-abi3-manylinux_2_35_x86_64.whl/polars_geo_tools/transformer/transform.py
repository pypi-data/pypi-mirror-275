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


def transform(
    expr: pl.Expr,
    *,
    from_crs: str,
    to_crs: str,
    column_names: tuple[str, str] = ("x", "y"),
) -> pl.Expr:
    return register_plugin(
        args=[
            expr,
        ],
        symbol="transform",
        is_elementwise=True,
        lib=lib,
        kwargs={
            "from": from_crs,
            "to": to_crs,
            "column_names": column_names,
        },
    )
