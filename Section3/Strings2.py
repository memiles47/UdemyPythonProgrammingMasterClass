__author__ = "Michael E Miles"
#
#         01234567890123
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[0:6])  # Norweg
print(parrot[-14:-8])

print(parrot[0:6:2])  # Nre
print(parrot[:6:3])  # Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

# Example and not part of this lesson
values = "".join(char if char not in separators
                 else " " for char in number).split()
print([int(val) for val in values])
