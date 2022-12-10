from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    lines = s.splitlines()
    trees = []
    visible = 0
    for line in lines:
        trees.append([int(x) for x in line])
    
    for x in range(len(trees[0])):
        for y in range(len(trees)):
            tree = trees[x][y]

            visible_left = True
            for i in range(0, x):
                if tree <= trees[i][y]:
                    visible_left = False

            visible_right = True
            for i in range(x+1, len(trees[0])):
                if tree <= trees[i][y]:
                    visible_right = False
            
            visible_top = True
            for i in range(0, y):
                if tree <= trees[x][i]:
                    visible_top = False
            
            visible_down = True
            for i in range(y+1, len(trees)):
                if tree <= trees[x][i]:
                    visible_down = False
            
            if (visible_left or visible_right \
                or visible_top or visible_down):
                visible += 1

    return visible

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())