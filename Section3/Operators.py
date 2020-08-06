__author__ = "Michael E Miles"
a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4
print(a // b)   # 4.0 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division

print()

for i in range(1, a // b):  # Using integer division will work as if using/
    # the number 4 but using regular division / would result in a float and/
    # produce an error
    print(i)
