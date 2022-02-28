import time, math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element_by_css_selector("[type='submit']").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)
    browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()

