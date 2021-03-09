__author__ = "Michael E Miles"
#jabber = open("E:\\Repositories\\UdemyPythonProgrammingMasterClass\\Section8\\sample.txt", 'r')
#jabber = open("C:\\Users\\Michael\\OneDrive\\Desktop\\sample.txt", 'r')
jabber = open("sample.txt", 'r')

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()
