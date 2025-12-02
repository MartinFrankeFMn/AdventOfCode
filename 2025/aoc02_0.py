# FILENAME='aoc02-0.txt'
FILENAME='aoc02-1.txt'

START=50

def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def get_invalid_ids(lower: int, upper: int) -> list:
    invalid_ids = []
    for id in range(lower, upper + 1):
        id_str = str(id)
        id_len = len(id_str)
        if id_len % 2 != 0:
            continue
        invalid = id_str[:id_len // 2] == id_str[id_len // 2:]
        if invalid:
            invalid_ids.append(id)
    return invalid_ids

def main():
    (line,) = parse_input(FILENAME)
    ranges = [tuple(int(value) for value in part.split('-')) for part in line.split(',')]
    total = 0
    for (lower, upper) in ranges:
      invalid_ids = get_invalid_ids(lower, upper)
      print(', '.join(str(id) for id in invalid_ids))
      total += sum(invalid_ids)
      print(total)

if __name__ == '__main__':
    main()
