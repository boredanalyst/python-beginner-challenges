## Add an item to a shopping list if it doesn't exist yet.

shopping_list = ["apple"]

item_to_add = input("Please input the item you want to add: ")
if item_to_add in shopping_list:
    print("This item is already in the shopping list!")
else:
    shopping_list.append(item_to_add)
    print("The new item has been added")
    print(shopping_list)


