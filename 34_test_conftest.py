import pytest                           # Это можно вынести в отдельный файл conftest.py
from selenium import webdriver


@pytest.fixture(scope="function")         # фикстуру также можно вынести в отдельный файл conftest.py
def browser():                            # чтобы не прописывать одну и ту же часть кода каждый раз
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

    # запуск теста с аргументом browser из фикстуры вынесенной в отдельный файл conftest.py
    # Таким образом можно удобно переиспользовать одни и те же вспомогательные функции в разных частях проекта.
    # PyTest автоматически находит и подгружает файлы conftest.py, которые находятся в директории с тестами.
    # Если вы храните все свои скрипты для курса в одной директории, будьте аккуратны и следите,
    # чтобы не возникало ситуации, когда в поддиректориях имеется 2 файла conftest.py, иначе это приведет к конфликтам.


