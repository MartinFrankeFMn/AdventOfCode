import sys
import math

ADVENTDAY=6
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'

OPERATORS = {
    '+': sum,
    '*': math.prod,
}


def parse_input(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def main():
    lines = parse_input(FILENAME)
    tokens = [line.split() for line in lines]
    op_symbols = tokens.pop()
    operations = [OPERATORS[symbol] for symbol in op_symbols]
    numbers = [[int(token_line[i]) for token_line in tokens] for i in range(len(operations))]
    problems = list(zip(numbers, operations))
    print("Problems:", problems)
    results = [operation(nums) for nums, operation in problems]
    print("Results:", results)
    grand_total = sum(results)
    print("Grand Total:", grand_total)


if __name__ == '__main__':
    main()
