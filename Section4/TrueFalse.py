__author__ = "Michael E Miles"
# region First Part of lesson
day = "Saturday"  # String variable
temperature = 30  # Integer variable
raining = True  # Boolean variable

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")
# endregion
if 0:
    print("Ture")
else:
    print("False")

name = input("Please enter your name: ")
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are the name with no name?")
