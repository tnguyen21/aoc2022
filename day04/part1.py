from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    count = 0 
    lines = s.splitlines()
    for line in lines:
        elf1, elf2 = line.split(",")
        
        elf1_start, elf1_stop = elf1.split("-")
        elf1_start, elf1_stop = int(elf1_start), int(elf1_stop)
        
        elf2_start, elf2_stop = elf2.split("-")
        elf2_start, elf2_stop = int(elf2_start), int(elf2_stop)

        if (elf1_start >= elf2_start and elf1_stop <= elf2_stop) \
        or (elf2_start >= elf1_start and elf2_stop <= elf1_stop):
            count += 1

    return count

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())