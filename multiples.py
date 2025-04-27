## Get the first 10 mulitple of any number. 

multipliers = [1,2,3,4,5,6,7,8,9,10]
output_numbers = []

## get the number from user


input_number = 0

while input_number == 0:
    try:
        input_number = input("Please provide your number: ")
        if int(input_number) >= 1:
            input_number = int(input_number)
            pass
        else:
            print("Please provide an valid integer.")
            input_number = 0
    except:
        print("Please input a valid integer.")
        input_number = 0

for number in multipliers:
    output_numbers.append(number * input_number)

print(output_numbers)