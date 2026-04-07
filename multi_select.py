from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://vallarasu.in/test/multi-select")

#//select[@id='language_select']

element = driver.find_element(By.XPATH, "//select[@id='language_select']")
language_select = Select(element)

language_select.select_by_value("2")
language_select.select_by_value("3")

language = []

assert len(language_select.all_selected_options) == 2

for i in language_select.all_selected_options:
    language.append(i.text)

assert "Telugu" in language
assert "Malayalam" in language

time.sleep(10)
