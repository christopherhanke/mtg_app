import time, datetime
import json

from selenium import webdriver
from bs4 import BeautifulSoup


# list of cards to search. names have to be in html notation.
cards = [
    "Yavimaya-Cradle-of-Growth",
    "Misty-Rainforest",
    "Scalding-Tarn"
]

test_file = "test.json"


def setup_browser():
    """setting up the browser and return webdriver object."""
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = webdriver.ChromeOptions()
    # headless mode deactivates displaying browser.
    options.add_argument("headless")
    browser = webdriver.Chrome(executable_path=PATH, options=options)
    return browser


def search(card, browser):
    """
    search and print infos for card given.\n
    card = card name in HTML notation.\n
    browser = webdriver object
    """
    info = {}
    
    # data for later URL
    base_url = "https://www.cardmarket.com/de/Magic/Cards/"
    filter_url = "?sellerCountry=7&language=1"
    
    today = datetime.date.today()
    print(today)

    
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

        info[card] = {
            "name": name.text,
            "price": price.text,
            "best_price": best_price
        }
    
    except Exception:
        print(f"There was an exception occuring, while searching for: {card}.")
    finally:        
        browser.quit()
    
    return info


def save(file, card_infos):
    """
    saving data to file.\n
    file = string path/to/file\n
    card_infos = infos to save
    """
    try:
        with open(file, "w") as save_file:
            save_file.write(json.dumps(card_infos))
    except FileNotFoundError:
        print(f"File not found! - {file}")
    else:
        print(f"Data saved to: {file}")
    

# control execution
if __name__ == "__main__":
    card_infos = {}
    for card in cards:
        info = search(card, setup_browser())
        for key in info.keys():
            card_infos[key] = info[key]
    
    print(card_infos)
    save(test_file, card_infos)