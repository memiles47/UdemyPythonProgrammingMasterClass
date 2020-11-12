__author__ = "Michael E Miles"


def factorial(value: int) -> int:
    """
    Find factorial of given number.

    :param value: number to find factorial
    :return: factorial of given number
    """
    if value == 0:
        return 1
    elif value == 1 or value == 2:
        return value
    else:
        new_value = 2
        for index in range(3, value +1):
            new_value *= index
    return new_value


for i in range(36):
    print("{} {}".format(i, factorial(i)))
