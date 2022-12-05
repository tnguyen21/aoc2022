from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    """
    >>> ord("a")
    97
    >>> ord("b")
    98
    >>> ord("A")
    65
    """
    priorities = 0
    lines = s.splitlines()
    for line in lines:
        compart_split = len(line) // 2
        compartment_one, compartment_two = line[0:compart_split], line[compart_split:]
        compartment_one = set(compartment_one)
        compartment_two = set(compartment_two)

        item = compartment_one.intersection(compartment_two).pop()
        
        if (ord(item) >= 97 and ord(item) <= 122):
            priority = ord(item) - 96
        else:
            priority = ord(item) - 38
        
        priorities += priority
    
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