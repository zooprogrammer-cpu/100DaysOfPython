

import random
friends_list = ["Alice", "Jonn", "Bob", "Tom"]

# Option #1
length_of_list = len(friends_list)
print(length_of_list)
random_number = random.randint(0,length_of_list-1)
print(random_number)

print(friends_list[random_number])

# Option #2
print(random.choice(friends_list))

