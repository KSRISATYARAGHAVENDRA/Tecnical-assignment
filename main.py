
from bs4 import BeautifulSoup
from urllib.parse import quote

import requests

search_term = input("Enter the product you want to search for: ")
search_term = quote(search_term) #to handle spaces and special characters

url = f"https://mdcomputers.in/?route=product/search&search={search_term}"

try:
    response = requests.get(url,timeout=10)

    response.raise_for_status()  # Raise an exception for HTTP errors

except requests.RequestException as error:
    print(f"Error fetching the webpage: {error}")
    exit()

html_text = response.text

soup = BeautifulSoup(html_text, 'lxml')

products = soup.find_all('div', class_='retrinapro-productlist-all_products_design col-lg-3 col-md-4 col-6 col-sm-6 px-0')

if not products:
    print("No products found for the search term.")

else:
    for product in products:
        product_name = product.find('h3', class_='product-entities-title').text
        Actual_price = product.select("span.price span.amount")[0].text.strip()
        Selling_price = product.select("span.price span.amount")[1].text.strip()
        print(f'Product: {product_name}')
        print(f'Actual Price: {Actual_price}')
        print(f'Selling Price: {Selling_price}')
        print('-----------------------------------')