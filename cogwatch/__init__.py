"""
dpymenus -- Simplified menus for discord.py developers.
"""

__title__ = "cogwatch"
__author__ = "Rob Wagner <rob@robwagner.dev>"
__license__ = "MIT"
__copyright__ = "Copyright 2020-2021 Rob Wagner"
__version__ = "2.1.0"

import logging

from cogwatch.cogwatch import Watcher, watch


logger = logging.getLogger("cogwatch")
logger.addHandler(logging.NullHandler())
