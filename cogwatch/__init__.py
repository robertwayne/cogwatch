"""
dpymenus -- Simplified menus for discord.py developers.
"""

__title__ = "cogwatch"
__author__ = "Rob Wagner <rob@sombia.com>"
__license__ = "MIT"
__copyright__ = "Copyright 2020-2022 Rob Wagner"
__version__ = "3.0.0a"

import logging

from cogwatch.cogwatch import Watcher, watch

logger = logging.getLogger("cogwatch")
logger.addHandler(logging.NullHandler())
