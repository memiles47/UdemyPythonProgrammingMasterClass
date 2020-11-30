__author__ = "Michael E Miles"

import shelve

with shelve.open("shelve_test") as fruit:
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour, yellow, citrus fruit"
    fruit["grape"] = "a small, sweet fruit growing in bunches"
    fruit["lime"] = "a sour, green, citrus fruit"

    # Within code block because as soon as the code block is exited the
    # shelve will be closed
    print(fruit["lemon"])
    print(fruit["grape"])

print()
print('=' * 40)
print()

with shelve.open("shelf_test") as fruit:
    fruit2 = {
        "orange": "a sweet, orange, citrus fruit",
        "apple": "good for making cider",
        "lemon": "a sour, yellow, citrus fruit",
        "grape": "a small, sweet fruit growing in bunches",
        "lime": "a sour, green, citrus fruit"
    }

print(fruit2["lemon"])
print(fruit2["grape"])

print(fruit2)
