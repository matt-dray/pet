"""
CLI entry with user input.
"""

import datetime as dt
from InquirerPy import inquirer
from pathlib import Path
from platformdirs import user_data_dir
from .utils import (
    write_pet_data,
    read_pet_data,
    delete_pet_data,
    extract_timestamp,
    calculate_time_delta,
)


def main():
    pet_data_path = Path(user_data_dir("pet")) / "pet.json"

    while True:
        if not pet_data_path.exists():
            timestamp = dt.datetime.now()
            name = inquirer.text(message="Your pet's name:").execute()
            write_pet_data(pet_data_path, name, timestamp)

        stats = read_pet_data(pet_data_path)

        action = inquirer.select(
            message="What would you like to do?",
            choices=["Check", "Delete", "Quit"],
        ).execute()

        if action == "Check":
            timestamp = extract_timestamp(stats["TIMESTAMP"])
            delta = calculate_time_delta(stats["TIMESTAMP"])
            print(f"Name:  {stats['NAME']}")
            print(f"Birth: {timestamp}")
            print(f"Age:   {delta} seconds")

        if action == "Delete":
            delete_pet_data(pet_data_path)
            print("Pet data deleted. Goodbye!")
            break

        if action == "Quit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
