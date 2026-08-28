from bs4 import BeautifulSoup

import requests
search_term = input("Enter the product you want to search for: ")
html_text = requests.get(f'https://mdcomputers.in/?route=product/search&search={search_term}').text
print(html_text);
