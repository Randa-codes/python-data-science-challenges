# 🌐 REST APIs – GET Request Challenge

This folder contains a mini challenge where I use Python's `requests` library to send GET requests to a public test API.

## 💪 Challenge:
- Send a basic GET request to `https://httpbin.org/get`
- Print the server's JSON response

## 🚀 Stretch Goal:
- Send a GET request with query parameters:
  - `name=Lisa`
  - `age=30`
- Use the `params` argument in `requests.get(...)`
- Print both the JSON response and the full URL sent

## ✅ Output Example:
```json
{
  "args": {
    "name": "Lisa",
    "age": "30"
  },
  "url": "https://httpbin.org/get?name=Lisa&age=30",
  ...
}

>This challenge helped me practice how to interact with public APIs using GET requests and query strings.
