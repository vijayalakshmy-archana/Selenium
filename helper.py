from selenium.webdriver.common. by import By

def find_element(driver):
    user_locator = "login-user"
    password_locator = "login-pass"
    login_locator = "login-button"
    expected_title = "Form Fields Automation Testing"

    user_element = driver.find_element(By.ID, user_locator)
    password_element = driver.find_element(By.ID, password_locator)
    login_element = driver.find_element(By.ID, login_locator)
    return expected_title, login_element, password_element, user_element




