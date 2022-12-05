from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    priorities = 0
    iter = (_ for _ in s.splitlines())
    while(True):
        try:
            sack_one = set(next(iter))
            sack_two = set(next(iter))
            sack_three = set(next(iter))

            item = sack_one.intersection(sack_two).intersection(sack_three).pop()
            if (ord(item) >= 97 and ord(item) <= 122):
                priority = ord(item) - 96
            else:
                priority = ord(item) - 38

            priorities += priority
    
        except StopIteration:
            print("end of list")
            break

    return priorities

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())