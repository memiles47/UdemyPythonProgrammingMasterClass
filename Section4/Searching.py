__author__ = "Michael E Miles"
shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
itemToFind = "spam"
foundAt = None

# for index in range(6)
for index in range(len(shoppingList)):
    if shoppingList[index] == itemToFind:
        foundAt = index
        break

print("Item found at postion {}".format(foundAt))
