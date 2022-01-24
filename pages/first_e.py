# в этом файле описание того как будут делаться проверки на странице 1-го теста
from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    PAGE_TITLE = {
        "selector": (By.CSS_SELECTOR, ".container div>h3"),
        "name": "page title: Super calculator"
    }

    def open(self, **kwargs):
        super().open("/")

    def should_be_page_title(self):
        self.browser.smart_click(self.PAGE_TITLE)
        title_page = self.browser.get_element(MainPage.PAGE_TITLE).text
        assert "Super Calculator" == title_page, \
            "there is now correct page title"
