# FILENAME='aoc03-0.txt'
FILENAME='aoc03-1.txt'

def parse_input(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def get_joltage(line: str, k: int) -> int:
    digits = [int(c) for c in line]
    maxima = [0 for _ in range(k)]
    startpos = 0
    for d in range(k):
        r = k - d
        for j in range(startpos, len(digits) - r + 1):
            i = j - d
            assert(i >= 0)
            assert(j < len(digits))
            if digits[j] > maxima[d]:
                maxima[d] = digits[j]
                startpos = j + 1
    return int(''.join(str(m) for m in maxima))

def main():
    lines = parse_input(FILENAME)
    joltages = [get_joltage(line, 12) for line in lines]
    print(f"Joltages: {joltages}")
    total = sum(joltages)
    print(f"Total joltage: {total}")

if __name__ == '__main__':
    main()
