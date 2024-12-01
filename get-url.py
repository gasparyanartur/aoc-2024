import argparse
import os

def main(day: int, year: int) -> None:
    print(f"https://adventofcode.com/{year}/day/{day}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="day of the challenge (e.g. 1, 2, ..., 25)", type=int)
    parser.add_argument("--year", help="year of the challenge (e.g. 2024)", type=int, default=2024)
    args = parser.parse_args()

    main(args.day, args.year)
