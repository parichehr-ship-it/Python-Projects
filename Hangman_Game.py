import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''' ]

word_list = ["banana", "apple", "orange", "pear"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
end_of_game = False

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Please enter a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Print the updated display after checking all positions
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You have {lives} chances left.")
        
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Print the current hangman stage based on remaining lives
    print(stages[lives])


