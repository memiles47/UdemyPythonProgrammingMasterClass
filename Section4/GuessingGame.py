__author__ = "Michael E Miles"
import random
highest = 10
countOfGuesses = 1
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}, enter 0 to quit: ".format(highest))
guess = int(input())

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
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed in {} guesses, the answer was {}".format(countOfGuesses, answer))
        break
# endregion
