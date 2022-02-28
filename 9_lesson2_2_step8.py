import time, os
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element_by_css_selector("[placeholder='Enter first name']").send_keys("Gomer")
    browser.find_element_by_css_selector("[placeholder='Enter last name']").send_keys("Simpson")
    browser.find_element_by_css_selector("[placeholder='Enter email']").send_keys("Gomer@everybody.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "new.txt")
    browser.find_element_by_css_selector("#file").send_keys(file_path)

    browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()

