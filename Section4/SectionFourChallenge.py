__author__ = "Michael E Miles"
options = ["Update Resume'", "Apply for Unemployment", "Learn Python",
           "Work in Blender", "Make Dinner", "Go to bed", "Play Chess",
           "Play Sudoku", "Order out"]
option_high = 9
choice = 100

while choice != 0:
    if 1 <= choice <= option_high:
        print("You chose to {}, option {}".format(options[choice - 1],
                                                  choice))
    else:
        print("Please choose your option from the list below\n")
        for i in range(1, option_high + 1):
            print("{}:\t{}".format(i, options[i - 1]))
        print("0:\tExit")

    choice = int(input("\nPlease enter you choice (1 - {}, 0 to exit): "
                       .format(option_high)))
