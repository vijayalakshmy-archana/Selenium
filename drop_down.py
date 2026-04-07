from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://vallarasu.in/test/select")
driver.maximize_window()
time.sleep(3)

D_O_B = driver.find_element(By.ID, "dob_day")
drop_down = Select(D_O_B)

length = len(drop_down.options)
print(length)

#values
#text
#index

education = driver.find_element(By.ID, "education")
drop_down = Select(education)

drop_down.select_by_index(4)
time.sleep(4)
#print(drop_down.all_selected_options) - all
print(drop_down.all_selected_options[0] == drop_down.options[4])
print(drop_down.all_selected_options[0].text)






