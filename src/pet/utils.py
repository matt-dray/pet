"""
Functions to manage pet stats stored in a JSON file on disk.
"""

import datetime
import json
from pathlib import Path


def init_stats(stats_path: Path, name: str) -> None:
    """
    Write initial pet stats to a JSON file on disk.

    Args:
        stats_path (Path): Path to where the pet's stats json file will be written.
        name (str): The pet's name provided by the user.

    Returns:
        None: File is written to disk.
    """
    timestamp_iso_str = datetime.datetime.now().isoformat()
    json_dict = {
        "NAME": name,
        "BORN": timestamp_iso_str,
        "LAST": timestamp_iso_str,
        "AGE": 0,
        "HEALTH": 10,
    }
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    with stats_path.open("w", encoding="utf-8") as f:
        json.dump(json_dict, f)


def read_stats(stats_path: Path) -> dict:
    """
    Read pet statistics from a JSON file on disk.

    Args:
        stats_path (Path): Path to the pet's stats file.

    Returns:
        dict: A dictionary containing the pet's statistics with keys:
            - 'NAME' (str): The pet's name.
            - 'BORN' (str): The datetime of the pet's birth.
            - 'LAST' (str): The datetime of your last interaction with the pet.
            - 'AGE' (int): The pet's age in days.
            - 'HEALTH' (int): The pet's health value (out of 10).
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


def get_datetime(timestamp: str) -> dict:
    """
    Extract the pet's birth date and time from a timestamp string.

    Args:
        timestamp (str): The timestamp of the pet's birth.

    Returns:
        dict: A dictionary with keys:
            - 'DATE' (str): The date portion of the timestamp.
            - 'TIME' (str): The time portion of the timestamp.
    """
    timestamp_iso = datetime.datetime.fromisoformat(timestamp)
    date = timestamp_iso.strftime("%d %b %Y")
    time = timestamp_iso.strftime("%H:%M")
    return {"DATE": date, "TIME": time}


def update_latest_time(stats: dict, stats_path: Path) -> None:
    """
    Write the current time to the stats json file on disk.

    Args:
        stats (dict): Pet stats read from the stats json file on disk.
        stats_path (Path): Path to where the pet's stats json file will be written.

    Returns:
        None: File is written to disk.
    """
    stats["LAST"] = datetime.datetime.now().isoformat()
    with stats_path.open("w", encoding="utf-8") as f:
        json.dump(stats, f)


def update_age(stats: dict, stats_path: Path) -> None:
    """
    Record difference in days between birth and last user interaction.

    Args:
        stats (dict): Pet stats read from the stats json file on disk.
        stats_path (Path): Path to where the pet's stats json file will be written.

    Returns:
        None: File is written to disk.
    """
    born_dt = datetime.datetime.fromisoformat(stats["BORN"])
    last_dt = datetime.datetime.fromisoformat(stats["LAST"])
    age_dt = last_dt - born_dt
    stats["AGE"] = age_dt.days
    with stats_path.open("w", encoding="utf-8") as f:
        json.dump(stats, f)


# def calculate_hp_lost(birth_delta: str, current_hp: int) -> int:


# def write_to_stats(key: str, value: str) -> None:
