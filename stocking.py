## Check the stock of items

inventory_list = {
    "apple" : 12,
    "orange" : 20,
    "banana" : 2,
    "grapes" : 4,
    "strawberry" : 10
}

for fruit in inventory_list.keys():
    if inventory_list[fruit] <= 10:
        print(f"There's around 10 or less units of {fruit}.")
        print(f"Please buy at least {20 - inventory_list[fruit]} units more.")
        print("## ----- ## \n")