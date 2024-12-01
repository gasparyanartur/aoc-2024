import argparse
import importlib

from pathlib import Path

def main(day: int, problem: str, data: str) -> None:
    mod = importlib.import_module(f"solutions.day{day}.sol")
    problem_path = Path(f"solutions/day{day}")

    input_path = problem_path / "inputs" / f"{data}.txt"
    input_data: str = input_path.read_text()
    output_path = problem_path / "outputs" / f"{problem}-{data}.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    program = getattr(mod, problem)
    solution = program(input_data)

    print(solution)

    with open(output_path, "w") as f:
        f.write(solution)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="day of the challenge (e.g. 1, 2, ..., 25)", type=int)
    parser.add_argument("problem", type=str, help="problem1, problem2, etc...")
    parser.add_argument(
        "data", type=str, help="example, puzzle, etc..."
    )

    args = parser.parse_args()
    main(args.day, args.problem, args.data)
