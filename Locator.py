from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

def open_chrome():
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(5)
    return chrome

def open_flipkart(chrome, url):
    chrome.get(url)
    time.sleep(5)

def close_icon(chrome):
    close = chrome.find_element(By.XPATH, "//span[@role='button' and text()='✕']")
    close.click()
    time.sleep(5)

def search_value(chrome):
    search = chrome.find_element(By.CSS_SELECTOR,"input[name='q']")
    search.send_keys("laptop")
    search.send_keys(Keys.ENTER)
    time.sleep(10)

def click_newest(chrome):
    newest = chrome.find_element(By.XPATH, "//div[text()='Newest First']")
    newest.click()
    time.sleep(5)

def product_name(chrome):
    name = chrome.find_element(By.XPATH, "//div[contains(@class,'row')]//div[contains(@class,'col')]//div[@class='RG5Slk']")
    print(name.text)

chrome_driver = open_chrome()
open_flipkart(chrome_driver, "https://www.flipkart.com/")
close_icon(chrome_driver)
search_value(chrome_driver)
click_newest(chrome_driver)
product_name(chrome_driver)









