__author__ = "Michael E Miles"

import pickle
from functions import print_separator

imelda = ("More Mayhem",
          "Imelda May",
          "2011",
          ((1, "Pulling the Rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish Town Waltz")
           ))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2