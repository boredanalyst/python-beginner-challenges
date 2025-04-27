## Guess an alien's color

import random as rd


color_list = ["RED","GREEN","YELLOW"]
alien_color = color_list[rd.randint(0,2)]

print("An alien has descended on earth!")
print("Guess the color of the alien!")

print("## ---- ##")
input_guess = input("What color is the alien? RED, YELLOW, or GREEN?: ").upper()

print(f'You guessed that the alien is: {input_guess}.')
print(f'The alien is: {alien_color}')
print("\n ## -------- ## \n")

if alien_color == input_guess:
    print("You guessed correct!")
else:
    print("You guessed incorrectly. Sorry!")
