def count_differences(adapters):
    adapters = sorted(adapters)
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)

    differences = dict.fromkeys([1, 2, 3], 0)

    for idx, adapter in enumerate(adapters):
        if idx < len(adapters) - 1:
            next_adapter = adapters[idx + 1]

            for rate in range(1, 4):
                if adapter + rate == next_adapter:
                    differences[rate] += 1
                    break

    return differences


def main(adapters):
    differences = count_differences(adapters)
    print(differences)

    return differences[1] * differences[3]


if __name__ == "__main__":
    with open("input.txt") as f:
        adapters = [
            int(adapter)
            for adapter in f.read().splitlines(False)
            if adapter.strip() != ""
        ]

    multiplied = main(adapters)
    print(multiplied)
