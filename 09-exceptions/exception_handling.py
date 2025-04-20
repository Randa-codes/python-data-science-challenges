# exception_handling.py

# 🚨 Mini Challenge: Exception Handling

try:
    number1 = float(input("🔢 Enter number 1: "))
    number2 = float(input("🔢 Enter number 2: "))
    result = number1 / number2
    print("✅ Result:", result)

except ZeroDivisionError:
    print("❌ You cannot divide by zero.")

except ValueError:
    print("⚠️ Please enter valid numbers only.")

finally:
    print("🏁 Challenge done.")
