from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def lookup(monkeys: dict, monkey: str):
    if type(monkeys[monkey]) == int:
        return monkeys[monkey]
    else:
        m1, m2 = monkeys[monkey][0], monkeys[monkey][2]
        op = monkeys[monkey][1]
        m1_val = lookup(monkeys, m1)
        m2_val = lookup(monkeys, m2)
        if op == "+":
            return m1_val + m2_val
        if op == "*":
            return m1_val * m2_val
        if op == "/":
            return m1_val / m2_val
        if op == "-":
            return m1_val - m2_val

def compute(s: str) -> int:
    lines = s.splitlines()
    monkeys = {}
    for line in lines:
        tokens = line.split(" ")
        monkey = tokens[0][:-1]
        if len(tokens[1:]) == 1:
            monkeys[monkey] = int(tokens[1:][0])
        else:
            monkeys[monkey] = tokens[1:]
    
    return lookup(monkeys, "root")
   
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())