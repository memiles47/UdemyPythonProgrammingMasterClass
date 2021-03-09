__author__ = "Michael E Miles"
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
# print(lines)

for line in lines:
    print(line, end='')
