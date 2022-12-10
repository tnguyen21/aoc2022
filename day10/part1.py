from __future__ import annotations

import argparse
import os.path

from collections import deque

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    lines = s.splitlines()
    register = 1 
    cycle = 1
    next_signal = 20
    signal_str_acc = 0
    signal_strs = []
    for line in lines:
        inst = line.split(" ")
        if inst[0] == "noop":
            cycle += 1
            if cycle == next_signal:
                signal_str_acc = cycle * register
                signal_strs.append(signal_str_acc)
                next_signal += 40
        else:
            _, arg = inst
            cycle += 1
            if cycle == next_signal:
                signal_str_acc = cycle * register
                signal_strs.append(signal_str_acc)
                next_signal += 40
            
            cycle += 1
            register += int(arg)
            if cycle == next_signal:
                signal_str_acc = cycle * register
                signal_strs.append(signal_str_acc)
                next_signal += 40

    return sum(signal_strs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())