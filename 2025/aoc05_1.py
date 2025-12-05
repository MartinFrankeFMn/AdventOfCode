import sys

ADVENTDAY=5
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'


def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def fuse_ranges(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int] | None:
    if first[1] + 1 < second[0] or second[1] + 1 < first[0]:
        return None
    return (min(first[0], second[0]), max(first[1], second[1]))

def range_size(range: tuple[int, int]) -> int:
    return range[1] - range[0] + 1

def main():
    lines = parse_input(FILENAME)
    ranges = []
    for line in lines:
      if line == '':
        continue
      parts = line.split('-')
      if len(parts) == 1:
        continue
      if len(parts) == 2:
        ranges.append((int(parts[0]), int(parts[1])))
        continue
      assert False
    changed = True
    while changed:
      changed = False
      for i in range(len(ranges)):
        for j in range(len(ranges) - 1, i, -1):
          fused = fuse_ranges(ranges[i], ranges[j])
          if fused is not None:
            ranges[i] = fused
            ranges.pop(j)
            changed = True
    print("Ranges:", ranges)
    print("Count:", len(ranges))
    total = sum(range_size(r) for r in ranges)
    print("Total:", total)


if __name__ == '__main__':
    main()
