__author__ = "Michael E Miles"

def create_even_set():
    even_set = set(range(0, 40, 2))
    return even_set


def create_squares_set():
    squares_set_tuple = (4, 6, 9, 16, 25)
    squares_set = set(squares_set_tuple)
    return squares_set


# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("*" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
#
# print(farm_animals)
# print(wild_animals)
#
# empty_set = set()
# print(empty_set)
#
# empty_set_2 = {}
# empty_set.add("a")
# empty_set_2.add("a")

even = create_even_set()
print(even)
print(len(even))

squares = create_squares_set()
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print(squares.union(even))
print(len(squares.union(even)))

print("*" * 40)
print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

print()
print("*" * 40)
print()

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares - even))

print()
print("*" * 40)
print()

print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

even = create_even_set()
squares_tuple = create_squares_set()

print()
print("*" * 40)
print()

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))
print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

print()
print("*" * 40)
print()

squares.discard(4)
squares.remove(16)
squares.discard(8) #  no error even though 8 does not exist
print(squares)
if 8 in squares:
    squares.remove(8)

try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")
# squares.remove(8)   will be an error because 8 does not exist

even = create_even_set()
squares_tuple = create_squares_set()
squares.remove(9)
squares.remove(25)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")

even = frozenset(create_even_set())
print(even)
# even.add(3)  not possible with frozen set (immutable)

























