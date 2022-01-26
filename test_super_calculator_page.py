# этот файл будем запускать для теста, здесь прописаны сами шаги теста
from .pages.super_calculator_page import MainPage


def test_user_can_see_page_title(browser_url):
    page = MainPage(browser_url)
    page.should_be_page_title()


def test_user_can_see_result_of_addition_numbers(browser_url):
    page = MainPage(browser_url)
    page.should_be_result_of_adding_numbers()


def test_user_can_see_history_of_calculator_results(browser_url):
    page = MainPage(browser_url)
    page.history_session_calculator_results()
