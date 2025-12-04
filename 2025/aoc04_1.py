import sys

ADVENTDAY=4
INPUTNUM=sys.argv[1] if len(sys.argv) > 1 else '0'
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'


def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def count(grid: list, row: int, col: int):
    if not grid[row][col]:
        return None
    neigh = 0
    for dr in [-1, 0, 1]:
        if row + dr < 0 or row + dr >= len(grid):
            continue
        for dc in [-1, 0, 1]:
            if col + dc < 0 or col + dc >= len(grid[0]):
                continue
            if dr == 0 and dc == 0:
                continue
            if grid[row + dr][col + dc]:
                neigh += 1
    return neigh

def main():
    lines = parse_input(FILENAME)
    grid = [[c == '@' for c in line] for line in lines]
    total = 0
    while True:
      counts = [[count(grid, r, c) for c in range(len(grid[r]))] for r in range(len(grid))]
      movable = [[count is not None and count < 4 for count in row] for row in counts]
      for row in grid:
          print(''.join(['@' if cell else '.' for cell in row]))
      for row in counts:
          print(''.join(['.' if count is None else str(count) for count in row]))
      for row in movable:
          print(''.join(['x' if m else '-' for m in row]))
      tally = sum(sum(1 for m in row if m) for row in movable)
      print(f'Movable positions: {tally}')
      total += tally
      if tally == 0:
          break
      for r in range(len(grid)):
          for c in range(len(grid[r])):
              if movable[r][c]:
                  grid[r][c] = False
    print(f'Total movable positions: {total}')


if __name__ == '__main__':
    main()
