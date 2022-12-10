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
            # move head
            if direction == "U":
                head.y += 1
            if direction == "D":
                head.y -= 1
            if direction == "L":
                head.x -= 1
            if direction == "R":
                head.x += 1

            if tail.distance_squared(head) < 2:
                # adj col or row
                pass
            elif head.x == tail.x:
                # along same row, but 2 away
                if head.y - tail.y == 2:
                    tail.y += 1

                if head.y - tail.y == -2:
                    tail.y -= 1

            elif head.y == tail.y:
                # along same col, but two away
                if head.x - tail.x == 2:
                    tail.x += 1
                
                if head.x - tail.x == -2:
                    tail.x -= 1

            elif (tail.distance_squared(head) == 2):
                # adj diagonal
                pass
            
            elif (tail.distance_squared(head) > 2):
                # move head
                if direction == "U":
                    tail.y += 1
                    tail.x = head.x
                if direction == "D":
                    tail.y -= 1
                    tail.x = head.x
                if direction == "L":
                    tail.x -= 1
                    tail.y = head.y
                if direction == "R":
                    tail.x += 1
                    tail.y = head.y
            
            
            if (tail.x, tail.y) not in visited:
                visited.append((tail.x, tail.y))

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