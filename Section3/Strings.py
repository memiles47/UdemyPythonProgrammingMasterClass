__author__ = "Michael E Miles"

print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = "Michael"
print(greeting + name)

# if we want a space we can add that too
print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

ageInWords = "2 years"
print(age)
print(type(age))

# If you were to bind a string to age you would avoid an error in\
# the next statement
print(name + f" is {age} years old")

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
