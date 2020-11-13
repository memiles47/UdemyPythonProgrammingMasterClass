__author__ = "Michael E Miles"
fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         }


print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a {}"
#                             .format(dict_key))
#     print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("we don't have a {}".format(dict_key))

# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print("{} is {}".format(snack, fruit[snack]))
#     print('-' * 40)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print("{} - {}".format(f, fruit[f]))

# for f in sorted(fruit.keys()):
#     print("{} - {}".format(f, fruit[f]))

# for val in fruit.values():
#     print(val)
#
# print(fruit.keys())
#
# print(fruit.values())
#
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

print()
print(fruit.items())

print()
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print("{} is {}".format(item, description))

print()
print(dict(f_tuple))
