import requests
from bs4 import BeautifulSoup

# 1. Define the URL (the web address) you want to scrape
URL = "http://books.toscrape.com/"

# 2. Use the 'requests' library to download the webpage content
page = requests.get(URL)

# 3. Use 'BeautifulSoup' to parse (read) the downloaded content
soup = BeautifulSoup(page.content, "html.parser")

# 4. Find the first <h1> tag, which usually contains the main title
#    (This is the "scraping" part!)
main_heading = soup.find("h1")

# 5. Print the text contained within that tag
print(f"Webpage Title Found: {main_heading.text}")

print("\n--- Scraping Complete ---")

