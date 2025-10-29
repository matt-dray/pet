"""
A persistent cyberpet that lives on the command line.
"""

from .utils import (
    init_stats,
    read_stats,
    delete_stats,
    get_datetime,
    update_time_stats,
    update_health_stats,
    feed_pet,
    print_pet,
)

__all__ = [
    "init_stats",
    "read_stats",
    "delete_stats",
    "get_datetime",
    "update_time_stats",
    "update_health_stats",
    "feed_pet",
    "print_pet",
]
