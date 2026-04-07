from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://vallarasu.in/test/action-chain")

name = driver.find_element(By.XPATH, "//input[@id='name-input']")

action = ActionChains(driver)
action.click(name)
action.key_down(Keys.CONTROL)
action.send_keys("A")
action.key_down(Keys.DELETE)

action.perform()

time.sleep(3)

element = driver.find_element(By.XPATH, "//div[@id='double-click-area']")

z = ActionChains(driver)
z.double_click(element)
z.pause(3)
z.double_click(element)

z.perform()

context_click_element = driver.find_element(By.XPATH, "//button[@class='context-menu-one']")

con_click = ActionChains(driver)
con_click.context_click(context_click_element)
con_click.click(driver.find_element(By.XPATH, "//li[contains(@class,'context-menu-icon-copy')]"))

con_click.perform()

link = driver.find_element(By.XPATH,"//a[@href='https://vallarasu.in/']")
x = ActionChains(driver)
x.key_down((Keys.CONTROL))
x.click(link)
x.perform()

time.sleep(2)

