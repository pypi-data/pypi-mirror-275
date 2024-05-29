from __future__ import annotations

import logging

log = logging.getLogger("red_utils.std.logging_utils.lib_loggers.red_utils_logger")

from red_utils.std.logging_utils._methods import merge_config_dicts
from red_utils.std.logging_utils.fmts import (
    DATE_FMT_DATE_ONLY,
    DATE_FMT_STANDARD,
    DATE_FMT_TIME_ONLY,
    MESSAGE_FMT_BASIC,
    MESSAGE_FMT_DETAILED,
    MESSAGE_FMT_STANDARD,
    RED_UTILS_DETAIL_FMT,
    RED_UTILS_FMT,
)

RED_UTILS_STANDARD_FORMATTER = {
    "red_utils_fmt": {"format": RED_UTILS_FMT, "datefmt": DATE_FMT_STANDARD}
}
RED_UTILS_DETAILED_FORMATTER: dict = {
    "red_utils_detail_fmt": {
        "format": RED_UTILS_DETAIL_FMT,
        "datefmt": DATE_FMT_STANDARD,
    }
}


RED_UTILS_CONSOLE_HANDLER: dict = {
    "red_utils_console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "red_utils_fmt",
        "stream": "ext://sys.stdout",
    }
}


RED_UTILS_LOGGER: dict = {
    "red_utils": {
        "handlers": ["red_utils_console"],
        "level": "DEBUG",
        "propagate": False,
    }
}

RED_UTILS_STANDARD_CONSOLE_HANDLER: dict = {
    "red_utils_standard_console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "red_utils_fmt",
        "stream": "ext://sys.stdout",
    }
}
RED_UTILS_DETAILED_CONSOLE_HANDLER: dict = {
    "red_utils_detailed_console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "red_utils_detail_fmt",
        "stream": "ext://sys.stdout",
    }
}


def get_red_utils_standard_logger(log_level: str = "INFO") -> dict:
    _logger_dict: dict = {
        "red_utils": {
            "handlers": ["red_utils_standard_console"],
            "level": log_level.upper(),
            "propagate": False,
        }
    }

    return _logger_dict


def get_red_utils_detailed_logger(log_level: str = "INFO") -> dict:
    _logger_dict: dict = {
        "red_utils": {
            "handlers": ["red_utils_detailed_console"],
            "level": log_level.upper(),
            "propagate": False,
        }
    }

    return _logger_dict


RED_UTILS_STANDARD_LOGGER = get_red_utils_standard_logger()

RED_UTILS_DETAILED_LOGGER = get_red_utils_detailed_logger()

RED_UTILS_STANDARD_LOGGING_CONFIGDICT = {
    "formatters": {
        **RED_UTILS_STANDARD_FORMATTER,
    },
    "handlers": {
        **RED_UTILS_STANDARD_CONSOLE_HANDLER,
    },
    "loggers": {
        **RED_UTILS_STANDARD_LOGGER,
    },
}

RED_UTILS_DETAILED_LOGGING_CONFIGDICT = {
    "formatters": {
        **RED_UTILS_DETAILED_FORMATTER,
    },
    "handlers": {
        **RED_UTILS_DETAILED_CONSOLE_HANDLER,
    },
    "loggers": {
        **RED_UTILS_DETAILED_LOGGER,
    },
}


def merge_red_utils_logging_configdict(
    logging_config: dict = None,
    red_utils_dictconfig: dict = RED_UTILS_STANDARD_LOGGING_CONFIGDICT,
) -> dict:
    try:
        merged_configdict = merge_config_dicts(
            configdict1=logging_config, configdict2=red_utils_dictconfig
        )

        return merged_configdict
    except Exception as exc:
        msg = Exception(
            f"Unhandled exception merging configuration dicts. Details: {exc}"
        )
        log.error(msg)

        raise exc
