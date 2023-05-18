from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
ser = Service("/Users/jmb2393/Development/chromedriver")
driver = webdriver.Chrome(service=ser, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# get the div containing the article count
# article_count = driver.find_element(By.ID, "articlecount")

# # get the anchor tag inside the article count:
# link = article_count.find_element(By.TAG_NAME, "a")
# print(link.text)

# searching with selenium
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.close()  # close current tab6
driver.quit()  # quits the whole browser
