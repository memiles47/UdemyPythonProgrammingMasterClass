__author__ = "Michael E Miles"


def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers together.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence. If you pass
    a string for example as the first argument, you'll get
    the string repeated 'y' times as the returned value.

    :param x: First number to multiply
    :param y: The number to multiply 'x' by
    :return: The product of 'x' and 'y'
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Determine if a string is a palindrome.

    Accepts input string and compares the original string
    to the reversed string. Input string is not case sensitive.

    :param string: The string to check
    :return: True if string is a palindrome, False otherwise
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Prepare input string as a sentence for `is_palindrome`.

    Remove all non alphanumeric characters from input sentence.
    Call `is_palindrome` function with resulting string.

    :param sentence: Sentence to check.
    :return: True if sentence is a palindrome, False otherwise
    """
    check_string = ""
    for char in sentence:
        if char.isalnum():
            check_string += char

    return is_palindrome(check_string)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

# word = input("Please enter a work to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# sentence = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("'{}' is a palindrome".format(sentence))
# else:
#     print("'{}' is not a palindrome".format(sentence))
