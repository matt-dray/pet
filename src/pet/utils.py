"""
Handle pet data.
"""

import datetime as dt
import json
from pathlib import Path


def write_pet_data(pet_data_path: Path, name: str, timestamp: dt.datetime) -> None:
    """
    Write pet data.

    Args:
        pet_data_path (Path): The path to the pet data file.
        name (str): The pet name.
        timestamp (datettime.datetime) The date-time of pet data creation.

    Returns:
        None: Writes to disk.
    """
    json_dict = {"NAME": name, "TIMESTAMP": timestamp.isoformat()}
    pet_data_path.parent.mkdir(parents=True, exist_ok=True)
    with pet_data_path.open("w", encoding="utf-8") as f:
        json.dump(json_dict, f)


def read_pet_data(pet_data_path: Path) -> dict:
    """
    Read pet data.

    Args:
        pet_data_path (Path): The path to the pet data file.

    Returns:
        dict: Pet data.
    """
    pet_data_text = pet_data_path.read_text(encoding="utf-8")
    pet_data_json = json.loads(pet_data_text)
    return pet_data_json


def delete_pet_data(pet_data_path: Path) -> None:
    """
    Delete pet data.

    Args:
        pet_data_path (Path): The path to the pet data file.

    Returns:
        None: Pet data on disk deleted.
    """
    if pet_data_path.exists():
        pet_data_path.unlink()


def extract_timestamp(timestamp: str) -> str:
    """
    Extract timestamp from pet data.

    Args:
        timestamp (str): The path to the pet data file.

    Returns:
        str: Formatted date-time.
    """
    timestamp_iso = dt.datetime.fromisoformat(timestamp)
    return timestamp_iso.strftime("%d %B %Y at %H:%M:%S")


def calculate_time_delta(timestamp: str) -> int:
    """
    Calculate difference between now and timestamp from pet data.

    Args:
        timestamp (str): The path to the pet data file.

    Returns:
        int: Elapsed time in seconds.
    """
    timestamp_iso = dt.datetime.fromisoformat(timestamp)
    delta = dt.datetime.now() - timestamp_iso
    return int(delta.total_seconds())
