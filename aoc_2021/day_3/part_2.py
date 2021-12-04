from collections import Counter
from typing import List


def __common_bit(bits: List, how: str) -> str:
    common_bit = ""
    frequency = Counter(bits).most_common()
    most_common_tuple = frequency[0]  # (key, frequency)
    least_common_tuple = frequency[-1]  # (key, frequency)

    if how == "most":
        if most_common_tuple[1] == least_common_tuple[1]:
            common_bit = "1"
        else:
            common_bit = most_common_tuple[0]
    elif how == "least":
        if most_common_tuple[1] == least_common_tuple[1]:
            common_bit = "0"
        else:
            common_bit = least_common_tuple[0]

    return common_bit


def dianose_rating(diagnostic_reports: List[str], idx: int, how: str) -> str:
    if len(diagnostic_reports) == 1:
        return diagnostic_reports[0]

    bits = []
    for report in diagnostic_reports:
        bits.append(report[idx])
    common_bit = __common_bit(bits, how=how)

    diagnostic_reports = [
        report for report in diagnostic_reports if report[idx] == common_bit
    ]

    return dianose_rating(diagnostic_reports, idx + 1, how)


def life_support_rating(diagnostic_reports: List[str]) -> int:
    o2 = int(dianose_rating(diagnostic_reports, 0, "most"), 2)
    co2 = int(dianose_rating(diagnostic_reports, 0, "least"), 2)

    return o2 * co2


if __name__ == "__main__":
    with open("input.txt") as f:
        diagnostic_reports = [
            report for report in f.read().splitlines(False) if report.strip() != ""
        ]

    result = life_support_rating(diagnostic_reports)
    print(result)
