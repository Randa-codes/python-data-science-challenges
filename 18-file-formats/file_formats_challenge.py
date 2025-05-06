# 📁 18-file-formats/file_formats_challenge.py

# JSON Challenge
import json

dic = {'name': 'Lisa', 'Age': 21}

# Write to JSON
with open('dic_json.json', 'w') as file:
    json.dump(dic, file, indent=4)

# Read from JSON
with open('dic_json.json', 'r') as file:
    loaded_dic = json.load(file)

print("✅ JSON Loaded:")
print(loaded_dic)

# CSV Stretch Goal
import pandas as pd

Products_data = {
    'Products': ['laptop', 'phone', 'tv', 'coffe machine'],
    'Prices': [2000, 1500, 5000, 3000],
    'Quantities': [2, 3, 1, 2]
}

# Create DataFrame
df = pd.DataFrame(Products_data)

# Save to CSV
df.to_csv('Products_total_prices.csv', index=False)

# Add Total Value column
df['Total Value'] = df['Prices'] * df['Quantities']

# Print the final table
print("\n💰 CSV Table with Total Value:")
print(df)
