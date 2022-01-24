# этот файл будем запускать для теста, здесь прописаны сами шаги теста
from .pages.first_e import MainPage
import pytest


def test_user_can_see_page_title(browser):
    page = MainPage(browser)
    page.open()
    page.should_be_page_title()
