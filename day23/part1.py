from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    lines = s.splitlines()
    elves = []
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == "#":
                elves.append((x, y))
    
    for _ in range(10):
        
        

    return 0

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())