# httpbin_post_challenge.py

# 📬 Mini Challenge: POST Request with Form Data

import requests

# Step 1: Set the URL
url = "https://httpbin.org/post"

# Step 2: Define the form data (the information you want to send)
form_data = {
    "name": "Lisa",
    "favorite_color": "Blue"
}

# Step 3: Send a POST request with the form data
response = requests.post(url, data=form_data)

# Step 4: Print the full JSON response (optional)
print("📡 Full Response JSON:")
print(response.json())

# -------- STRETCH GOAL --------
# Step 5: Print only the 'form' part of the response (what we sent)
print("\n🎯 Data we sent (from 'form'):")
print(response.json()['form'])

