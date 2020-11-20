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


def print_separator() -> None:
    """
    Prints 40 '*' with a blank line before and after.
    :return:
    """
    print()
    print("*" * 40)
    print()


def create_even_set() -> set:
    """
    Create a `set` of even numbers from 0 to 40.

    :return: Set of even numbers.
    """
    even_set = set(range(0, 40, 2))
    return even_set


def create_squares_set() -> set:
    """
    Creates a `set` of squares {4, 6, 9, 16, 25}.

    :return: Set of squares
    """
    squares_set_tuple = (4, 6, 9, 16, 25)
    squares_set = set(squares_set_tuple)
    return squares_set
