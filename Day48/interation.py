from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://orteil.dashnet.org/experiments/cookie/"
options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=options)
driver.get(url=url)

cookie = driver.find_element(By.ID, "cookie")
now = start = time.time()

while True:
    current = time.time()
    cookie.click()
    if current - now > 120:
        now = current
        money = driver.find_element(By.ID, "money").text
        items = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for item in items[::-1]:
            try:
                item.click()
            except:
                pass

    if current - start > 300:
        break
cps = driver.find_element(By.ID, "cps").text
print(cps)
#driver.quit()