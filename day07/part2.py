from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

class Node:
    def __init__(self, path: str):
        self.path = path
        self.parent = None
        self.children = []
    
    def bfs_print(self):
        print(self)
        for i in self.children:
            if type(i) != Node:
                print(i)
            else:
                i.bfs_print()
    
    def get_total_size(self):
        sum = 0
        for i in self.children:
            if type(i) != Node:
                sum += int(i[0])
            else:
                sum += i.get_total_size()

        return sum

    def get_gt_threshold(self, list, threshold):
        for i in self.children:
            if type(i) == Node:
                if i.get_total_size() >= threshold:
                    list.append(i)
                i.get_gt_threshold(list, threshold)

def compute(s: str) -> int:
    lines = s.splitlines()
    root = Node("/")
    curr = root
    for line in lines:
        i = line.split(" ")
        if (i[1] == "cd") and (i[-1] == "/"):
            continue

        if "ls" in i:
            continue
        elif i[0] == "dir":
            new_node = Node(i[-1])
            new_node.parent = curr
            curr.children.append(new_node)
        elif i[0].isnumeric():
            curr.children.append(i)
        elif ("cd" in i and ".." in i):
            curr = curr.parent
        elif (i[1] == "cd"):
            for c in curr.children:
                if type(c) == Node and c.path == i[-1]:
                    curr = c

    DESIRED_UNUSUED_SPACE = 30_000_000
    TOTAL_SPACE = 70_000_000
    delete_threshold = root.get_total_size() - 40_000_000
    l = []
    root.get_gt_threshold(l, delete_threshold)
    l.sort(key=lambda n: n.get_total_size())

    for i in l:
        print(i.path, i.get_total_size())
    



def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())