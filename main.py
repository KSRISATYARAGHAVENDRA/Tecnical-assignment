from bs4 import BeautifulSoup
from urllib.parse import quote

import requests
search_term = input("Enter the product you want to search for: ")
search_term = quote(search_term)
html_text = requests.get(f'https://mdcomputers.in/?route=product/search&search={search_term}').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find('div', class_='retrinapro-productlist-all_products_design col-lg-3 col-md-4 col-6 col-sm-6 px-0')
product_name = soup.find('h3', class_='product-entities-title').text
amount = soup.select("span.price span.amount")[1].text.strip()
print(product_name)
print(amount)