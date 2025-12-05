import sys

ADVENTDAY=5
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'


def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def in_range(value: int, range: tuple[int, int]) -> bool:
    return range[0] <= value <= range[1]

def main():
    lines = parse_input(FILENAME)
    ranges = []
    ingredients = []
    fresh = []
    for line in lines:
      if line == '':
        continue
      parts = line.split('-')
      if len(parts) == 1:
        ingredients.append(int(parts[0]))
        continue
      if len(parts) == 2:
        ranges.append((int(parts[0]), int(parts[1])))
        continue
      assert False
    for value in ingredients:
      if any(in_range(value, r) for r in ranges):
        print(f'{value} is fresh')
        fresh.append(value)
      else:
        print(f'{value} is spoiled')
    print(f'Fresh ingredients: {fresh}')
    print(f'Found {len(fresh)} fresh ingredients')


if __name__ == '__main__':
    main()
