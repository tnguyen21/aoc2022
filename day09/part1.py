from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    def distance_squared(self, other: Point):
        return (self.x - other.x) * (self.x - other.x) + \
            (self.y - other.y) * (self.y - other.y)

def compute(s: str) -> int:
    lines = s.splitlines()
    visited = [(0, 0)]
    head = Point(0, 0)
    tail = Point(0, 0)
    for line in lines:
        direction, magnitude = line.split(" ")
        magnitude = int(magnitude)
        for _ in range(magnitude):
            if direction == "U":
                head.y += 1
                if tail.distance_squared(head) <= 2 \
                    and ((abs(tail.y - head.y) == 1) \
                    or (tail.y - head.y == 0)):
                    # head and tail still touching, do nothing
                    continue
                elif tail.distance_squared(head) == 2:
                    # tail isn't touch head, need to move tail
                    tail.y += 1
                else:
                    tail.x = head.x
                    tail.y += 1
                if (tail.x, tail.y) not in visited:
                    visited.append(((tail.x, tail.y)))
            
            if direction == "D":
                head.y -= 1
                if tail.distance_squared(head) <= 2 \
                    and ((abs(tail.y - head.y) == 1) \
                    or (tail.y - head.y == 0)):
                    # head and tail still touching, do nothing
                    continue
                elif tail.distance_squared(head) == 2:
                    # tail isn't touch head, need to move tail
                    tail.y -= 1
                else:
                    tail.x = head.x
                    tail.y -= 1
                if (tail.x, tail.y) not in visited:
                    visited.append(((tail.x, tail.y)))
            
            if direction == "L":
                head.x -= 1
                if tail.distance_squared(head) <= 2 \
                    and ((abs(tail.x - head.x) == 1) \
                    or (tail.x - head.x == 0)):
                    # head and tail still touching, do nothing
                    continue
                elif tail.distance_squared(head) == 2:
                    # tail isn't touch head, need to move tail
                    tail.x -= 1
                else:
                    tail.y = head.y
                    tail.x -= 1
                if (tail.x, tail.y) not in visited:
                    visited.append(((tail.x, tail.y)))
            
            if direction == "R":
                head.x += 1
                if tail.distance_squared(head) <= 2 \
                    and ((abs(tail.x - head.x) == 1) \
                    or (tail.x - head.x == 0)):
                    # head and tail still touching, do nothing
                    continue
                elif tail.distance_squared(head) == 2:
                    # tail isn't touch head, need to move tail
                    tail.x += 1
                else:
                    tail.y = head.y
                    tail.x += 1
                if (tail.x, tail.y) not in visited:
                    visited.append(((tail.x, tail.y)))
    # print("head:", head, "tail:", tail)
    # from pprint import pprint
    # pprint(visited)
    return len(visited)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())