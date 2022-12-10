from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    lines = s.splitlines()
    trees = []
    highest_score = 0
    for line in lines:
        trees.append([int(x) for x in line])
    
    for x in range(len(trees[0])):
        for y in range(len(trees)):
            tree = trees[x][y]

            visible_left = 0
            for i in range(x-1, -1, -1):
                if tree > trees[i][y]:
                    visible_left += 1
                else:
                    visible_left += 1
                    break

            visible_right = 0
            for i in range(x+1, len(trees[0])):
                if tree > trees[i][y]:
                    visible_right += 1
                else:
                    visible_right += 1
                    break
            
            visible_top = 0
            for i in range(y-1, -1, -1):
                if tree > trees[x][i]:
                    visible_top += 1
                else:
                    visible_top += 1
                    break
            
            visible_down = 0
            for i in range(y+1, len(trees)):
                if tree > trees[x][i]:
                    visible_down += 1
                else:
                    visible_down += 1
                    break
            
            score = visible_down * visible_left * visible_right * visible_top
            if score > highest_score:
                highest_score = score
        
    return highest_score


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())