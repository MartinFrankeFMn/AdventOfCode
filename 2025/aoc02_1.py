# FILENAME='aoc02-0.txt'
FILENAME='aoc02-1.txt'

START=50

def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def is_invalid(id: int) -> bool:
    id_str = str(id)
    id_len = len(id_str)
    for k in range(2, id_len + 1):
        (q, r) = divmod(id_len, k)
        if r != 0:
            continue
        valid = False
        for i in range(1, k):
            if id_str[0:q] != id_str[i * q:(i + 1) * q]:
                valid = True
                break
        if not valid:
            return True
    return False

def get_invalid_ids(lower: int, upper: int) -> list:
    invalid_ids = []
    for id in range(lower, upper + 1):
        invalid = is_invalid(id)
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
