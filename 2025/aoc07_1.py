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

def count_timelines(grid: list[list[str]], length: int, x: int, y: int, cache: dict = {}) -> int:
    timeline_count = 0
    assert x >= 0 and x < length
    assert y >= 1 and y < len(grid)
    assert len(grid[y]) == length
    if y == len(grid) - 1:
        return 1
    y += 1
    c = grid[y][x]
    if c == '.':
        return count_timelines(grid, length, x, y, cache)
    assert c == '^'
    key = (x, y)
    if key in cache:
        return cache[key]
    if x > 0:
        timeline_count += count_timelines(grid, length, x - 1, y, cache)
    if x < length - 1:
        timeline_count += count_timelines(grid, length, x + 1, y, cache)
    cache[key] = timeline_count
    return timeline_count

def main():
    (lines, length) = parse_input(FILENAME)
    grid = [list(line) for line in lines]
    start_x = lines[0].index('S')
    timeline_count = count_timelines(grid, length, start_x, 1)
    print(f"Number of timelines: {timeline_count}")


if __name__ == '__main__':
    main()
