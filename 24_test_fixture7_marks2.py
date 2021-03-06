import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke  # чтобы в выводе не было предупреждений, необходимо создать файл pytest.ini и добавить метки
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    # pytest -s -v -m "smoke and win10" 24_test_fixture7_marks2.py
    # Так должны выглядеть добавленные метки в файл pytest.ini
    # [pytest]
    # markers =
    #     smoke: marker for smoke tests                (то, что после двоеточия - необязательно!)
    #     regression: marker for regression tests
    #     win10
