__author__ = "Michael E Miles"
myList = ['a', 'b', 'c', 'd']
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

# newString = ''
# for c in myList:
#     newString += c + ", "

newString = ", ".join(myList)
newStringAgain = ", ".join(letters)
newNumbers = "-mississippi ".join(numbers)

print(newString)
print(newStringAgain)
print(newNumbers)
print(len(newNumbers))
