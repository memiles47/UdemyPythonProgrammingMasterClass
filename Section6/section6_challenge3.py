__author__ = "Michael E Miles"


def sum_numbers(*args: float) -> float:
    """
    Sum list of numbers

    :param args: list to sum
    :return: sum of `*args`
    """
    sum_of_args = 0
    for i in args:
        sum_of_args += i
    return sum_of_args


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
