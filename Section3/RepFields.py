__author__ = "Michael E Miles"
age = 24
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jam", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("THere are {0} days in Jan, Mar, Mar, Jul, Aug, Oct and Dec".format(31))

print("Jan: {2}\nFeb: {0}\nMar: {2}\nApr: {1}\nMay: {2}\nJun: {1}\n"
      "Jul: {2}\nAug: {2}\nSep: {1}\nOct: {2}\nNov: {1}\nDec: {2}"
      .format("28 or 29", 30, 31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format("28 or 29", 30, 31))
