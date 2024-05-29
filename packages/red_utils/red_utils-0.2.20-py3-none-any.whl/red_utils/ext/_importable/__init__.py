"""Extensions & utilities for third-party libraries I use frequently, like `red_utils.ext.sqla_utils`, which contains
boilerplate code for `SQLAlchemy`, or `red_utils.ext.pydantic`, which contains a method (parse_pydantic_schema) that can
parse a `Pydantic` class object into a compatible `SQLAlchemy` model.

This module uses pkgutil to only load modules if dependencies are met, keeping the `red_utils` package functional by limiting the utilities that are loaded.
If a find_spec() check fails, that import is passed over and will be unavailable
for type completion & usage.

!!! warning

    `pkutil.find_loader()` will be deprecated in a future Python 3.12 release. I will start updating the code in `red_utils` to be
    compatible with the new `importlib.util.find_spec()` method.
"""

from __future__ import annotations

# from importlib.util import find_spec

# if find_spec("pendulum"):
#     from . import time_utils

# if find_spec("loguru"):
#     from . import loguru_utils

# if find_spec("pydantic"):
#     from . import pydantic_utils

# if find_spec("msgpack"):
#     from . import msgpack_utils

# if find_spec("diskcache"):
#     from . import diskcache_utils

# if find_spec("httpx"):
#     from . import httpx_utils

# if find_spec("fastapi"):
#     from . import fastapi_utils

# if find_spec("sqlalchemy"):
#     from . import sqlalchemy_utils

# if find_spec("rich"):
#     from . import context_managers

# if find_spec("pandas") or find_spec("polars"):
#     from . import dataframe_utils
