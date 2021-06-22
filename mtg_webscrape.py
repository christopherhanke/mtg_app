import time
import datetime

from selenium import webdriver
from bs4 import BeautifulSoup


def search():
    """search and print infos for cards given."""

    # setting up the browser, headless mode deactivates displaying browser.
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    browser = webdriver.Chrome(executable_path=PATH, options=options)

    # data for later URL
    base_url = "https://www.cardmarket.com/de/Magic/Cards/"
    filter_url = "?sellerCountry=7&language=1"

    # list of cards to search. names have to be in html notation.
    cards = [
        "Yavimaya-Cradle-of-Growth",
        "Misty-Rainforest",
        "Scalding-Tarn"
    ]

    today = datetime.date.today()
    print(today)

    # looping the cards in list and searching for the card and price infos.
    for card in cards:
        # setting up the url
        url = base_url + card + filter_url

        try:
            # calling the url
            browser.get(url)
            time.sleep(0.1)

            # searching the site for name of the card, the trend-price and offers.
            name = browser.find_element_by_css_selector("body > main > div.page-title-container.d-flex.align-items-center > div > h1")
            price = browser.find_element_by_css_selector('#info > div > dl > dd:nth-child(8) > span')
            table = browser.find_element_by_css_selector("#table > div > div.table-body")

            # splitting the table of offers in a list. searching for the first price in list.
            table_list = table.text.split("\n")
            for item in table_list:
                if "€" in item:
                    best_price = item
                    break
            
            print(f"{name.text} - Preistrend: {price.text} - Bester Preis: {best_price}")
        
        except Exception:
            print(f"There was an exception occuring, while searching for: {card}.")
        
    browser.quit()

# control execution
if __name__ == "__main__":
    print("Hello")
    search()
