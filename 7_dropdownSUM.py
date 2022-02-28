import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    a = browser.find_element_by_css_selector("#num1").text
    b = browser.find_element_by_css_selector("#num2").text
    x = int(a) + int(b)

    time.sleep(1)

    Select(browser.find_element_by_tag_name("select")).select_by_value(str(x))
    browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()

