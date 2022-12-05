from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    # dict[int, list]
    # treat lists as stacks
    crates = {}
    lines = s.splitlines()
    
    # figure out how many crates we have
    crate_input_idx = None
    for idx, line in enumerate(lines):
        if line.strip().split(" ")[0].isnumeric():
            crate_input_idx = idx
            break

    crates_input = lines[:crate_input_idx]
    for col in lines[crate_input_idx].strip().split():
        crates[col] = []
    
    crate_keys = crates.keys()
    for c in crates_input[::-1]:
        for key in crate_keys:
            str_idx = lines[crate_input_idx].index(key)
            if c[str_idx] != " ":
                crates[key].append(c[str_idx])  

    # move crates around
    for move in lines[crate_input_idx+2:]:
        tokens = filter(lambda s: s.isnumeric(), move.split(" "))
        no_of_crates, from_stack, to_stack = list(tokens)

        move_idx = len(crates[from_stack]) - int(no_of_crates)
        tmp = crates[from_stack][move_idx:]
        for _ in range(int(no_of_crates)):
            crates[from_stack].pop()

        crates[to_stack] += tmp

    return_str = ""

    for _, item in crates.items():
        if item != []:
            return_str += item[-1]

    return return_str
    
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())