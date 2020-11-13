__author__ = "Michael E Miles"
fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "for for making cider",
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

for i in range(10):
    for snack in fruit:
        print("{} is {}".format(snack, fruit[snack]))
    print('-' * 40)
