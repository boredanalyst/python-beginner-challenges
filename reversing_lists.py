print("Reversing a list without using the .reverse method.")

colors = ["red","orange","yellow","green","blue","purple"]
reverse_list = []

for color in colors:
    reverse_list.insert(0,color)

print(colors)
print(reverse_list)