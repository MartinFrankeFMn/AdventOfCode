import sys
import re
import math

ADVENTDAY=12
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'

SHAPE=re.compile(r'(?:[#.]+\r?\n)+')
REGION=re.compile(r'(\d+)x(\d+):\s*(.*)')


def read_input(filename: str, pad: bool = False) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def parse_shapes(input: str) -> list:
  shapes = [shape.split() for shape in SHAPE.findall(input)]
  return [[[c == '#' for c in line] for line in shape] for shape in shapes]

def parse_regions(input: str) -> list:
  regions = REGION.findall(input)
  return [((int(a), int(b)), [int(r) for r in spec.split()]) for (a, b, spec) in regions]

def main():
    input = read_input(FILENAME)
    shapes = parse_shapes(input)
    regions = parse_regions(input)
    shape_sizes = [sum(map(sum, shape)) for shape in shapes]
    region_sizes = [a * b for ((a, b), _) in regions]
    region_loads = [sum(map(math.prod, zip(spec, shape_sizes))) for (_, spec) in regions]
    region_densities = [load / size for (size, load) in zip(region_sizes, region_loads)]
    okay_densities = [density for density in region_densities if density <= 1.0]
    print("Okay densities: ", len(okay_densities))


if __name__ == '__main__':
    main()
