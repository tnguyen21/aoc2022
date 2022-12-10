from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    lines = s.splitlines()
    register = 1
    cycle = 0
    next_signal = 40
    for line in lines:
        inst = line.split(" ")
        if inst[0] == "noop":
            if cycle%40 >= register-1 and cycle%40 <= register+1:
                print("#", end="")
            else:
                print(".", end="")
            cycle += 1
            
            if cycle == next_signal:
                print()
                next_signal += 40
        else:
            _, arg = inst
            if cycle%40 >= register-1 and cycle%40 <= register+1:
                print("#", end="")
            else:
                print(".", end="")
            
            cycle += 1
            
            if cycle == next_signal:
                print()
                next_signal += 40
            
            if cycle%40 >= register-1 and cycle%40 <= register+1:
                print("#", end="")
            else:
                print(".", end="")
            
            cycle += 1
            register += int(arg)
            
            if cycle == next_signal:
                print()
                next_signal += 40

    print()
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())