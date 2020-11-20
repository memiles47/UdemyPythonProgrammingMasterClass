__author__ = "Michael E Miles"
# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

sampleText = "the quick brown fox jumps over the lazy dog"
vowels = frozenset("aeiou")

# vowels = {'a', 'e', 'i', 'o', 'u'}
# consonants = []

# for char in sampleText:
#     if char not in vowels and char != " ":
#         consonants.append(char)

consonants = set(sampleText).difference(vowels)

sorted_consonants = sorted(consonants)
print(sorted_consonants)
