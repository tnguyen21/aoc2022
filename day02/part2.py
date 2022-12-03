from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    SHAPE_SCORES = {"rock": 1, "paper": 2, "scissors": 3}
    OUTCOME_SCORES = {"Z": 6, "Y": 3, "X": 0}
    score = 0
    lines = s.splitlines()
    for line in lines:
        them, outcome = line.split()
        if (them == "A"):
            if (outcome == "X"):
                shape = "scissors"
            elif (outcome == "Y"):
                shape = "rock"
            else:
                shape = "paper"        
        if (them == "B"):
            if (outcome == "X"):
                shape = "rock"
            elif (outcome == "Y"):
                shape = "paper"
            else:
                shape = "scissors"        
        if (them == "C"):
            if (outcome == "X"):
                shape = "paper"
            elif (outcome == "Y"):
                shape = "scissors"
            else:
                shape = "rock"        
        
        score += SHAPE_SCORES[shape] + OUTCOME_SCORES[outcome]

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