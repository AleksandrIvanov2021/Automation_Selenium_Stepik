import time, math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

browser.find_element_by_css_selector("[type='submit']").click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_css_selector("#input_value").text
y = calc(x)

browser.find_element_by_css_selector("#answer").send_keys(y)
browser.find_element_by_css_selector("[type='submit']").click()

time.sleep(10)
browser.quit()

