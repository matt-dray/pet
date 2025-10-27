"""
A virtual pet that lives on the command line and is remembered between terminal sessions.
"""

from .utils import (
    init_stats,
    read_stats,
    delete_stats,
    get_datetime,
    update_latest_time,
    update_age,
)

__all__ = [
    "init_stats",
    "read_stats",
    "delete_stats",
    "get_datetime",
    "update_latest_time",
    "update_age",
]
