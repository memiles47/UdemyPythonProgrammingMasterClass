__author__ = "Michael E Miles"


def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string):
    check_string = ""
    for char in string:
        if char.isalnum():
            check_string += char

    return is_palindrome(check_string)


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

word = input("Please enter a work to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

sentence = input("Please enter a sentence to check: ")
if palindrome_sentence(sentence):
    print("'{}' is a palindrome".format(sentence))
else:
    print("'{}' is not a palindrome".format(sentence))
