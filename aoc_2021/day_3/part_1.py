from typing import List


def __common_bit(bits: List, how: str) -> str:
    common_bit = ""
    if how == "most":
        common_bit = max(set(bits), key=bits.count)
    elif how == "least":
        common_bit = min(set(bits), key=bits.count)

    return common_bit


def binary_diagnostic(diagnostic_reports: List[str]) -> int:
    number_of_bits = len(diagnostic_reports[0])
    gamma = ""
    epsilon = ""

    for idx in range(number_of_bits):
        bits = []
        for report in diagnostic_reports:
            bits.append(report[idx])

        most_common_bit = __common_bit(bits, how="most")
        least_common_bit = __common_bit(bits, how="least")

        gamma += most_common_bit
        epsilon += least_common_bit

    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    with open("input.txt") as f:
        diagnostic_reports = [
            report for report in f.read().splitlines(False) if report.strip() != ""
        ]

    result = binary_diagnostic(diagnostic_reports)
    print(result)
