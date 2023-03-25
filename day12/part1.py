from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    map = []
    visited = []
    paths = []
    curr = (0, 0)
    end = (0, 0)
    for x, line in enumerate(lines):
        row = [ord(c) for c in line]
        if ord('S') in row:
            y = row.index(ord('S'))
            curr = (x, y)
        if ord('E') in row:
            y = row.index(ord('E'))
            end = (x, y)
        map.append([c for c in line])

    while (curr != end):
        up = (curr[0] + 1, curr[1])
        down = (curr[0] - 1, curr[1])
        left = (curr[0], curr[1] - 1)
        right = (curr[0], curr[1]  + 1)
        
        moves = []

        for move in [up, down, left, right]:
            if map[move[0]][move[1]] <= map[curr[0]][curr[1]] + 1:
                moves.append(move)
        


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