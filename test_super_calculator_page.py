# этот файл будем запускать для теста, здесь прописаны сами шаги теста
import time

from .pages.super_calculator_page import MainPage

import pytest


def test_user_can_see_page_title(browser_url):
    page = MainPage(browser_url)
    page.should_be_page_title()
    time.sleep(5)
