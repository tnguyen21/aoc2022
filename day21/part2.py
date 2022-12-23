from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'puzzle_input2.txt')

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
        elif op == "*":
            return m1_val * m2_val
        elif op == "/":
            return m1_val / m2_val
        elif op == "-":
            return m1_val - m2_val

def find_humn(monkeys: dict, monkey: str, val: int):
    if monkey == "humn":
        print(val)
        return val
    m1, m2 = monkeys[monkey][0], monkeys[monkey][2]
    op = monkeys[monkey][1]
    m1_val, m2_val = None, None
    try:
        m1_val = lookup(monkeys, m1)
    except:
        pass
    try:
        m2_val = lookup(monkeys, m2)
    except:
        pass
    
    if m1_val == None:
        if op == "+":
            new_v = val - m2_val 
        elif op == "*":
            new_v = val / m2_val 
        elif op == "/":
            new_v = val * m2_val
        elif op == "-":
            new_v = val + m2_val
        assert new_v % 1 == 0
        find_humn(monkeys, m1, new_v)
    else:
        if op == "+":
            new_v = val - m1_val
        elif op == "*":
            new_v = val / m1_val
        elif op == "/":
            new_v = m1_val / val
        elif op == "-":
            new_v = m1_val - val
        assert new_v % 1 == 0
        find_humn(monkeys, m2, new_v)
    
def compute(s: str) -> int:
    lines = s.splitlines()
    monkeys = {}
    for line in lines:
        tokens = line.split(" ")
        monkey = tokens[0][:-1]
        if len(tokens[1:]) == 1:
            if monkey == "humn":
                monkeys[monkey] = None
            else:
                monkeys[monkey] = int(tokens[1:][0])
        else:
            if monkey == "humn":
                monkeys[monkey] = None
            else:
                monkeys[monkey] = tokens[1:]

    m1, m2 = monkeys["root"][0], monkeys["root"][2]
    m1_val, m2_val = None, None
    try:
        m1_val = lookup(monkeys, m1)
    except:
        pass
    try:
        m2_val = lookup(monkeys, m2)
    except:
        pass
    if m1_val:
        v = find_humn(monkeys, m2, m1_val)
    else:
        v = find_humn(monkeys, m1, m2_val)

    return v
   
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())