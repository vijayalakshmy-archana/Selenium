from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Home_Page:
    def __init__(self, url : str, driver : WebDriver):
        self.url = url
        self.driver = driver

    def open_internet(self):
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.maximize_window()

    def click_alert(self):
        button = self.driver.find_element(By.XPATH, "//button[text()= 'Click for JS Alert']")
        button.click()
        alert = driver.switch_to.alert
        print("Alert text:", alert.text)
        time.sleep(2)
        alert.accept()
        print("ok")
        time.sleep(2)

    def click_confirm(self):
        button_2 = self.driver.find_element(By.XPATH, "//button[text()= 'Click for JS Confirm']")
        button_2.click()
        alert_2 = driver.switch_to.alert
        print("Alert text:", alert_2.text)
        time.sleep(1)
        alert_2.dismiss()
        print("cancel")
        time.sleep(1)


# Create driver object for chrome
driver = webdriver.Chrome()
driver.implicitly_wait(2)

# create homepage object
page = Home_Page("https://the-internet.herokuapp.com/javascript_alerts", driver)
page.open_internet()
page.click_alert()
page.click_confirm()
