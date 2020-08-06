from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which

#these 2 lines makes headless browser (without GUI)
chrome_options = Options()
chrome_options.add_argument("--headless")


chrome_path = which("chromedriver")

#if you want a headless browser add it through options
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver.get("https://duckduckgo.com")

search_input = driver.find_element_by_xpath("(//input[contains(@class, 'js-search-input')])[1]")
search_input.send_keys("My User Agent")

# search_btn = driver.find_element_by_id("search_button_homepage")
# search_btn.click()
# OR:
search_input.send_keys(Keys.ENTER)
print(driver.page_source)
driver.close()

"""
#this is how you find an element with ID
search_btn.find_element_by_id("search_form_input_homepage")
driver.find_elements_by_class_name("class")
driver.find_elements_by_tag_name("h1")
driver.find_elements_by_xpath("")
driver.find_elements_by_css_selector()
"""