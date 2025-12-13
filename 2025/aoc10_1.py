import sys
import re
import scipy

ADVENTDAY=10
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'

MACHINE = re.compile(r'\[(.*?)\]\s*(\(.*?\)\s*)\{(.*?)\}')
BUTTON = re.compile(r'\((.*?)\)')


def parse_input(filename: str, pad: bool = False) -> tuple[list[str], int]:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.removesuffix('\n').removesuffix('\r') for line in file.readlines()]
    length = max(len(line) for line in lines)
    if pad:
        lines = [line.ljust(length) for line in lines]
    return lines, length

def get_machine(line: str) -> tuple:
    m = MACHINE.fullmatch(line)
    assert m
    goal = [c == '#' for c in m.group(1)]
    buttons = [[int(light) for light in b.split(',')] for b in BUTTON.findall(m.group(2))]
    joltages = [int(jolt) for jolt in m.group(3).split(',')]
    return (goal, buttons, joltages)

def machine_to_equations(buttons: list, joltages: list) -> list:
    contributions = [[1 if j in button else 0 for button in buttons] for j in range(len(joltages))]
    equations = list(zip(contributions, joltages))
    return equations

def print_machine(info: str, buttons: list, joltages: list):
    print(f"{info}:")
    print(buttons)
    print(joltages)
    print()

def print_equations(info: str, equations: list):
    print(f"{info}:")
    for (contrib, jolt) in equations:
        print(" ".join(str(c) for c in contrib), "|", f"{jolt:3}")
    print()

def print_solution(result):
    print("Solution:")
    print(f"{result.x} -> {result.fun}")
    print()

def solve_equation_system(equations: list):
    (contributions, joltages) = zip(*equations)
    c = [1 for _ in contributions[0]]
    return scipy.optimize.linprog(c, A_eq = contributions, b_eq = joltages, bounds=(0, None), integrality=1)

def solve_machine(machine: tuple) -> int:
    (_, buttons, joltages) = machine
    print_machine("Machine", buttons, joltages)

    equations = machine_to_equations(buttons, joltages)
    print_equations("Equations", equations)

    result = solve_equation_system(equations)
    print_solution(result)
    assert result.success
    return round(result.fun)

def main():
    (lines, _) = parse_input(FILENAME)
    machines = [get_machine(line) for line in lines]
    total = 0
    for machine in machines:
        total += solve_machine(machine)
    print("Total number of button presses:", total)


if __name__ == '__main__':
    main()
