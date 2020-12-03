from part_1 import multiply_expense_report as part_1_solution
from part_2 import multiply_expense_report as part_2_solution

numbers = [1721, 979, 366, 299, 675, 1456]

def test_part_1_solution():
    assert part_1_solution(numbers) == 514579

def test_part_2_solution():
    assert part_2_solution(numbers) == 241861950
