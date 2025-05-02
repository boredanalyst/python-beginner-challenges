## This categorizes a user's age according to life stages



user_age = 0;

while user_age == 0:
    try:
        user_age = int(input("Hold old are you?: "))
    except:
        print("Please provide a valid age.")
        user_age = 0

if user_age >= 1 and user_age <= 12:
    print("You are a child.")
elif user_age >= 13 and user_age <= 19:
    print("You are a teenager")
elif user_age >= 20 and user_age <= 29:
    print("You are a young adult.")
elif user_age >= 40 and user_age <= 50:
    print("You are middle-aged.")
elif user_age >= 51:
    print("You are old.")