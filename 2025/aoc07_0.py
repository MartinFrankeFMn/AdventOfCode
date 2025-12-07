import sys

ADVENTDAY=7
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'


def parse_input(filename: str, pad: bool = False) -> tuple[list[str], int]:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.removesuffix('\n').removesuffix('\r') for line in file.readlines()]
    length = max(len(line) for line in lines)
    if pad:
        lines = [line.ljust(length) for line in lines]
    return lines, length

def process(grid: list[list[str]], length: int):
    split_count = 0
    for y in range(1, len(grid)):
        for x in range(length):
            t = grid[y - 1][x]
            tl = grid[y - 1][x - 1] if x > 0 else '.'
            tr = grid[y - 1][x + 1] if x < length - 1 else '.'
            c = grid[y][x]
            emit = t in ('S', '|') or '#' in (tl, tr)
            free = c == '.'
            if emit and free:
                grid[y][x] = '|'
            if emit and c == '^':
                grid[y][x] = '#'
                split_count += 1
    return (grid, split_count)

def main():
    (lines, length) = parse_input(FILENAME)
    grid = [list(line) for line in lines]
    (result_grid, split_count) = process(grid, length)
    print("Final grid state:")
    for row in result_grid:
        print(''.join(row))
    print(f"Number of splits: {split_count}")


if __name__ == '__main__':
    main()
