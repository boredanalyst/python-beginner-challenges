## Here is a list of numbers

number_list = [1,3,4,5,1,2,11,31,42,23,56,42,33,22,17,82]
even_number = []
odd_number = []

## get even numbers and add them to even numbers list

for number in number_list:
    if number%2 == 0:
        even_number.append(number)
print("These are even numbers:")
print(even_number)
print("## ---- ##")

## get odd numbers and add them to odd numbers list

for number in number_list:
    if number%2 != 0:
        odd_number.append(number)

print("These are odd numbers:")
print(odd_number)
print("## ---- ##")
