"""
This module will pull be used to interact with the zillow website.
"""
import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

zillow_url = os.environ["ZILLOW_URL"]
driver_path = os.environ["CHROME_DRIVER_PATH"]
options = webdriver.ChromeOptions()
options.add_argument("--star-maximized")
options.add_argument("--window-size=1440,1440")
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get(zillow_url)
time.sleep(4)

for _ in range(20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

html_data = driver.page_source
soup = BeautifulSoup(html_data, "html.parser")
property_list = soup.select("ul li article")
property_dict = {}

for n in enumerate(property_list):
    property_dict[n] = {
        "address": property_list[n].select_one("address").text,
        "price": property_list[n].select_one("div.list-card-price").text,
        "link": property_list[n].select_one("a.list-card-link").get("href"),
    }

driver.quit()


class ZillowDataManager:
    """
    Contains methods for requesting data from zillow
    """

    def __init__(self) -> None:
        """
        Create a new instance of the ZillowDataManager class
        """
        headers = {
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        }
        response = requests.get(zillow_url, headers=headers, timeout=5)
        response.raise_for_status()
        response_text = response.text
        self.soup = BeautifulSoup(response_text, "html.parser")
        self.address_links = []
        self.price_list = []

    def get_links(self):
        """
        Get the links to the zillow listings.
        Search for the HTML for anchor tags with tabindex="0". \n
        Put these into a list.

        :return: list of links
        """

        self.address_links = [a["href"] for a in self.soup.find_all("a", tabindex="0")]

        # catch the short links
        for index in enumerate(self.address_links):
            if not self.address_links[index].startswith("http"):
                self.address_links[index] = "https://www.zillow.com" + {
                    self.address_links[index]
                }

        # return the list of links
        return self.address_links

    def get_addresses(self, html):
        """
        Search the HTML for address tags with specific class.\n
        Form these into a list.

        :param html: the html section to be examined
        :return: list of addresses
        """
        address_list = [
            a.text for a in html.find_all("address", class_="list-card-addr")
        ]
        # print(f"list_addresses = {list_addresses}\n\n")

        return address_list

    def get_prices(self, html):
        """
        Search the HTML for div tags with specific class.\n
        Form these into a list.

        :param html: the html section to be examined
        :return: list of prices
        """
        price_list = [a.text for a in html.find_all("div", class_="list-card-price")]
        # print(f"list_cost = {list_cost}\n\n")

        return price_list
