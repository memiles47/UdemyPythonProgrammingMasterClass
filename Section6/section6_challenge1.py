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


input("Play Fizz Buzz, press enter to continue.")
print()

while count < 101:
    print(fizz_buzz(count))
    player_guess = input("Your turn: ")
    if player_guess != fizz_buzz(count + 1):
        print("You loose, you should have entered {}."
              .format(fizz_buzz(count + 1)))
        break
    count += 2
else:
    print("Congratulation we made it")

