import os

# Dictionary to store bids (name: price)
bids = {}
bidding_finished = False

while not bidding_finished:
    # Get bidder's name and bid amount
    name = input("Please enter your name: ")
    price = int(input("What is your bid? $ "))
    
    # Add the new bid to the dictionary
    bids[name] = price

    # Check if there are more bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    if should_continue == "no":
        bidding_finished = True
        best_price = 0
        winner = "" # Initialize winner to avoid errors
        
        # Loop through the dictionary to find the highest bid
        for bidder in bids:
            bids_amount = bids[bidder]
            if bids_amount > best_price:
                best_price = bids_amount
                winner = bidder
                
        # Announce the winner
        print(f"The winner is {winner} with {best_price} dollars.")
        
    elif should_continue == "yes":
        # Clear the console screen for the next bidder (works on Windows and Mac/Linux)
        os.system('cls' if os.name == 'nt' else 'clear')



