__author__ = "Michael E Miles"
from functions import print_separator

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
# print(lines)

for line in lines:
    print(line, end='')

print_separator()

for line in lines[::-1]:
    print(line, end='')

print_separator()

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()
# print(lines)

for line in lines[::-1]:
    print(line, end='')