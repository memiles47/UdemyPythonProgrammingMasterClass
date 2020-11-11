__author__ = "Michael E Miles"
count = 1


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


# for value in range(1, 101):
#     fizz_buzz(value)
while count < 101:
    print(fizz_buzz(count))
    count += 1
    player_guess = input("Please enter fiz, buzz, fiz buzz or count: ")
    if player_guess != fizz_buzz(count):
        print("You loose, you should have entered {}."
              .format(fizz_buzz(count)))
        break
    else:
        count += 1
else:
    print("Congratulation we made it")

