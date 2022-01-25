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
            "there is no correct page title"

    def should_be_result_of_adding_numbers(self):
        self.browser.get_element(self.FIRST_NUMBER_FIELD)
        self.browser.smart_send_keys(self.FIRST_NUMBER_FIELD, "8")
        self.browser.get_element(self.SECOND_NUMBER_FIELD)
        self.browser.smart_send_keys(self.SECOND_NUMBER_FIELD, "8")
        self.browser.smart_click(self.BUTTON_GO)
        result_addition = self.browser.find_element(By.CSS_SELECTOR, "tr td.ng-binding:last-child").text
        assert "16" == result_addition, \
            "you got wrong result_addition"


    def history_session_calculator_results(self):
        self.browser.get_element(self.FIRST_NUMBER_FIELD)
        self.browser.smart_send_keys(self.FIRST_NUMBER_FIELD, "16")
        select_operation = self.browser.find_element(By.CSS_SELECTOR, "select.span1")
        select_operation.find_element(By.XPATH, "//option[text() = "/"]")
        self.browser.get_element(self.SECOND_NUMBER_FIELD)
        self.browser.smart_send_keys(self.SECOND_NUMBER_FIELD, "4")
        self.browser.smart_click(self.BUTTON_GO)
        result_division = self.browser.find_element(By.CSS_SELECTOR, "tr td.ng-binding:last-child").text
        assert "4" == result_division, \
            "you got wrong result_division"
        self.browser.get_element(self.FIRST_NUMBER_FIELD)
        self.browser.smart_send_keys(self.FIRST_NUMBER_FIELD, "4")
        select_operation = self.browser.find_element(By.CSS_SELECTOR, "select.span1")
        select_operation.find_element(By.XPATH, "//option[text()="*"]")
        self.browser.get_element(self.SECOND_NUMBER_FIELD)
        self.browser.smart_send_keys(self.SECOND_NUMBER_FIELD, "4")
        self.browser.smart_click(self.BUTTON_GO)
        result_multiplication = self.browser.find_element(By.CSS_SELECTOR, "tr td.ng-binding:last-child").text
        assert "16" == result_multiplication, \
            "you got wrong result_multiplication"
        # expression_first_line = self.browser.find_element(By.XPATH, "//span[contains(text(), "*")]").text
        # expression_second_line = self.browser.find_element(By.XPATH, "//span[contains(text(), "/")]").text
        # assert expression_first_line and expression_second_line not None
