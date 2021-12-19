from collections import deque
from typing import List

SYNTAX_PAIR = {")": "(", "]": "[", "}": "{", ">": "<"}
SYNTAX_POINT = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMPLETE_POINT = {"(": 1, "[": 2, "{": 3, "<": 4}


def check(syntax_list: List[str]) -> int:
    corrupted = []
    incompleted_scores = []

    for syntax in syntax_list:
        stack = deque()
        is_corrupted = False

        for parenthesis in syntax:
            if parenthesis in SYNTAX_PAIR.values():
                stack.append(parenthesis)
            elif parenthesis in SYNTAX_PAIR:
                if not stack:  # corrupted
                    corrupted.append(parenthesis)
                    is_corrupted = True
                    break

                current_parenthesis = stack.pop()
                if SYNTAX_PAIR[parenthesis] != current_parenthesis:  # corrupted
                    is_corrupted = True
                    corrupted.append(parenthesis)
                    break

        if stack and is_corrupted == False:  # incomplete
            total_score = 0
            for parenthesis in reversed(stack):
                total_score *= 5
                total_score += AUTOCOMPLETE_POINT.get(parenthesis, 0)

            incompleted_scores.append(total_score)

    incompleted_scores.sort()
    middle_idx = len(incompleted_scores) // 2

    return incompleted_scores[middle_idx]


if __name__ == "__main__":
    with open("input.txt") as f:
        syntax_list = [
            signal.strip() for signal in f.read().split("\n") if signal.strip() != ""
        ]

    result = check(syntax_list)
    print(result)
