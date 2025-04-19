# file_handling.py

# 📁 Mini Challenge: File Handling
# Write a list of favorite foods to a file, then read it back

# List of favorite foods
foods = ["Pizza", "Couscous", "Sushi", "Chakchouka", "Tajine"]

# Write foods to a file
with open("favorite.food.txt", "w") as file:
    for food in foods:
        file.write(food + "\n")

# Read the entire file content at once
print("📖 Reading full file with .read():")
with open("favorite.food.txt", "r") as file:
    content = file.read()
    print(content)

# Read the file line by line and strip newlines
print("📄 Reading file line by line with .strip():")
with open("favorite.food.txt", "r") as file:
    for line in file:
        print("🍽️", line.strip())
