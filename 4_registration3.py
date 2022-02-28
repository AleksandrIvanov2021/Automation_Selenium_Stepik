from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys("Joker")
    browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys("Poker")
    browser.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys("Joker@mail.com")
    browser.find_element_by_css_selector("button.btn").click()

    time.sleep(5)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()

