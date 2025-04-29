## Ask the player how many people will be seated.

guest_seat = 0.

while guest_seat == 0:
    guest_seat = input("How many poeple will be dining with us today?: ")
    try:
        guest_seat = int(guest_seat)
    except:
        print("Please provide a valid number.")
        guest_seat = 0

print("## ------ ##")

if guest_seat >= 8:
    print("I'm sorry, we don't have seats left.")
else:
    print("Let me take you to your seats.")