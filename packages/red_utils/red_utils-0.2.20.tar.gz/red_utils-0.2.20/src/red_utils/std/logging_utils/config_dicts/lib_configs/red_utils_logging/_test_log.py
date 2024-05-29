from __future__ import annotations

import logging

def test_red_utils_logging():
    log = logging.getLogger("red_utils")

    log.debug("red_utils: Test DEBUG")
    log.info("red_utils: Test INFO")
    log.warning("red_utils: Test WARNING")
    log.error("red_utils: Test ERROR")
    log.critical("red_utils: Test CRITICAL")
