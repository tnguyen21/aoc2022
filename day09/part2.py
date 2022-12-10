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
    rope = [Point(0, 0) for _ in range(10)]
    for line in lines:
        direction, magnitude = line.split(" ")
        magnitude = int(magnitude)
        for _ in range(magnitude):
            # print("tail", rope[9])
            # print("[", end="")
            # for knot in rope:
            #     print(f"{knot}, ", end="")
            # print("]")
            # move head
            if direction == "U":
                rope[0].y += 1
            if direction == "D":
                rope[0].y -= 1
            if direction == "L":
                rope[0].x -= 1
            if direction == "R":
                rope[0].x += 1

            for i in range(len(rope)-1):
                # figure out how each knot moves
                head = rope[i]
                tail = rope[i+1]
                
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
                    # move tail diag
                    if head.x > tail.x:
                        tail.x += 1
                    else:
                        tail.x -= 1
                    if head.y > tail.y:
                        tail.y += 1
                    else:
                        tail.y -= 1
                else:
                    # unreachable
                    print("If you're seeing this, something went wrong")

            # after rope has moved, check position of tail
            if (rope[9].x, rope[9].y) not in visited:
                visited.append((rope[9].x, rope[9].y))

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