"""
Command-line interface (CLI) for interacting with pet statistics.
Accepts user input to read, write or delete pet data.
"""

from InquirerPy import inquirer
from pathlib import Path
from platformdirs import user_data_dir
from .utils import (
    init_stats,
    read_stats,
    delete_stats,
    get_datetime,
    update_latest_time,
    update_age,
)


def main():
    stats_path = Path(user_data_dir("pet")) / "pet.json"

    while True:
        if not stats_path.exists():
            name = inquirer.text(message="Your pet's name:").execute()
            init_stats(stats_path, name)

        stats = read_stats(stats_path)
        update_latest_time(stats, stats_path)
        update_age(stats, stats_path)

        action = inquirer.select(
            message="What would you like to do?",
            choices=["Check", "Release", "Quit"],
        ).execute()

        if action == "Check":
            birth = get_datetime(stats["BORN"])
            print(f"Name:   {stats['NAME']}")
            print(f"Birth:  {birth['DATE']} at {birth['TIME']}")
            print(f"Age:    {stats['AGE']} days")
            print(f"Health: {stats['HEALTH']}/10")

        if action == "Release":
            delete_stats(stats_path)
            print("Your pet is released and its data deleted. Farewell!")
            break

        if action == "Quit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
