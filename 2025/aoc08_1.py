import sys
import itertools as it
import math
import numpy as np
import numpy.linalg as la

ADVENTDAY=8
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'


def parse_input(filename: str, pad: bool = False) -> tuple[list[str], int]:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.removesuffix('\n').removesuffix('\r') for line in file.readlines()]
    length = max(len(line) for line in lines)
    if pad:
        lines = [line.ljust(length) for line in lines]
    return lines, length

def main():
    (lines, _) = parse_input(FILENAME)
    boxes = [tuple(map(int, line.split(','))) for line in lines]
    distances = [[la.norm(np.subtract(q, p)) for q in boxes] for p in boxes]
    dist_dict = {d: (i, j) for (i, dists) in enumerate(distances) for (j, d) in enumerate(dists) if i != j}
    dist_dict = dict(sorted(dist_dict.items(), key=lambda item: item[0]))
    assert len(dist_dict.keys()) == len(boxes) * (len(boxes) - 1) / 2
    connect = [z for z in range(len(boxes))]
    for (d, (i, j)) in dist_dict.items():
      (box1, box2) = (boxes[h] for h in (i, j))
      print(box1, box2)
      (x, y) = (connect[h] for h in (i, j))
      for (k, z) in enumerate(connect):
        if z == y:
          connect[k] = x
      size = sum(int(z == x) for z in connect)
      if size == len(boxes):
        print(math.prod(box[0] for box in (box1, box2)))
        break


if __name__ == '__main__':
    main()
