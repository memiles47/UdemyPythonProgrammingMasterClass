__author__ = "Michael E Miles"
answer = 5
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Pleas guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you have not guessed correctly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you have not guessed correctly")
else:
    print("You got it the first time")
