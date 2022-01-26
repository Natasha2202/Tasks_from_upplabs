# Страница, от которой будут унаследованы все остальные классы
# В ней опишем вспомогательные методы для работы с драйвером
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

timeout = 10


class BasePage:
    HEADER_PAGE = {
        "selector": (By.CSS_SELECTOR, ".header__body.grid-base"),
        "name": "header size"
    }

    def __init__(self, browser_url):
        self.browser = browser_url

    def open(self):
        self.browser.get(self.browser.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def scroll_by_height_of_header(self):
        header = self.browser.get_element(self.HEADER_PAGE)
        self.browser.execute_script("window.scrollBy(0, -arguments[0].offsetHeight)", header)

    def get_element(self, element):
        WebDriverWait(self.browser, 5).until(expected_conditions.presence_of_element_located(element["selector"]))
        try:
            found_element = self.browser.find_element(*element["selector"])
            return found_element
        except NoSuchElementException:
            assert False, f"element {element['name']} is not found"

    def smart_click(self, _object):
        element = self.get_element(_object)
        for i in range(timeout * 2):
            try:
                element.click()
                return
            except WebDriverException:
                time.sleep(0.5)
        assert False, f"time expired, {_object['name']} is not clickable"

    def smart_send_keys(self, _object, value):
        input1 = self.get_element(_object)
        for i in range(timeout * 2):
            try:
                input1.send_keys(value)
                return
            except WebDriverException:
                time.sleep(0.5)
        assert False, f"time expired, {_object['name']} is not found"
