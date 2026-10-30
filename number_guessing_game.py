import random

logo=r"""                                 __  __                                  __             
   ____ ___  _____  __________   / /_/ /_  ___     ____  __  ______ ___  / /_  ___  _____
  / __ `/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/
 / /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / / / / /_/ / / / / / / /_/ /  __/ /    
 \__, /\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/     
/____/                                                                                    
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def play_game():
    selected_number=random.randint(1,100)
    
    if input("Choose a difficulty. Type 'easy' or 'hard': ").lower()=="easy":
        attempts=10
    else:
        attempts=5
    
    is_game_over=False
    while not is_game_over:
            print(f"You have {attempts} attempts remaining to guess the number")
            your_guess=int(input("Make a guess: "))
            if your_guess==selected_number:
                is_game_over=True
                print(f"You got it!The answer was {selected_number}")
            else:
                if your_guess<selected_number:
                    print("Too low.")
                elif your_guess>selected_number:
                    print("Too high.")
            
                attempts-=1
                if attempts!=0:
                    print("Guess again.")
                else:
                    is_game_over=True
                    print("You lose!")
            

while input("Do you want to play?type 'y' or 'n': ").lower()=="y":
    play_game()





