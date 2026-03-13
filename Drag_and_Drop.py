from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class internet_Page:
    def __init__(self, url : str, driver : WebDriver):
        self.url = url
        self.driver = driver

    def open_internet(self):
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.maximize_window()

    def drag_drop(self):
         drag = self.driver.find_element(By.ID, "column-a")
         drop = self.driver.find_element(By.ID, "column-b")
         ActionChains(self.driver).drag_and_drop(drag, drop).perform()


# Create driver object for chrome
driver = webdriver.Chrome()
driver.implicitly_wait(2)

page = internet_Page("https://the-internet.herokuapp.com/drag_and_drop",driver)
page.open_internet()
page.drag_drop()
time.sleep(5)

