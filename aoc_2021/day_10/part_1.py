from collections import deque
from typing import List

SYNTAX_PAIR = {")": "(", "]": "[", "}": "{", ">": "<"}
SYNTAX_POINT = {")": 3, "]": 57, "}": 1197, ">": 25137}


def check(syntax_list: List[str]) -> int:
    corrupted = []

    for syntax in syntax_list:
        stack = deque()

        for parenthesis in syntax:
            if parenthesis in SYNTAX_PAIR.values():
                stack.append(parenthesis)
            elif parenthesis in SYNTAX_PAIR:
                if not stack:  # corrupted
                    corrupted.append(parenthesis)
                    break

                current_parenthesis = stack.pop()
                if SYNTAX_PAIR[parenthesis] != current_parenthesis:  # corrupted
                    corrupted.append(parenthesis)
                    break

    return sum(SYNTAX_POINT.get(parenthesis, 0) for parenthesis in corrupted)


if __name__ == "__main__":
    with open("input.txt") as f:
        syntax_list = [
            signal.strip() for signal in f.read().split("\n") if signal.strip() != ""
        ]

    result = check(syntax_list)
    print(result)
