## accept user response to create an order receipt


## Empty and default dictionary
shirt_order = {
    "size": "",
    "quantity" : 0,
    "color" : ""
}

## Ask for user input
size_order = input("What is the size of the shirt? ")

active = True
while active:
    try:
        qty_order = int(input("How many items do you need? "))
        active = False
    except:
        print("Please provide a valid number.")

color_order = input("What is the color of your shirt? ")

def printOrder():
    ## Append the user inputs to the dictionary of the shirt
    shirt_order["size"] = size_order
    shirt_order["quantity"] = qty_order
    shirt_order["color"] = color_order

    ## Print the user inputs
    print("\n### ------ ###\n")
    print(f'THESE ARE THE DETAILS OF YOUR ORDER:')
    print(f'SIZE: {shirt_order["size"].upper()}')
    print(f'SIZE: {shirt_order["quantity"]}')
    print(f'SIZE: {shirt_order["color"].upper()}')

printOrder()
    
