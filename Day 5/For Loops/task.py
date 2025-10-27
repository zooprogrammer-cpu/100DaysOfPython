fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)


student_scores = [23, 45, 7]

print(sum(student_scores))
print(max(student_scores))


highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score is {highest_score}")

# Range function - does not include 10
for num in range(1,10):
    print(num) # prints 1,2,3,4,5,6,7,8,9
# option to change the steps-
for num in range(1,10,3):
    print(num) # prints 1,4,7

# Gauss Challenge-
sum = 0
for num in range(1,101):
    sum+= num
print(sum) # prints 5050

# Fizz Buzz
for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)

