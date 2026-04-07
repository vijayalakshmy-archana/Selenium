import pytest
from selenium import webdriver
from selenium.webdriver.common. by import By

import time

@pytest.mark.parametrize ("user_crenditials", [("admin", "admin"), ("ad", "pass")])
def test_validate(user_crenditials):

#Arrange

    driver = webdriver.Chrome()
    driver.get("https://vallarasu.in/test/login")

    user_locator = "login-user"
    password_locator = "login-pass"
    login_locator = "login-button"
    expected_title = "Form Fields Automation Testing"

    user_element  = driver.find_element(By.ID, user_locator)
    password_element = driver.find_element(By.ID, password_locator)
    login_element = driver.find_element(By.ID, login_locator)

    user_name , password = user_crenditials

#Act
    user_element.send_keys(user_name)
    password_element.send_keys(password)
    time.sleep(5)
    login_element.click()
    time.sleep(5) # only for local

#Assert

    assert driver.title == expected_title, "Failed: Invaild login crendiatials for " + user_name











