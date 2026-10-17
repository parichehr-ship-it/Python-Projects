import random

choices = ["rock", "paper", "scissors"]

# Get user input
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))

# Check for invalid input
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose.")
else:
    print(f"You chose {choices[user_choice]}")
    
    # Generate computer choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {choices[computer_choice]}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    else:
        if user_choice == 0 and computer_choice == 1:
            print("You lose!")
        elif user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif user_choice == 1 and computer_choice == 0:
            print("You win!")
        elif user_choice == 1 and computer_choice == 2:
            print("You lose!")
        elif user_choice == 2 and computer_choice == 0:
            print("You lose!")
        elif user_choice == 2 and computer_choice == 1:
            print("You win!")
    


