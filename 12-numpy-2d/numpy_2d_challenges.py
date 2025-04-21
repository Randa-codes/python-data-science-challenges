# numpy_2d_challenges.py

# 🧮 Mini Challenge: NumPy – 2D Arrays

import numpy as np

# Create 2D array (3x3 matrix)
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("🔢 Matrix X:\n", x)

# Slice the first row
print("\n🔍 First row of X:", x[0][0:3])

# Create another 2D array
y = np.array([[10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]])
print("\n➕ Matrix Y:\n", y)

# Add two matrices
z = x + y
print("\n🧮 X + Y:\n", z)

# Multiply X by 2
u = x * 2
print("\n✖️ X multiplied by 2:\n", u)

# Matrix dot product
dot_product = np.dot(x, y)
print("\n📌 Dot Product of X and Y:\n", dot_product)

# Transpose of matrix X
p = x.T
print("\n🔄 Transpose of X:\n", p)
