import math, time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 120);")

    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    browser.find_element_by_css_selector("#robotsRule").click()
    browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()

