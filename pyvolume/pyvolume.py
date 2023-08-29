"""OS-agnostic module to control system volume using built-in functions."""

import logging
import math
import os
import platform

from . import mod

_SYSTEM = platform.system()


def default_logger() -> logging.Logger:
    """Configure default logger.

    Returns:
        Logger:
        Returns the ``Logger`` object as an argument.
    """
    handler = logging.StreamHandler()
    handler.setFormatter(fmt=logging.Formatter(
        datefmt='%b-%d-%Y %I:%M:%S %p',
        fmt='%(asctime)s - %(levelname)s - [%(module)s:%(lineno)d] - %(funcName)s - %(message)s')
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    logger.addHandler(hdlr=handler)
    return logger


def pyvolume(level: int, debug: bool = False, logger: logging.Logger = None) -> None:
    """Set system volume to a certain level.

    Args:
        level: Volume level in percentage. 0 for mute and 100 for max volume.
        debug: Boolean value to show output logs.
        logger: Bring your own logger for custom logging.

    Notes:
        - This package uses:
            - ``amixer`` for volume controls in Linux.
            - ``osascript`` for volume controls in macOS.
            - key combinations for volume controls in Windows.
        - ``amixer`` is a command-line mixer for ALSA(Advanced Linux Sound Architecture) sound-card driver.
    """
    if not logger:
        logger = default_logger()
    if level > 100:
        # log warning without checking debug flag
        logger.warning("'%d' bad value received. volume level cannot exceed 100, defaulting to 100" % level)
        level = 100
    if level < 0:
        # log warning without checking debug flag
        logger.warning("'%d' bad value received. volume level cannot be negative, defaulting to 0" % level)
        level = 0
    if _SYSTEM == "Darwin":
        result = os.system('osascript -e "set Volume %d"' % math.ceil((8 * level) / 100))
        if debug is False:
            return
        if result == 0:
            logger.info("System volume has been set to %s%s" % (level, "%"))
        else:
            logger.error("Failed to set system volume. ErrorCode: %s%s" % (result, "%"))
    elif _SYSTEM == "Windows":
        try:
            mod.set_volume(level=level)
        except Exception as error:
            logger.error(error.__str__()) if debug else None
        else:
            logger.info("System volume has been set to %s%s" % (level, "%")) if debug else None
    elif _SYSTEM == "Linux":
        result = os.system("amixer sset 'Master' %d%s /dev/null 2>&1" % (level, "%"))
        if debug is False:
            return
        if result == 0:
            logger.info("System volume has been set to %s%s" % (level, "%"))
        else:
            logger.error("Failed to set system volume. ErrorCode: %s%s" % (result, "%"))
    else:
        # log warning without checking debug flag
        logger.warning("This module is not intended for '%s'" % _SYSTEM)
