## Remove rotten items from an inventory dictionary.

fruit_storage = {
    "apple" : "Slightly fresh",
    "banana" : "Rotten",
    "orange" : "Fresh",
    "grapes" : "Slightly fresh",
    "melon" : "Rotten",
    "dragonfruit" : "Slightly fresh",
    "wintermelon" : "Fresh"
} ## This is the fruit storage.

new_fruit_storage = {}

print("\n## ------ ##\n")
print("FRUIT STORAGE ----- ##")
for fruit in fruit_storage.keys():
    print(f'FRUIT: {fruit.upper()} STATUS: {fruit_storage[fruit]}')

for fruit in fruit_storage.keys():
    if fruit_storage[fruit] != "Rotten":
        new_fruit_storage[fruit] = fruit_storage[fruit]

print("\n### =------- ###\n")
print("FRESH FRUITS")

new_fruit_storage = dict(sorted(new_fruit_storage.items()))

for fruit in new_fruit_storage.keys():
    print(f'FRUIT: {fruit.upper()} STATUS: {new_fruit_storage[fruit]}')