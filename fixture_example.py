import pytest
from selenium import webdriver

import time

from helper_example import method_name


@pytest.fixture
def user_crenditials():
    file = open(r"C:\Users\VPrabhakaran\OneDrive - RCG Global Services, Inc\Desktop\Selenium\fixture_pwd.txt", "r")
    line = file.readline()
    print(line)
    file.close()
    return line.split(",")


def test_validate(user_crenditials):

#Arrange

    driver = webdriver.Chrome()
    driver.get("https://vallarasu.in/test/login")

    expected_title, login_element, password_element, user_element = method_name(driver)

    user_name , password = user_crenditials

#Act
    user_element.send_keys(user_name)
    password_element.send_keys(password)
    time.sleep(5)
    login_element.click()
    time.sleep(5) # only for local

#Assert

    assert driver.title == expected_title, "Given username or password incorrect"













