# в этом файле описание селекторов для 1-й страницы
from selenium.webdriver.common.by import By


class LocatorsSuperCalculatorPage:
    PAGE_TITLE = {
        "selector": (By.CSS_SELECTOR, ".container div>h3"),
        "name": "page title: Super calculator"
    }
