"""
Functions to read, write, and manage pet statistics stored in a JSON stats file on disk.
"""

import datetime as dt
import json
from pathlib import Path


def write_stats(stats_path: Path, name: str, timestamp: dt.datetime) -> None:
    """
    Write pet statistics to a JSON file.

    Args:
        stats_path (Path): Path to the pet's stats file.
        name (str): The pet's name.
        timestamp (datetime.datetime) The datetime of the pet's birth.

    Returns:
        None: File is written to disk.
    """
    json_dict = {"NAME": name, "TIMESTAMP": timestamp.isoformat(), "HP": 10}
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    with stats_path.open("w", encoding="utf-8") as f:
        json.dump(json_dict, f)


def read_stats(stats_path: Path) -> dict:
    """
    Read pet statistics from a JSON file.

    Args:
        stats_path (Path): Path to the pet's stats file.

    Returns:
        dict: A dictionary containing the pet's statistics with keys:
            - 'NAME' (str): The pet's name.
            - 'TIMESTAMP' (str): The datetime of the pet's birth.
            - 'HP' (int): The pet's health points.
    """
    stats_text = stats_path.read_text(encoding="utf-8")
    stats_json = json.loads(stats_text)
    return stats_json


def delete_stats(stats_path: Path) -> None:
    """
    Delete the stats file on disk.

    Args:
        stats_path (Path): Path to the pet's stats file.

    Returns:
        None: File is deleted from disk.
    """
    if stats_path.exists():
        stats_path.unlink()


def get_birth_datetime(timestamp: str) -> dict:
    """
    Extract the pet's birth date and time from a timestamp string.

    Args:
        timestamp (str): The timestamp of the pet's birth.

    Returns:
        dict: A dictionary with keys:
            - 'DATE' (str): The date portion of the timestamp.
            - 'TIME' (str): The time portion of the timestamp.
    """
    timestamp_iso = dt.datetime.fromisoformat(timestamp)
    date = timestamp_iso.strftime("%d %b %Y")
    time = timestamp_iso.strftime("%H:%M")
    return {"DATE": date, "TIME": time}


def get_birth_delta(timestamp: str) -> dict:
    """
    Calculate the time difference between the pet's birth and the current time.

    Args:
        timestamp (str): The timestamp of the pet's birth.

    Returns:
        dict: A dictionary with keys:
            - 'HOURS' (int): The number of hours since birth.
            - 'MINS' (int): The number of minutes after the number of hours since birth.
    """

    timestamp_iso = dt.datetime.fromisoformat(timestamp)
    delta = dt.datetime.now() - timestamp_iso
    seconds = delta.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    return {"HOURS": int(hours), "MINS": int(minutes)}
