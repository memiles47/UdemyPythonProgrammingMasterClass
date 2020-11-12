__author__ = "Michael E Miles"
numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")


def test_star(*args: any) -> None:
    """
    Print arguments.
    :param args: items to print
    :return: None
    """
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
