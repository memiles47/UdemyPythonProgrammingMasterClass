__author__ = "Michael E Miles"
import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping and prompting
    the user until a valid `int` is entered.

    :param prompt: The String that the user will see when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{} is not a valid number".format(temp))


highest = 1000
countOfGuesses = 1
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}, enter 0 to quit: "
      .format(highest))
guess = get_integer(": ")

# region Second Iteration
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")
# endregion

# region First Iteration
# if guess < answer:
#     print("Pleas guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# else:
#     print("You got it the first time")
# endregion

# region Challenge
if guess == answer:
    print("You got it first time")

while guess != answer:
    countOfGuesses += 1
    if guess == 0:
        print("You quit the program")
        break
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than answer
        print("Please guess lower")
    guess = get_integer(": ")
    if guess == answer:
        print("Well done, you guessed in {} guesses, the answer was {}".format(countOfGuesses, answer))
        break
# endregion
