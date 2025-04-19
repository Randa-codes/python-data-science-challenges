# loops_challenges.py

# 🔁 Mini Challenge: Loops (for and while)

print("🟦 Even numbers from 1 to 20 (using modulo):")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("\n🟩 Even numbers from 0 to 20 (step by 2):")
for i in range(0, 21, 2):
    print(i)

print("\n🔻 Countdown from 10 to 1 (using while loop):")
count = 10
while count >= 1:
    print(count)
    count -= 1

print("\n🟥 Odd numbers from 1 to 19 (step by 2):")
for i in range(1, 20, 2):
    print(i)

print("\n🟨 Odd numbers from 1 to 19 (using modulo):")
for i in range(1, 20):
    if i % 2 != 0:
        print(i)
