import sys
import math

ADVENTDAY=6
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'

OPERATORS = {
    '+': sum,
    '*': math.prod,
}


def parse_input(filename: str, pad: bool = False) -> tuple[list[str], int]:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.removesuffix('\n').removesuffix('\r') for line in file.readlines()]
    length = max(len(line) for line in lines)
    if pad:
        lines = [line.ljust(length) for line in lines]
    return lines, length

def split_numbers(numbers: list[str]):
    result = []
    for number in numbers:
        if number.strip() == '':
            yield result
            result = []
            continue
        result.append(int(number))
    if result:
        yield result

def main():
    (lines, length) = parse_input(FILENAME, pad=True)
    data = lines[:-1]
    op_symbols = lines[-1].split()
    numbers = [''.join(line[i] for line in data) for i in range(length)]
    operations = [OPERATORS[symbol] for symbol in op_symbols]
    problems = list(zip(split_numbers(numbers), operations))
    print("Problems:", problems)
    results = [operation(nums) for nums, operation in problems]
    print("Results:", results)
    grand_total = sum(results)
    print("Grand Total:", grand_total)


if __name__ == '__main__':
    main()
