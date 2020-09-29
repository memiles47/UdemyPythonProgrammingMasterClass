__author__ = "Michael E Miles"
availableExits = ["north", "south", "east", "west"]
chosenExit = ""
while chosenExit not in availableExits:
    chosenExit = input("Please choose a direction: ")
    if chosenExit.casefold() == "quit":
        print("Game over")
        break

print("aren't you glad you got out of there")
