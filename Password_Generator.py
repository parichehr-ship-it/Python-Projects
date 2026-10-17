import random

# Define the characters to use
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# --- Easy Level ---
def generate_easy_password():
    print("--- Easy Password Generator ---")
    nr_letters = int(input("How many letters would you like?:\n "))
    nr_symbols = int(input("How many symbols would you like?:\n "))
    nr_numbers = int(input("How many numbers would you like?:\n "))

    password = ""
    for item in range(1, nr_letters + 1):
        password += random.choice(letters)
    for item in range(1, nr_symbols + 1):
        password += random.choice(symbols)
    for item in range(1, nr_numbers + 1):
        password += random.choice(numbers)
        
    print(f"Your easy password is: {password}\n")


# --- Hard Level (More Secure) ---
def generate_hard_password():
    print("--- Hard Password Generator ---")
    nr_letters = int(input("How many letters would you like?:\n "))
    nr_symbols = int(input("How many symbols would you like?:\n "))
    nr_numbers = int(input("How many numbers would you like?:\n "))

    password_list = []
    
    for item in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))
    for item in range(1, nr_symbols + 1):
        password_list.append(random.choice(symbols))
    for item in range(1, nr_numbers + 1):
        password_list.append(random.choice(numbers))

    # Shuffle the list to make the password more secure
    random.shuffle(password_list)

    # Join the list into a single string
    password = "".join(password_list)
    
    print(f"Your secure password is: {password}\n")

# --- Run the program ---
print("Welcome to the Password Generator!")
level = input("Which level do you want to try? Type 'easy' or 'hard': ").lower()

if level == "easy":
    generate_easy_password()
elif level == "hard":
    generate_hard_password()
else:
    print("Invalid choice. Please run the program again.")

