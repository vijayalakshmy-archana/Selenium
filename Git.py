from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://github.com/VallarasuS/py-selenium")
time.sleep(5)
driver.maximize_window()
search = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Go to file']")
search.click()
search.send_keys("readme")
result = driver.find_element(By.CSS_SELECTOR, "#file-result-0")
#result = chrome.find_element(By.ID, 'file-result-0')
result.click()
time.sleep(10)
name = driver.find_element(By.XPATH, "//h3[@class='heading-element' and text()= 'CSS']")
if name.text == "CSS":
    print("success")
else:
    print("fail")


#print(name.text)

