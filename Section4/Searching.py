__author__ = "Michael E Miles"
shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
itemToFind = "spam"
# itemToFind = "albatross"
foundAt = None

# for index in range(6)
# for index in range(len(shoppingList)):
#     if shoppingList[index] == itemToFind:
#         foundAt = index
#         break

if itemToFind in shoppingList:
    foundAt = shoppingList.index(itemToFind)

if foundAt is not None:
    print("Item {} found at position {}".format(itemToFind, foundAt))
else:
    print("{} not found".format(itemToFind))
