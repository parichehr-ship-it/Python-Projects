print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# Get the first choice
left_right = input('You are at a crossroad. Where do you want to go? Type "left" or "right": ').lower()

if left_right == "left":
    # Get the second choice
    swim_wait = input('''You come to a lake. There is an island in the middle of the lake.
Type "wait" to wait for a boat. Type "swim" to swim across: ''').lower()
    
    if swim_wait == "wait":
        # Get the third choice
        door = input("""You arrive at the island unharmed. There is a house with three doors: 
one red, one blue, and one yellow. Which color do you choose?: """).lower()
        
        if door == "red":
            print("You enter a room full of fire. Game over.")
        elif door == "yellow":
            print("You find the treasure. You win!")
        elif door == "blue":
            print("You enter a room full of beasts. Game over.")
        else:
            print("You enter a color that doesn't exist. Game over.")
    else:
        print("You got attacked by a trout. Game over.")
else:
    print("You fell into a hole. Game over.")

