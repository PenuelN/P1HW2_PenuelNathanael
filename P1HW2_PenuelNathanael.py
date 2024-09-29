# Nathanael Penuel
# 9/29/2024
# P1HW2 - Travel Expenses
# This program calculates and displays travel expenses.

# 1. Enter the total budget.
# 2. Enter the travel destination.
# 3. Enter the estimated cost of gas.
# 4. Enter the estimated cost of accommodation.
# 5. Enter the estimated cost of food.
# 6. Calculate the total expenses by adding gas, accommodation, and food costs.
# 7. Calculate the remaining balance by subtracting the total expenses from the budget.
# 8. Display the total expenses and show remaining balance.

# Asking for input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas? "))
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_expense = float(input("Last, how much do you need for food? "))

# Calculating 
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance = budget - total_expenses

# Displaying
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"Fuel: {gas_expense}")
print(f"Accommodation: {accommodation_expense}")
print(f"Food: {food_expense}")
print(f"\nRemaining Balance: {remaining_balance}")
