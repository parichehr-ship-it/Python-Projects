alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define the caesar function outside the loop for better practice
def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
        
    for char in start_text:
        if char in alphabet:
            current_index = alphabet.index(char)
            new_index = current_index + shift_amount
            new_letter = alphabet[new_index]
            end_text += new_letter
        else:
            # Keep spaces and symbols unchanged
            end_text += char
            
    # Print the final result once the loop is done
    print(f"The {cipher_direction}d text is: {end_text}\n")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # Handle shifts larger than 26
    shift = shift % 26

    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)
    
    result = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye.")