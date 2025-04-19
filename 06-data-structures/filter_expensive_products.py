# filter_expensive_products.py

# 📦 Mini Challenge: Data Structures (Dictionaries)

# Create a dictionary with products and their prices in DZD
products = {
    'lemon': 10,
    'car': 10000,
    'rice': 20,
    'coffee machine': 11000,
    'television': 20000
}

# Print only products that cost more than 1000 DZD
print("🛒 Products costing more than 1000 DZD:")
for product, price in products.items():
    if price > 1000:
        print(f"- {product}")
