input_number = int(input("Enter a number to check if odd or even: "))

remainder = (input_number % 2)

if input_number % 2 == 0:
    print("You have an even number")
else:
    print("You have an odd number")