## Add more and more toppings to the pizza.

pizza_toppings = []

active = True
while active:
    print("## --------- ##")
    topping = input("Please choose your topping: ")

    if topping != "quit":
        print(f'{topping} has been added!')
        pizza_toppings.append(topping)
        

    elif topping.lower() == "quit":
        print("--- END ---")
        active = False

    else:
        active = False
        break
        
## finalize the list of toppings.
print("## ---------- ##")
print("Here are your toppings:")

for tops in pizza_toppings:
    print(tops)

