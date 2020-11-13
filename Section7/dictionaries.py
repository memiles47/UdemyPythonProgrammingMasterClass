__author__ = "Michael E Miles"
fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "for for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         }

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# fruit.clear()
# print(fruit)
# print(fruit["tomato"])
print(fruit)

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a {}".format(dict_key))
