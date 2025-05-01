## Transfer element from one list to another list.

# Source of information
fruit_basket = ["orange", "apple", "grapes", "banana"]
print("FRUIT BASKET")
for fruit in fruit_basket:
    print(fruit)

# Destination
fruit_storage = []

while len(fruit_basket) != 0: 
    fruit_to_transfer = fruit_basket.pop() ## Get the last fruit from the fruit_basket
    fruit_storage.append(fruit_to_transfer) ## Transfer the fruit_to_transfer to the fruit_storage

print("\n##---##\n")
print("The fruit basket contents have been transferred to the storage.")

print("FRUIT STORAGE")
for fruit in fruit_storage:
    print(fruit)