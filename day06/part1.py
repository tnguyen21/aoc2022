from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'test_input.txt')

def compute(s: str) -> int:
    marker_rcvd = 0
    window_start_idx = 0
    end_idx = len(s) - 3
    
    for i in range(end_idx):
        substr = s[window_start_idx+i:window_start_idx+i+4]
        if len(set(substr)) == 4:
            marker_rcvd = i + 4
            break

    return marker_rcvd

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())