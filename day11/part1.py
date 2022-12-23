from __future__ import annotations

import argparse
import os.path
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

class Monkey:
    def __init__(
        self,
        monkey_id: str,
        starting_items: list[int],
        operation: list[str],
        test: int,
        if_true: str,
        if_false: str,
    ):
        self.monkey_id = monkey_id
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.items_inspected = 0

    def run(self, monkeys: dict):
        for old in self.items:
            # figure out new value
            if self.operation[0] == "+":
                if str.isalpha(self.operation[1]):
                    new = old + old
                else:
                    new = old + int(self.operation[1])
            elif self.operation[0] == "*":
                if str.isalpha(self.operation[1]):
                    new = old * old
                else:
                    new = old * int(self.operation[1])
            else:
                print("Unknown operation:", self.operation[0])
                break

            new = new // 3
            
            if new % self.test == 0:
                monkeys[self.if_true].items.append(new)
            else:
                monkeys[self.if_false].items.append(new)

            self.items_inspected += 1
        
        self.items = []

    def __str__(self):
        return f"Monkey {self.monkey_id} inspected {self.items_inspected} items"
        # return f"Monkey {self.monkey_id}: {self.items}"

def compute(s: str) -> int:
    lines = s.split("\n\n")
    monkeys = {}
    for monkey_input in lines:
        monkey_input = monkey_input.split("\n")
        id = re.findall(r'\d+', monkey_input[0])[0]

        starting_items = [int(_) for _ in re.findall(r'\d+', monkey_input[1])]
        
        operation = monkey_input[2].split(" ")[-2:]
        
        test = int(re.findall(r'\d+', monkey_input[3])[0])
        if_true = re.findall(r'\d+', monkey_input[4])[0]
        if_false = re.findall(r'\d+', monkey_input[5])[0]
        
        monkeys[id] = Monkey(id, starting_items, operation, test, if_true, if_false)
    
    for i in range(20):
        for _, monkey in monkeys.items():
            monkey.run(monkeys)
        # print("Round", i)
    for _, m in monkeys.items():
        print(m)

    return 0

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())