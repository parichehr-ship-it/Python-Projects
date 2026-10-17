print("Welcome to the Tip Calculator!")

# Get user inputs with proper type casting
bill = float(input("What was the total bill? $\n"))
people = int(input("How many people to split the bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

# Calculate the tip amount and total bill
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# Calculate the amount each person needs to pay
bill_per_person = total_bill / people

# Using round() drops trailing zeros (e.g., 10.5 instead of 10.50).
# Using string formatting (.2f) ensures exactly two decimal places are always displayed.
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")