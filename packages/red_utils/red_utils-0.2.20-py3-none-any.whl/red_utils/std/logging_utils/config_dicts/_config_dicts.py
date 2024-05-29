from __future__ import annotations

import logging

from red_utils.std.logging_utils.fmts._formats import (
    DATE_FMT_DATE_ONLY,
    DATE_FMT_STANDARD,
    DATE_FMT_TIME_ONLY,
    MESSAGE_FMT_BASIC,
    MESSAGE_FMT_DETAILED,
    MESSAGE_FMT_STANDARD,
)

log = logging.getLogger("red_utils.std.logging_utils.config_dicts")

STANDARD_FORMATTER = {
    "standard": {"format": MESSAGE_FMT_STANDARD, "datefmt": DATE_FMT_STANDARD}
}
DETAILED_FORMATTER = {
    "detail": {"format": MESSAGE_FMT_DETAILED, "datefmt": DATE_FMT_STANDARD}
}
BASIC_FORMATTER = {"basic": {"format": MESSAGE_FMT_BASIC, "datefmt": DATE_FMT_STANDARD}}

BASIC_CONSOLE_HANDLER: dict = {
    "basic_console": {
        "class": "logging.StreamHandler",
        "level": "INFO",
        "formatter": "basic",
        "stream": "ext://sys.stdout",
    }
}
STANDARD_CONSOLE_HANDLER: dict = {
    "console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "standard",
        "stream": "ext://sys.stdout",
    }
}

DETAILED_CONSOLE_HANDLER: dict = {
    "console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "detail",
        "stream": "ext://sys.stdout",
    }
}


def get_standard_logger_configdict(
    app_name: str = "app", log_level: str = "WARNING"
) -> dict:
    _logger_dict: dict = {
        app_name: {
            "handlers": ["standard_console"],
            "level": log_level.upper(),
            "propagate": False,
        }
    }

    return _logger_dict


def get_detailed_logger_configdict(app_name: str = "app", log_level: str = "WARNING"):
    _logger_dict: dict = {
        f"{app_name}_detailed": {
            "handlers": ["detailed_console"],
            "level": log_level,
            "propagate": False,
        }
    }

    return _logger_dict


def get_basic_logger_configdict(app_name: str = "app", log_level: str = "WARNING"):
    _logger_dict: dict = {
        f"{app_name}_basic": {
            "handlers": ["basic_console"],
            "level": log_level,
            "propagate": False,
        }
    }

    return _logger_dict


STANDARD_LOGGER = get_standard_logger_configdict()
DETAILED_LOGGER = get_detailed_logger_configdict()
BASIC_LOGGER = get_basic_logger_configdict()
