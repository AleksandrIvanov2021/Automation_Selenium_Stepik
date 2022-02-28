import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])  # проверяет 2 раза один тест(русскую и англ. версию)
def test_guest_should_see_login_link(browser, language):  # так же нужно передать в качестве аргумента
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

    # pytest -s -v 32_test_fixture12_marks_parametrize.py
    # В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться, и список значений параметра.
    # В самом тесте наш параметр тоже нужно передавать в качестве аргумента. Обратите внимание, что внутри декоратора
    # имя параметра оборачивается в кавычки, а в списке аргументов теста кавычки не нужны.
    # Можно задавать параметризацию также для всего тестового класса, чтобы все тесты в классе запустились с заданными
    # параметрами. В таком случае отметка о параметризации должна быть перед объявлением класса
