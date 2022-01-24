# Страница, от которой будут унаследованы все остальные классы
# В ней опишем вспомогательные методы для работы с драйвером
from selenium.common.exceptions import NoSuchElementException
from ..modules.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    HEADER_PAGE = {
        "selector": (By.CSS_SELECTOR, ".header__body.grid-base"),
        "name": "header size"
    }

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def open(self, route):
        self.browser.get(self.browser.url + route)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def scroll_by_height_of_header(self):
        header = self.browser.get_element(self.HEADER_PAGE)
        self.browser.execute_script("window.scrollBy(0, -arguments[0].offsetHeight)", header)
