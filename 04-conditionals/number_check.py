# number_check.py

# 🔍 Mini Challenge: Conditionals & Branching

# Ask the user to input a number
number = float(input("Enter a number of your choice: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("✅ The number is positive.")
elif number == 0:
    print("⚠️ The number is zero.")
else:
    print("❌ The number is negative.")
