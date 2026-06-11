"""
logger.py — Structured logging for Vigle_Sense.

Sets up a rotating file handler so every session's events are
persisted to disk, in addition to the UI console output.

Usage (in any module):
    from logger import get_logger
    log = get_logger(__name__)
    log.info("Sensor started")
    log.warning("No frames for 5 s")
    log.error("Serial port error: %s", e)
"""

import logging
import os
from logging.handlers import RotatingFileHandler

# Log file lives next to this module (i.e. in the project root)
_LOG_FILE    = os.path.join(os.path.dirname(__file__), "vigle_sense.log")
_MAX_BYTES   = 5 * 1024 * 1024   # 5 MB per log file
_BACKUP_COUNT = 3                 # keep up to 3 rotated files

# ── Module-level flag so we only configure handlers once ─────────
_configured = False


def _configure():
    """Attach handlers to the root logger exactly once."""
    global _configured
    if _configured:
        return

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    # ── 1. Rotating file handler (full DEBUG level) ──────────────
    fh = RotatingFileHandler(
        _LOG_FILE,
        maxBytes=_MAX_BYTES,
        backupCount=_BACKUP_COUNT,
        encoding="utf-8",
    )
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter(
        fmt="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ))
    root.addHandler(fh)

    # ── 2. Console handler (INFO and above) ──────────────────────
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter(
        fmt="%(levelname)-8s  %(name)s  %(message)s",
    ))
    root.addHandler(ch)

    _configured = True


def get_logger(name: str) -> logging.Logger:
    """
    Return a named logger.  Calling this function also ensures the
    root logger is configured with file + console handlers.

    Args:
        name: typically ``__name__`` of the calling module.

    Returns:
        A standard :class:`logging.Logger` instance.
    """
    _configure()
    return logging.getLogger(name)
