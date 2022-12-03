from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    """
    A, X = ROCK
    B, Y = PAPER
    C, Z = SCISSORS
    """
    SHAPE_SCORES = {"X": 1, "Y": 2, "Z": 3}
    OUTCOME_SCORES = {"win": 6, "draw": 3, "loss": 0}
    score = 0
    lines = s.splitlines()
    for line in lines:
        them, us = line.split()
        if (them == "A"):
            if (us == "X"):
                outcome = "draw"
            elif (us == "Y"):
                outcome = "win"
            else:
                outcome = "loss"        
        if (them == "B"):
            if (us == "X"):
                outcome = "loss"
            elif (us == "Y"):
                outcome = "draw"
            else:
                outcome = "win"        
        if (them == "C"):
            if (us == "X"):
                outcome = "win"
            elif (us == "Y"):
                outcome = "loss"
            else:
                outcome = "draw"        
        
        score += SHAPE_SCORES[us] + OUTCOME_SCORES[outcome]

    return score

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())