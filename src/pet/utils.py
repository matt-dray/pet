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
    timestamp_now = datetime.datetime.now().isoformat()
    json_dict = {
        "NAME": name,
        "BORN": timestamp_now,
        "LAST": timestamp_now,  # last interaction
        "DELTA": 0,  # mins
        "AGE": 0,  # days
        "HEALTH": 10,  # 0 to 10
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
            - 'LAST' (str): The datetime of the last interaction with the pet.
            - 'DELTA' (str): Difference in minutes from last interaction to now.
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
    Extract a date and time from an ISO timestamp string.

    Args:
        timestamp (str): The ISO string timestamp for conversion.

    Returns:
        dict: A dictionary with keys:
            - 'DATE' (str): The date portion of the ISO timestamp.
            - 'TIME' (str): The time portion of the ISO timestamp.
    """
    timestamp_iso = datetime.datetime.fromisoformat(timestamp)
    date = timestamp_iso.strftime("%d %b %Y")
    time = timestamp_iso.strftime("%H:%M")
    return {"DATE": date, "TIME": time}


def update_time_stats(stats: dict, stats_path: Path) -> dict:
    """
    Overwrite time-related keys in the stats json file on disk.

    Args:
        stats (dict): Pet stats read from the stats json file on disk.
        stats_path (Path): Path to where the pet's stats json file will be written.

    Returns:
        dict: Pet stats.
    """
    born_iso = stats["BORN"]
    last_iso = stats["LAST"]

    birth_dt = datetime.datetime.fromisoformat(born_iso)
    last_dt = datetime.datetime.fromisoformat(last_iso)
    now_dt = datetime.datetime.now()
    now_iso = now_dt.isoformat()

    delta_born = now_dt - birth_dt
    delta_born_days = delta_born.days

    delta_last = now_dt - last_dt
    delta_last_mins = int(delta_last.total_seconds() // 60)

    stats["LAST"] = now_iso
    stats["DELTA"] = delta_last_mins
    stats["AGE"] = delta_born_days

    with stats_path.open("w", encoding="utf-8") as f:
        json.dump(stats, f)

    return stats


def update_health_stats(stats: dict, stats_path: Path) -> dict:
    """
    Deplete health key over time in the stats json file on disk.

    Args:
        stats (dict): Pet stats read from the stats json file on disk.
        stats_path (Path): Path to where the pet's stats json file will be written.

    Returns:
        dict: Pet stats.
    """
    delta = stats["DELTA"]
    health = stats["HEALTH"]

    health_loss = delta // 60  # lose one health per hour
    new_health = health - health_loss
    if new_health < 0:
        new_health = 0

    stats["HEALTH"] = new_health

    with stats_path.open("w", encoding="utf-8") as f:
        json.dump(stats, f)

    return stats


def feed_pet(stats: dict, stats_path: Path) -> dict:
    """
    Feed pet to increment health key in the stats json file on disk.

    Args:
        stats (dict): Pet stats read from the stats json file on disk.
        stats_path (Path): Path to where the pet's stats json file will be written.

    Returns:
        dict: Pet stats.
    """
    health = stats["HEALTH"]
    health += 1
    new_health = min(health, 10)

    stats["HEALTH"] = new_health

    with stats_path.open("w", encoding="utf-8") as f:
        json.dump(stats, f)

    return stats


def print_pet() -> None:
    """
    Print an image of your pet.

    Returns:
        None: Text is printed to the screen.
    """
    print(
        r"   /\__/\ ",
        r" ={ o x o}=  < meow ",
        r" L(  u u ) ",
        sep="\n",
    )
