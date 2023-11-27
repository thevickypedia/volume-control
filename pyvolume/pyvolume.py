"""OS-agnostic module to control system volume using built-in functions."""

import logging
import os
import warnings

from . import windows
from .module import settings


def log(msg: str):
    """Log messages if logger is set."""
    if settings.logger:
        settings.logger.error(msg)


def increase(logger: logging.Logger = None):
    """Sets the system volume to maximum."""
    settings.logger = logger
    custom(100)


def decrease(logger: logging.Logger = None):
    """Mutes the system volume."""
    settings.logger = logger
    custom(0)


# noinspection PyUnusedLocal
def pyvolume(level: int, debug: bool = False, logger: logging.Logger = None) -> None:
    """Legacy function."""
    warnings.warn('`pyvolume` function and `debug` flag are deprecated, please use `custom` instead',
                  DeprecationWarning, 2)
    custom(level, logger)


def custom(percent: int, logger: logging.Logger = None) -> None:
    """Set system volume to a certain level.

    Args:
        percent: Volume level in percentage.
        logger: Bring your own logger for custom logging.

    Notes:
        - This package uses:
            - ``amixer`` for volume controls in Linux.
            - ``osascript`` for volume controls in macOS.
            - key combinations for volume controls in Windows.
        - ``amixer`` is a command-line mixer for ALSA(Advanced Linux Sound Architecture) sound-card driver.
    """
    settings.logger = logger
    assert isinstance(percent, int) and 0 <= percent <= 100, "value should be an integer between 0 and 100"
    if settings.os == "Darwin":
        result = os.system('osascript -e "set Volume %d"' % round((8 * percent) / 100))
        if result != 0:
            log(f"Failed to set system volume. ErrorCode: {result}")
    elif settings.os == "Windows":
        try:
            windows.set_volume(level=percent)
        except Exception as error:
            log(error.__str__())
    elif settings.os == "Linux":
        result = os.system("amixer sset 'Master' %d%s /dev/null 2>&1" % (percent, "%"))
        if result != 0:
            log(f"Failed to set system volume. ErrorCode: {result}")
