# numpy_1d_challenges.py

# 🧮 Mini Challenge: NumPy 1D Arrays

import numpy as np

# Create a 1D array
a = np.array([1, 2, 3, 4, 5])
print("🔢 Original array:", a)

# Add 5 to each element
b = a + 5
print("➕ Array after adding 5:", b)

# Multiply each element by 2
c = a * 2
print("✖️ Array after multiplying by 2:", c)

# Calculate statistics
mean = a.mean()
print("📊 Mean:", mean)

a_max = a.max()
print("⬆️ Max value:", a_max)

a_min = a.min()
print("⬇️ Min value:", a_min)

std_dev = a.std()
print("📈 Standard Deviation:", std_dev)
