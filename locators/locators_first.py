# This page describes the selectors for super calculator page
from selenium.webdriver.common.by import By


class LocatorsSuperCalculatorPage:
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
    OPERATIONS = {
        "selector": (By.CSS_SELECTOR, "select.span1"),
        "name": "operations"
    }
    OPERATION_DIVISION = {
        "selector": (By.XPATH, "//option[text() = '/']"),
        "name": "operation division"
    }
    OPERATION_MULTIPLICATION = {
        "selector": (By.XPATH, "//option[text()='*']"),
        "name": "operations multiplication"
    }
    FIRST_LINE_RESULT = {
        "selector": (By.XPATH, "//span[contains(text(), '*' )]"),
        "name": "expression on the first line"
    }
    SECOND_LINE_RESULT = {
        "selector": (By.XPATH, "//span[contains(text(), '/')]"),
        "name": "expression on the second line"
    }
    RESULT_DIVISION = {
        "selector": (By.CSS_SELECTOR, "tr td.ng-binding:last-child"),
        "name": "result division"
    }
    RESULT_MULTIPLICATION = {
        "selector": (By.CSS_SELECTOR, "tr td.ng-binding:last-child"),
        "name": "result multiplication"
    }
    RESULT_ADDITION = {
        "selector": (By.CSS_SELECTOR, "tr td.ng-binding:last-child"),
        "name": "result multiplication"
    }
