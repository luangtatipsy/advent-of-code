from collections import defaultdict
from typing import List


def traverse(paths: List[str]) -> int:
    edges = defaultdict(set)
    for line in paths:
        source, destination = line.split("-")
        edges[source].add(destination)
        edges[destination].add(source)

    # dfs
    all_paths = set()
    caves = [["start"]]
    while caves:
        path = caves.pop(0)

        if path[-1] == "end":
            all_paths.add(tuple(path))
            continue

        for cave in edges[path[-1]]:
            if cave.isupper() or cave not in path:
                caves.append(path + [cave])

    return len(all_paths)


if __name__ == "__main__":
    with open("input.txt") as f:
        paths = [line for line in f.read().splitlines(False)]

    result = traverse(paths)
    print(result)
