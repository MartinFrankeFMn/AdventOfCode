import sys
import itertools as it
import numpy as np

ADVENTDAY=9
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'

SIZE=100_000 if INPUTNUM == 1 else 14
RED=1
GREEN=2
ROTATIONS=(((1, 0), (0, 1)), ((0, -1), (1, 0)), ((0, 1), (-1, 0)))


def parse_input(filename: str, pad: bool = False) -> tuple[list[str], int]:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.removesuffix('\n').removesuffix('\r') for line in file.readlines()]
    length = max(len(line) for line in lines)
    if pad:
        lines = [line.ljust(length) for line in lines]
    return lines, length

def shape_size(p: tuple, q: tuple) -> int:
    (px, py) = p
    (qx, qy) = q
    return (abs(qx - px) + 1) * (abs(qy - py) + 1)

def skew(a, k: int):
    k %= len(a)
    return it.chain(it.islice(a, k, None), it.islice(a, None, k))

def get_rotation(p: tuple, q: tuple) -> int:
    return np.sign(np.dot(np.dot(ROTATIONS[1], p), q))

def dot(*args) -> tuple:
    return tuple(np.dot(*args))

def add(*args) -> tuple:
    return tuple(np.add(*args))

def sign(*args) -> tuple:
    return tuple(np.sign(*args))

def connect(grid: np.ndarray, p: tuple, q: tuple) -> tuple:
    d = sign(np.subtract(q, p))
    s = add(p, d)
    while s != q:
        grid[s] = GREEN
        s = add(s, d)
    return d

def find_rectangle(grid: np.ndarray, p: tuple, d: tuple, c: int, coords: list) -> int:
    n = dot(ROTATIONS[c], d)
    r = new_r = p
    (inner, edge) = (True, False)
    while inner or edge:
        r = new_r
        new_r = add(r, n)
        edge = grid[new_r] != 0
        inner = inner and not edge
    max_height = np.linalg.norm(np.subtract(r, p), 1) + 1
    candidates = [s for s in coords if 0 <= np.dot(np.subtract(s, p), n) + 1 <= max_height]
    candidates.sort(key=lambda s: -np.linalg.norm(np.subtract(s, p), 1))
    sizes = [shape_size(p, s) for s in candidates]
    return max(sizes)

def main():
    (lines, _) = parse_input(FILENAME)
    coords = [tuple(int(v) for v in line.split(',')) for line in lines]
    print("points: ", len(coords))
    ranges = tuple(tuple(f(c_list) for f in (min, max)) for c_list in zip(*coords))
    print("ranges: ", ranges)
    center = tuple((lo + hi) / 2 for (lo, hi) in ranges)
    print("center: ", center)
    sizes = (shape_size(p, q) for p in coords for q in coords)
    print("largest rectangle: ", max(sizes))
    grid = np.zeros((SIZE, SIZE), dtype=np.int8)
    for p in coords:
        grid[p] = RED
    directions = []
    for (p, q) in zip(coords, skew(coords, 1)):
        d = connect(grid, p, q)
        directions.append(d)
    orientation = np.sign(sum(get_rotation(p, q) for (p, q) in zip(directions, skew(directions, 1))))
    rotation = ROTATIONS[orientation]
    print(grid)
    print("directions:", directions)
    print("orientation:", orientation)
    print("rotation:", rotation)
    corners = []
    for (p, q, h) in it.chain(zip(coords, skew(coords, 1), it.repeat(1)),
                              zip(coords, skew(coords, -1), it.repeat(-1))):
        delta = np.subtract(q, p)
        d = sign(delta)
        length = np.linalg.norm(delta, 1) + 1
        innerness = SIZE - np.linalg.norm(np.subtract(p, center), 1)
        corners.append((p, q, d, h, length, innerness))
    corners.sort(key=lambda corner: -corner[-2] * corner[-1])
    print("corners:")
    for corner in corners:
        print(corner)
        (p, q, d, h, length, innerness) = corner
        size = find_rectangle(grid, p, d, orientation * h, coords)
        print("optimistic rectangle size: ", size)


if __name__ == '__main__':
    main()
