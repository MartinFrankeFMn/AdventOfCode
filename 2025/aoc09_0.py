import sys

ADVENTDAY=9
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'


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

def main():
    (lines, _) = parse_input(FILENAME)
    coords = [tuple(int(v) for v in line.split(',')) for line in lines]
    print("points: ", len(coords))
    ranges = tuple(tuple(f(c_list) for f in (min, max)) for c_list in zip(*coords))
    print("ranges: ", ranges)
    sizes = (shape_size(p, q) for p in coords for q in coords)
    print("largest rectangle: ", max(sizes))


if __name__ == '__main__':
    main()
