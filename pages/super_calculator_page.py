# в этом файле описание того как будут делаться проверки на странице 1-го теста
from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    PAGE_TITLE = {
        "selector": (By.CSS_SELECTOR, ".container div>h3"),
        "name": "page title: Super calculator"
    }
    FIRST_NUMBER_FIELD = {
        "selector": (By.CSS_SELECTOR, ".input-small:first-child"),
        "name": "first field to input number"
    }
    SECOND_NUMBER_FIELD = {
        "selector": (By.CSS_SELECTOR, ".input-small:nth-of-type(2)"),
        "name": "second field to input number"
    }
    BUTTON_GO = {
        "selector": (By.CSS_SELECTOR, "#gobutton"),
        "name": "button go on super calculator page"
    }

    RESULT_FIELD = {
        "selector": (By.CSS_SELECTOR, "td:last-child.ng-binding"),
        "name": "result field"
    }


    def open(self, **kwargs):
        BasePage.open("/")

    def should_be_page_title(self):
        self.browser.smart_click(self.PAGE_TITLE)
        title_page = self.browser.get_element(MainPage.PAGE_TITLE).text
        assert "Super Calculator" == title_page, \
            "there is now correct page title"

    def should_be_result_of_adding_numbers(self):
        # input_first_number = self.browser.get_element(self.FIRST_NUMBER_FIELD)
        # input_second_number = self.browser.get_element(self.SECOND_NUMBER_FIELD)
        self.browser.smart_send_keys(self.FIRST_NUMBER_FIELD, "8")
        self.browser.smart_send_keys(self.SECOND_NUMBER_FIELD, "8")
        self.browser.smart_click(self.BUTTON_GO)

    def should_be_a_history_session(self):
        # input_first_number = self.browser.get_element(self.FIRST_NUMBER_FIELD)


