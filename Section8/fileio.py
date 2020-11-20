__author__ = "Michael E Miles"
from functions import print_separator

jabber = open("sample.txt",'r')

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()

print_separator()

# Using `with` automatically closes the file if that file supports
# without the need for the .close() method.
with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

print_separator()

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

print_separator()

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)
print()

for line in lines:
    print(line, end='')

print_separator()

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)
print()

for line in lines[::-1]:
    print(line, end='')

print_separator()

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')
