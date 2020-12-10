def main(adapters):
    adapters = sorted(adapters)
    highest = max(adapters) + 3
    adapters.append(highest)

    possible_ways = {0: 1}

    for adapter in adapters:
        count = 0
        for diff in range(1, 4):
            if (adapter - diff) in possible_ways:
                count += possible_ways[adapter - diff]

        possible_ways[adapter] = count

    return possible_ways[highest]


if __name__ == "__main__":
    with open("input.txt") as f:
        adapters = [
            int(adapter)
            for adapter in f.read().splitlines(False)
            if adapter.strip() != ""
        ]

    possible_ways = main(adapters)
    print(possible_ways)
