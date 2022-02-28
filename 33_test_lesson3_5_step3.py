import pytest
from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    def test_links(self, browser, links):
        answer = str(math.log(int(time.time())))
        link = links
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_tag_name("textarea").send_keys(answer)
        button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        button.click()
        right = browser.find_element_by_class_name("smart-hints__hint")
        assert "Correct!" in right.text
        time.sleep(3)


if __name__ == "__main__":
    pytest.main()

    # Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
    # Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
    # Ваша задача — реализовать автотест со следующим сценарием действий:
    # открыть страницу
    # ввести правильный ответ
    # нажать кнопку "Отправить"
    # дождаться фидбека о том, что ответ правильный
    # проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    # В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает
    # со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.
    # Правильным ответом на задачу в заданных шагах является число:
    # import time
    # import math
    # answer = math.log(int(time.time()))
