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
    feed_pet,
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
            choices=["📊 Stats", "👀 See", "🍣 Feed", "❌ Quit", "👋 Release"],
        ).execute()

        if "Stats" in action:
            birth = get_datetime(stats["BORN"])
            print(
                f"📛 Name:   {stats['NAME']}",
                f"🐣 Birth:  {birth['DATE']} at {birth['TIME']}",
                f"📅 Age:    {stats['AGE']} days",
                f"🔋 Health: {stats['HEALTH']}/10",
                sep="\n",
            )

        if "See" in action:
            print_pet()

        if "Feed" in action:
            if stats["HEALTH"] == 10:
                print(f"🤢 {stats['NAME']} is full (health = 10).")
            else:
                feed_pet(stats, stats_path)
                print(
                    f"😋 {stats['NAME']} ate the food (health = stats['HEALTH'] + 1)."
                )

        if "Quit" in action:
            print(f"👋 Goodbye {stats['NAME']}!")
            break

        if "Release" in action:
            confirm = inquirer.confirm(
                message=f"🤔 Are you sure? {stats['NAME']} will be gone forever..."
            ).execute()
            if confirm:
                delete_stats(stats_path)
                print(
                    f"🥲 {stats['NAME']} was released and their data deleted. Farewell!"
                )
                break


if __name__ == "__main__":
    main()
