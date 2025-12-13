import sys
import re

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

def toggle(state: list, button: list) -> list:
    new_state = list(state)
    for light in button:
        new_state[light] = not new_state[light]
    return new_state

def solve_machine(machine: tuple) -> int:
    print(machine)
    (goal, buttons, _) = machine
    states = [[False for _ in goal]]
    count = 0
    while True:
      if any(state == goal for state in states):
          print(count)
          return count
      states = [toggle(state, button) for state in states for button in buttons]
      count += 1

def main():
    (lines, _) = parse_input(FILENAME)
    machines = [get_machine(line) for line in lines]
    total = 0
    for machine in machines:
        total += solve_machine(machine)
    print("Total number of button presses:", total)


if __name__ == '__main__':
    main()
