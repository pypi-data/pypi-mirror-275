from red_utils.std.logging_utils.fmts import (
    MESSAGE_FMT_DETAILED,
    MESSAGE_FMT_STANDARD,
    DATE_FMT_STANDARD,
    MESSAGE_FMT_BASIC,
)

RED_UTILS_STANDARD_FORMATTER = {
    "red_util_fmt": {"format": MESSAGE_FMT_STANDARD, "datefmt": DATE_FMT_STANDARD}
}
RED_UTILS_DETAILED_FORMATTER: dict = {
    "red_util_detail_fmt": {
        "format": MESSAGE_FMT_DETAILED,
        "datefmt": DATE_FMT_STANDARD,
    }
}

STANDARD_FORMATTER = {
    "standard": {"format": MESSAGE_FMT_STANDARD, "datefmt": DATE_FMT_STANDARD}
}
DETAILED_FORMATTER = {
    "detail": {"format": MESSAGE_FMT_DETAILED, "datefmt": DATE_FMT_STANDARD}
}
BASIC_FORMATTER = {"basic": {"format": MESSAGE_FMT_BASIC, "datefmt": DATE_FMT_STANDARD}}

RED_UTILS_CONSOLE_HANDLER: dict = {
    "red_utils_console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "red_util_fmt",
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

STANDARD_CONSOLE_HANDLER: dict = {
    "console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "standard",
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
