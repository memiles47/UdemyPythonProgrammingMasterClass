__author__ = "Michael E Miles"
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted("342985716")
print(digits)

another_digits = list("342985716")
print(another_digits)

more_numbers = list(numbers)
print(more_numbers)

print(numbers is more_numbers)
print(numbers == more_numbers)

more_numbers_again = numbers[:]
print(more_numbers_again)

more_numbers_dux = numbers.copy()
print(more_numbers_dux)
