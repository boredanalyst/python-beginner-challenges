## Asking the user if they want a fruit.


## fruit name and stock available.
fruits = {
    "apple" : 12,
    "oranges" : 5,
    "banana" : 8,
    "grapes" : 15,
    "mango" : 21
}

fruit_input = input("What fruit are you interested in today?: ").lower()

print(f"I'll check if there is any {fruit_input} available.")

print("##------------##\n")

try:
    if (fruits.get(fruit_input) >= 10 ):
        print(f"There's a lot of {fruit_input} left!")
        print(f"Stock left: {fruits.get(fruit_input)}")
    elif (fruits.get(fruit_input) < 10):
        print(f"There's not a of {fruit_input} left.")
        print(f"Stock left: {fruits.get(fruit_input)}")
except:
    print("That fruit dies not exist in the fruit list.")