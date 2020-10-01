__author__ = "Michael E Miles"
low = 1
high = 1000
print("please think of a number between {} and {}".format(low, high))
input("Press <ENTER> to start")

guess = 1
while True:
    guess = low + (high - low) // 2
    highLow = input("My guess is {}. Should I guess higher or lower? "
                    "Enter h or l, or c if my guess was correct"
                    .format(guess)).casefold()

    if highLow == "h":
        print()  # Guess higher. The low end of the range becomes 1 greater than the guess.

    elif highLow == "l":
        print()  # Guess lower. The high end of the range becomes one less than the guess.

    elif highLow == "c":
        print("I got it in {} guesses!".format(guess))

    else:
        print("Please enter h, l or c")
