# quotes_scraper.py

import requests
from bs4 import BeautifulSoup

# Step 1: Download the HTML content
url = 'http://quotes.toscrape.com'
html = requests.get(url).text

# Step 2: Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Step 3: Extract quotes and authors
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f'📝 {text} ---> 💬 {author}')
