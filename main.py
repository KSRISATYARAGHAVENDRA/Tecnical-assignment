from bs4 import BeautifulSoup
from urllib.parse import quote

import requests
search_term = input("Enter the product you want to search for: ")
search_term = quote(search_term)
html_text = requests.get(f'https://mdcomputers.in/?route=product/search&search={search_term}').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_='retrinapro-productlist-all_products_design col-lg-3 col-md-4 col-6 col-sm-6 px-0')
for product in products:
    product_name = product.find('h3', class_='product-entities-title').text
    Original_amount = product.select("span.price span.amount")[0].text.strip()
    discount_amount = product.select("span.price span.amount")[1].text.strip()
    print(f'Product: {product_name}')
    print(f'Original Price: {Original_amount}')
    print(f'Discount Price: {discount_amount}')
    print('-----------------------------------')