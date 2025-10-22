"""
A virtual pet that lives on the command line and is remembered between terminal sessions.
"""

from .utils import (
    write_pet_data,
    read_pet_data,
    delete_pet_data,
    extract_timestamp,
    calculate_time_delta,
)

__all__ = [
    "write_pet_data",
    "read_pet_data",
    "delete_pet_data",
    "extract_timestamp",
    "calculate_time_delta",
]
