""" 
This program checks your internet speed and tweets at your internet provider if the speed is below
the promised speed.
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Optional - Automatically keep your chromedriver up to date.
from webdriver_manager.chrome import ChromeDriverManager

# measure speeds
PROMISED_DOWN = 150
PROMISED_UP = 10

# get environment variables
CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]

# set up selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
ser = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=ser, options=options)
chrome_driver_path = ChromeDriverManager(path=CHROME_DRIVER_PATH).install()


class InternetSpeedTwitterBot:
    """A class to represent a bot that checks your internet speed and tweets at your provider if it is below the promised speed."""

    # initialize the bot
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0
        self.opt = Options()
        self.opt.headless = True
        self.chrome_driver_path = CHROME_DRIVER_PATH
        self.ser = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.ser)

    # get the internet speed
    def get_internet_speed(self):
        """Gets the internet speed and stores it in the up and down attributes."""
        self.driver.get("https://www.speedtest.net/")
        accept_button = self.driver.find_element(
            by=By.ID, value="_evidon-banner-acceptbutton"
        )
        accept_button.click()
        time.sleep(3)

        go_button = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".start-button a"
        )
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span',
        ).text
        self.down = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span',
        ).text
        self.driver.quit()
        self.driver1 = webdriver.Chrome(service=self.ser)

    def tweet_at_provider(self):
        """sends a tweet to your internet provider if your internet speed is below the promised speed."""
        self.driver1.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver1.find_element(
            by=By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input',
        )
        password = self.driver1.find_element(
            by=By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input',
        )
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_compose = self.driver1.find_element(
            by=By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div',
        )
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver1.find_element(
            by=By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]',
        )
        tweet_button.click()
        time.sleep(5)
        self.driver1.quit()


#  run the bot
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

# get the internet speed
bot.get_internet_speed()

# tweet at the provider if the speed is below the promised speed
bot.tweet_at_provider()
