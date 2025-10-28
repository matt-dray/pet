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
    update_time_stats,
    update_health_stats,
    print_pet,
)


def main():
    stats_path = Path(user_data_dir("pet")) / "pet.json"

    while True:
        if not stats_path.exists():
            name = inquirer.text(message="Your pet's name:").execute()
            init_stats(stats_path, name)

        stats = read_stats(stats_path)
        update_time_stats(stats, stats_path)
        stats = read_stats(stats_path)
        update_health_stats(stats, stats_path)
        stats = read_stats(stats_path)

        if stats["HEALTH"] <= 0:
            print("🪫 Uh-oh, your pet's health is low!")

        action = inquirer.select(
            message="What would you like to do?",
            choices=["📊 Stats", "👀 See", "❌ Quit", "👋 Release"],
        ).execute()

        if "Stats" in action:
            birth = get_datetime(stats["BORN"])
            print(f"📛 Name:   {stats['NAME']}")
            print(f"🐣 Birth:  {birth['DATE']} at {birth['TIME']}")
            print(f"📅 Age:    {stats['AGE']} days")
            print(f"🔋 Health: {stats['HEALTH']}/10")

        if "See" in action:
            print_pet()

        if "Quit" in action:
            print("Goodbye!")
            break

        if "Release" in action:
            confirm = inquirer.confirm(
                message="Are you sure? Your pet will be gone forever!"
            ).execute()
            if confirm:
                delete_stats(stats_path)
                print("🥲  Your pet was released and its data deleted. Farewell!")
                break


if __name__ == "__main__":
    main()
