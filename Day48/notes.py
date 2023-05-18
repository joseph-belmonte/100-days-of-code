from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("/Users/jmb2393/Development/chromedriver")
driver = webdriver.Chrome(service=ser)

driver.get("https://www.python.org/")
# driver.close()  # close current tab
# driver.quit()  # quits the whole browser

# how to use selenium to locate specific elements
# driver.get(
#     "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/"
# )

# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# # print("Check", price.tag_name)
# print(price.get_attribute("innerHTML"))

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = {}

for event in range(0, len(event_times)):
    events[event] = {
        "time": event_times[event].text,
        "name": event_names[event].text,
    }

print(events)

driver.quit()
