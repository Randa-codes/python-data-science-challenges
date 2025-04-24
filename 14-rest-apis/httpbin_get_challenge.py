# httpbin_get_challenge.py

# 🌐 Challenge: Use requests to call https://httpbin.org/get

import requests

# Step 1: Set the URL of the API
url = 'https://httpbin.org/get'

# Step 2: Send a basic GET request (no extra data)
response = requests.get(url)

# Step 3: Print the JSON response (it tells us what the server sees)
print("🔹 Response from basic GET request:")
print(response.json())

# Step 4: Define query parameters using a dictionary
params = {
    "name": "Lisa",
    "age": 30
}

# Step 5: Send a GET request with query parameters
response = requests.get(url, params=params)

# Step 6: Print the JSON response that includes the parameters
print("\n🚀 Response from GET request with parameters:")
print(response.json())

# Step 7: Also print the full URL that was sent (includes the query string)
print("\n🌐 Full URL sent:")
print(response.url)
