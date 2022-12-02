from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(s: str) -> int:
    # every elem in this array is an elf
    calories = []
    lines = s.splitlines()
    accumulator = 0
    for line in lines:
        if line != '':
            accumulator += int(line)
        else:
            calories.append(accumulator)
            accumulator = 0
    # >:(
    calories.append(accumulator)
    
    calories = sorted(calories)

    return sum(calories[-3:])

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())