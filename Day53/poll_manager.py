""" 
Manages the submission of data into the google form
"""
import os
from bs4 import BeautifulSoup
from selenium import webdriver

path = os.environ["CHROME_DRIVER_PATH"]


class PollManager:
    def read_web_file(file, url):
        """
        If web file does not exist, then retrieve web page\n
        Open web file and return a BeautifulSoup object (HTML)

        :param file:  file where web page is saved
        :param url:  URL of web page to retrieve
        :return: HTML soup
        """
        try:
            open(file)
        except FileNotFoundError:
            get_web_page(file, url)
        else:
            pass
        finally:
            # Read the web page from file
            with open(file, mode="r", encoding="utf-8") as fp:
                content = fp.read()
            return BeautifulSoup(content, "html.parser")

    def get_web_page(file, url):
        """
        Retrieve requested web page\n
        Render in browser to execute the page's JavaScript\n
        Save the rendered web page to web file

        :param file: file where web page is saved
        :param url: URL of web page to retrieve
        :return: nothing
        """

        chrome_driver_path = path
        driver = webdriver.Chrome(executable_path=chrome_driver_path)

        driver.get(url)
        go = input(
            "Allow the page to completely render in the browser.\nEnter Y to save the web page! "
        ).lower()
        if go == "y":
            html_source = driver.page_source
            # Save web page to file
            with open(file, mode="w", encoding="utf-8") as fp:
                fp.write(html_source)

    # Use BeautifulSoup to retrieve the Zillow web page
    soup = read_web_file(file=WEB_FILE, url=ZILLOW_URL)
