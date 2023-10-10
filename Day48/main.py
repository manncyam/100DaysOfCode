from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

events_dict = {}
try:
    for i in range(len(event_times)):
        date = event_times[i].get_dom_attribute("datetime").split("T")[0]
        name = event_names[i].text
        events_dict[i] = {"time": date, "name": name}

    pprint(events_dict)
except:
    pass

driver.quit()