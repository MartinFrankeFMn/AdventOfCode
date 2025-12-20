import sys

ADVENTDAY=11
INPUTNUM=int(sys.argv[1]) if len(sys.argv) > 1 else 0
FILENAME=f'aoc{ADVENTDAY:02}-{INPUTNUM}.txt'


def parse_input(filename: str, pad: bool = False) -> tuple[list[str], int]:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.removesuffix('\n').removesuffix('\r') for line in file.readlines()]
    length = max(len(line) for line in lines)
    if pad:
        lines = [line.ljust(length) for line in lines]
    return lines, length

def main():
    (lines, _) = parse_input(FILENAME)
    graph = dict()
    for line in lines:
        (u, out) = line.split(':')
        graph[u] = set(out.split())
    vertices = set(graph.keys())
    for targets in graph.values():
        vertices.update(targets)
    paths = {u: {v: {1: int(u in graph and v in graph[u])} for v in vertices} for u in vertices}
    print("vertices:", vertices)
    print("graph:", graph)
    for s in range(2, len(paths.keys())):
      print("length:", s)
      for (u, u_paths) in paths.items():
          for (v, u_v_paths) in u_paths.items():
            u_v_paths[s] = 0
      for (u, u_paths) in paths.items():
          for (v, u_v_paths) in u_paths.items():
              for (w, v_w_paths) in paths[v].items():
                  count = u_v_paths[s - 1] * v_w_paths[1]
                  u_paths[w][s] += count
      print(sum(paths['you']['out'].values()))


if __name__ == '__main__':
    main()
