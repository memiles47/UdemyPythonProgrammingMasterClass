__author__ = "Michael E Miles"
def fizz_buzz(number: int) -> str:
    """
    Returns the string fizz if number divisible by 3, buzz if divisible
    by 5, fizz buzz if divisible by both otherwise returns the number
    as a string.

    :param number: `int` value to check
    :return: string, fizz, buzz, fizz buzz or number as a `string`
    """
    string = ""
    if number % 3 != 0 and number % 5 != 0:
        return str(number)
    elif number % 3 == 0:
        string += "fizz"
        if number % 5 == 0:
            string += " buzz"
    else:
        string = "buzz"
    return string


for value in range(1, 101):
    fizz_buzz(value)

