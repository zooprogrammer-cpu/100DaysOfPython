import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))


if user_input == 0:
    print(f"You chose: {game_images[0]}")
elif user_input == 1:
    print(f"You chose: {game_images[1]}")
elif user_input == 2:
    print(f"You chose: {game_images[2]}")
else:
    print("You have an invalid selectio. You lose!")


computer_input = random.randint(0,2)

print(f"Computer chose: {game_images[computer_input]}")

if user_input > 3 or user_input < 0:
    print("You have an incorrect input. You lose!")
elif user_input == 0 and computer_input == 2:
    print("You win!")
elif user_input == 2 and computer_input == 0:
    print("You lose!")
elif computer_input > user_input:
    print("You lose!")
elif user_input > computer_input:
    print("You win!")
elif computer_input == user_input:
    print("It's a Draw!")




