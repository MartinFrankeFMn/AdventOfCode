# FILENAME='aoc03-0.txt'
FILENAME='aoc03-1.txt'


def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def get_joltage(line: str, k: int) -> int:
    maximum = 0
    for i in range(len(line) - k + 1):
        for j in range(i + 1, len(line) - k + 2):
            num = int(line[i] + line[j])
            maximum = max(maximum, num)
    return maximum

def main():
    lines = parse_input(FILENAME)
    joltages = [get_joltage(line, 2) for line in lines]
    print(f"Joltages: {joltages}")
    total = sum(joltages)
    print(f"Total joltage: {total}")


if __name__ == '__main__':
    main()
