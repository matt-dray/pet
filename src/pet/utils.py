"""
Read, write and handle pet data from a stats file on disk.
"""

import datetime as dt
import json
from pathlib import Path


def write_stats(stats_path: Path, name: str, timestamp: dt.datetime) -> None:
    """
    Write pet data to a stats file on disk.

    Args:
        stats_path (Path): The path to the stats file.
        name (str): The pet's name.
        timestamp (datettime.datetime) The datetime of the pet's birth.

    Returns:
        None: Data written to disk.
    """
    json_dict = {"NAME": name, "TIMESTAMP": timestamp.isoformat()}
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    with stats_path.open("w", encoding="utf-8") as f:
        json.dump(json_dict, f)


def read_stats(stats_path: Path) -> dict:
    """
    Read pet data from the stats file on disk.

    Args:
        stats_path (Path): The path to the stats file.

    Returns:
        dict: 'NAME' (str) and 'TIMESTAMP' (str) keys.
    """
    stats_text = stats_path.read_text(encoding="utf-8")
    stats_json = json.loads(stats_text)
    return stats_json


def delete_stats(stats_path: Path) -> None:
    """
    Delete the stats file on disk.

    Args:
        stats_path (Path): The path to the stats file.

    Returns:
        None: Data deleted from disk.
    """
    if stats_path.exists():
        stats_path.unlink()


def get_birth_datetime(timestamp: str) -> dict:
    """
    Extract the pet's birth date and time.

    Args:
        timestamp (str): The datetime of the pet's birth.

    Returns:
        dict: 'DATE' (chr) and 'TIME' (chr) keys.
    """
    timestamp_iso = dt.datetime.fromisoformat(timestamp)
    date = timestamp_iso.strftime("%d %b %Y")
    time = timestamp_iso.strftime("%H:%M")
    return {"DATE": date, "TIME": time}


def get_birth_delta(timestamp: str) -> dict:
    """
    Calculate the difference between the pet's birth and now.

    Args:
        timestamp (str): The datetime of the pet's birth.

    Returns:
        dict: 'HOURS' (int) and 'MINS' (int) keys.
    """
    timestamp_iso = dt.datetime.fromisoformat(timestamp)
    delta = dt.datetime.now() - timestamp_iso
    seconds = delta.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    return {"HOURS": int(hours), "MINS": int(minutes)}
