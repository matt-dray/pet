"""
A virtual pet that lives on the command line and is remembered between terminal sessions.
"""

from .utils import (
    write_stats,
    read_stats,
    delete_stats,
    get_birth_datetime,
    get_birth_delta,
)

__all__ = [
    "write_stats",
    "read_stats",
    "delete_stats",
    "get_birth_datetime",
    "get_birth_delta",
]
