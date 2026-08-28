**Breif Description :**
  This Python web scraper takes a product name from the user, searches for it on the
  MDComputers website, and extracts product names and prices from the search
  results. It uses Requests to fetch the webpage and BeautifulSoup to parse the
  HTML content. The program also handles request failures and displays a message
  when no products are found.

**Prerequisites :**
  Python 3.x installed.
  VS Code or any Python IDE.
  Install the required Python libraries:
    requests 
    beautifulsoup4 
    lxml
  Internet connection to access the MDComputers website
  Basic knowledge of Python, HTML, and web scraping.

**Installation / Setup Instructions :**
  Install Python 3.x and verify:
    python --version
  Install the required libraries:
    pip install beautifulsoup4
    pip install requests
    pip install lxml
  Create a Python file :
    ex : main.py
  Add the scraper code to the file.
  Run the program:
    python main.py
  Enter a product name when prompted :
    ex : external hard drive 
  Internet connection is required

**Example input/output :**
  Input:
    Enter the product you want to search for: external hard drive
  output :
    Product: Seagate 1TB External Hard Disk
    Actual Price: ₹5,499
    Selling Price: ₹4,799

  ----------------------------
    Product: WD 2TB External Hard Disk
    Actual Price: ₹7,999
    Selling Price: ₹6,999

  Input :
    Enter the product you want to search for: pencil
  Output :
    No products found for the search term.

  Input :
    Enter the product you want to search for: external hard drive
  Output :
    Error fetching the webpage: Request timed out
  #This happens when the server takes too long to respond.

**Dependencies :**
Python 3.x
Requests – Used to send HTTP requests and fetch the webpage.
BeautifulSoup4 – Used to parse and extract data from HTML.
lxml – Used as the HTML parser for BeautifulSoup.

**Assumptions / Limitations :**
The MDComputers website is accessible and its HTML structure remains unchanged.
The scraper depends on specific HTML tags and CSS classes to extract product details.
Products must be available on the website for results to be displayed.
The program only extracts the product name, actual price, and selling price.
Changes to the website's layout or HTML structure may cause the scraper to stop working.

    

