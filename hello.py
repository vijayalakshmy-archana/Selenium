from selenium.webdriver.remote.webelement import WebElement

print("Hello World")

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
chrome.get("https://selenium-python.readthedocs.io/installation.html")
time.sleep(5)
#element = chrome.find_element(By.XPATH, "//a[@href='locating-elements.html']")
element = chrome.find_element(By.CSS_SELECTOR,"a[href='locating-elements.html']")
element.click()
time.sleep(5)
chrome.close()

# a[href='locating-elements.html'] - CSS
# //a[@href='locating-elements.html'] - xpath

#Search dropdown

#<input aria-label="Search or ask a question" class="syndicated-navigation__chrome__search__form__input syndicated-navigation__chrome__search__form__input--wdw syndicated-navigation__chrome__search__form__input--empty" type="search" placeholder="Search or ask a question" maxlength="254" autocomplete="off" name="searchQuery" role="combobox" aria-expanded="false" aria-controls="syndicated-navigation__chrome__search__autosuggest" aria-autocomplete="list" value="">

# CSS - document.querySelector("input[name='searchQuery']")
# x path - //input[@name='searchQuery']

# Explore resort hotels

#<a href="/resorts/" target="_self" class="button button--primary button--large hero-button astro-lvkotgoy" tabindex="0" data-analytics-link-id="WDW_Module_0_Hero_fastHeroStandard_0_ExploreResortHotels_link" data-astro-cid-lvkotgoy="">

#//a[@href="/resorts/" and contains(@class,"hero-button")] - X path
#document.querySelectorAll("a[href='/resorts/'].hero-button") - css

#//div[contains(@class,'row')]


#//input[@name='searchQuery']


