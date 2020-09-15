__author__ = "Michael E Miles"
name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome to the holiday {}".format(name))
else:
    print("I'm sorry {}, you can not go on holiday at this time".format(name))
