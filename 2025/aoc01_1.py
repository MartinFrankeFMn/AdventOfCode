# FILENAME='aoc01-0.txt'
FILENAME='aoc01-1.txt'

START=50
MODULUS=100

def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def dial(x, d):
    if d == 0:
        return (x, 0)
    c = 0
    y = x + d
    if (x > 0 and y <= 0) or (x < 0 and y >= 0):
        c = c + 1
    while (y >= MODULUS):
        y = y - MODULUS
        c = c + 1
    while (y <= -MODULUS):
        y = y + MODULUS
        c = c + 1
    return (y, c)

def main():
    lines = parse_input(FILENAME)
    x = START
    zero_count = 0
    for line in lines:
      value = line.replace('L', '-').replace('R', '+')
      (x, c) = dial(x, int(value))
      zero_count = zero_count + c
      print(value, x, c, zero_count)


if __name__ == '__main__':
    main()
