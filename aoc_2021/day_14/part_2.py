from collections import Counter
from typing import Dict


def polymerize(template: str, insertion_pair: Dict[str, str]) -> int:
    pair_template_counter = Counter()
    for char_idx in range(len(template) - 1):
        pair_template_counter[template[char_idx : char_idx + 2]] += 1

    char_counter = Counter()
    for _ in range(40):
        inserted_counter = Counter()
        char_counter = Counter()
        for key, count in pair_template_counter.items():
            inserted_counter[f"{key[0]}{insertion_pair[key]}"] += count
            inserted_counter[f"{insertion_pair[key]}{key[1]}"] += count
            char_counter[key[0]] += count
            char_counter[insertion_pair[key]] += count
        pair_template_counter = inserted_counter

    char_counter[template[-1]] += 1
    char_counter = char_counter.most_common()

    return char_counter[0][1] - char_counter[-1][1]


if __name__ == "__main__":
    with open("input.txt") as f:
        template, instructions = f.read().split("\n\n")
        insertion_pair = {}
        for instruction in instructions.split("\n"):
            pair, insertion = instruction.split(" -> ")
            insertion_pair[pair] = insertion

    result = polymerize(template, insertion_pair)
    print(result)
