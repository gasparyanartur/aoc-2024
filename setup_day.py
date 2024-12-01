import argparse
from pathlib import Path
import shutil


def main(day: int, overwrite: bool = False) -> None:
    path = Path(f"solutions/day{day}")
    if path.exists():
        if overwrite:
            print(f"Overwriting day {day}.")
            shutil.rmtree(path)
        else:
            print(f"Day {day} already exists.")
            return

    path.mkdir(parents=True)
    (path / "inputs").mkdir()
    (path / "outputs").mkdir()
    (path / "inputs" / "example.txt").write_text("")
    (path / "inputs" / "puzzle.txt").write_text("")
    (path / "inputs" / "test.txt").write_text("")
    (path / "sol.py").write_text(
        """
def problem1(data: str) -> str:
    return ""
    
def problem2(data: str) -> str:
    return ""
"""
    )

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="day of the challenge (e.g. 1, 2, ..., 25)", type=int)
    parser.add_argument("--overwrite", help="overwrite the day if it already exists", action="store_true")
    args = parser.parse_args()

    main(args.day, overwrite=args.overwrite)

