# FILENAME='aoc01-0.txt'
FILENAME='aoc01-1.txt'

START=50

def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def main():
    lines = parse_input(FILENAME)
    x = START
    zero_count = 0
    for line in lines:
      value = line.replace('L', '-').replace('R', '+')
      x += int(value)
      x = x % 100
      if x == 0:
          zero_count = zero_count + 1
      print(x, zero_count)


if __name__ == '__main__':
    main()
