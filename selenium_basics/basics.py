from selenium import webdriver
from shutil import which

chrome_path = which("chromedriver")


driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://duckduckgo.com")

search_input = driver.find_element_by_xpath("(//input[contains(@class, 'js-search-input')])[1]")
search_input.send_keys("My User Agent")

search_btn = driver.find_element_by_id("search_button_homepage")
search_btn.click()
"""
#this is how you find an element with ID
search_btn.find_element_by_id("search_form_input_homepage")
driver.find_elements_by_class_name("class")
driver.find_elements_by_tag_name("h1")
driver.find_elements_by_xpath("")
driver.find_elements_by_css_selector()
"""