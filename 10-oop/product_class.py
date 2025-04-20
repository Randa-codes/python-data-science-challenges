# product_class.py

# 🛒 OOP Challenge: Product class with discount

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"📦 Product: {self.name} | 💰 Price: {self.price} DZD")

    def app_discount(self, discount_percentage):
        discount = self.price * (discount_percentage / 100)
        self.price -= discount
        print(f"🎯 Discount applied: {discount_percentage}% | New Price: {self.price} DZD")


# Create an object from the class and test it
item1 = Product("Laptop", 5000)
item1.show_info()
item1.app_discount(20)
item1.show_info()
