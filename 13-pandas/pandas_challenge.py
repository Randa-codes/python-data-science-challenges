# pandas_challenge.py

# 📊 Challenge: Read CSV, calculate total value, and filter items

import pandas as pd

# Step 1: Create data and save it to a CSV file
data = {
    'Names': ['coffee machine', 'chair', 'mirror', 'lamp', 'fan'],
    'Prices': [5000, 500, 900, 700, 3000],
    'Quantities': [1, 10, 3, 2, 1]
}

df = pd.DataFrame(data)
df.to_csv("items.csv", index=False)

# Step 2: Read from the CSV file
items = pd.read_csv("items.csv")
print("📦 Items loaded from CSV:\n", items)

# Step 3: Calculate total value
items['Total Value'] = items['Prices'] * items['Quantities']

# Step 4: Filter items with total value > 1000 DZD
filtered_items = items[items['Total Value'] > 1000]
print("\n💰 Items with Total Value > 1000 DZD:\n", filtered_items)
