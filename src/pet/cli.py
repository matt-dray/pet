"""
Command-line interface (CLI) for interacting with pet statistics.
Accepts user input to read, write or delete pet data.
"""

import datetime as dt
from InquirerPy import inquirer
from pathlib import Path
from platformdirs import user_data_dir
from .utils import (
    write_stats,
    read_stats,
    delete_stats,
    get_birth_datetime,
    get_birth_delta,
)


def main():
    stats_path = Path(user_data_dir("pet")) / "pet.json"

    while True:
        if not stats_path.exists():
            timestamp = dt.datetime.now()
            name = inquirer.text(message="Your pet's name:").execute()
            write_stats(stats_path, name, timestamp)

        stats = read_stats(stats_path)

        action = inquirer.select(
            message="What would you like to do?",
            choices=["Check", "Delete", "Quit"],
        ).execute()

        if action == "Check":
            birth = get_birth_datetime(stats["TIMESTAMP"])
            age = get_birth_delta(stats["TIMESTAMP"])
            print(f"Name:  {stats['NAME']}")
            print(f"Birth: {birth['DATE']} at {birth['TIME']}")
            print(f"Age:   {age['HOURS']} hrs {age['MINS']} mins")

        if action == "Delete":
            delete_stats(stats_path)
            print("Pet data deleted. Goodbye!")
            break

        if action == "Quit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
