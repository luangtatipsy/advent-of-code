from collections import defaultdict
from typing import List


def traverse(paths: List[str]) -> int:
    edges = defaultdict(set)
    for line in paths:
        source, destination = line.split("-")
        edges[source].add(destination)
        edges[destination].add(source)

    all_paths = set()
    caves = []
    caves.append((["start"], False))  # cave, is_visited
    while caves:
        path, is_visited = caves.pop(0)

        if path[-1] == "end":
            all_paths.add(tuple(path))
            continue

        for cave in edges[path[-1]]:
            if cave == "start":
                continue
            elif cave.isupper() or cave not in path:
                caves.append(([*path, cave], is_visited))
            elif is_visited == False and path.count(cave) == 1:
                caves.append(([*path, cave], True))

    return len(all_paths)


if __name__ == "__main__":
    with open("input.txt") as f:
        paths = [line for line in f.read().splitlines(False)]

    result = traverse(paths)
    print(result)
