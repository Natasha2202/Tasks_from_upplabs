# Для хранения часто используемых фикстур и хранения глобальных настроек
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from .modules.webdriver import WebDriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, ru, ...(etc.)")
    parser.addoption("--base_url", action='store', default=None)
    parser.addoption("--timeout", action='store', default="10")
    parser.addoption("--headless", action='store', default="false")


@pytest.fixture(scope="function")
def browser(request):
    base_url = request.config.getoption("base_url")
    assert base_url is not None, "url is not correct"
    default_timeout = request.config.getoption("timeout")
    assert default_timeout.isnumeric() and 0 < int(default_timeout) < 120, "timeout is not correct"
    headless = request.config.getoption("headless")
    assert (headless == "true" or headless == "false"), "incorrect headless value"
    browser = WebDriver(url=base_url, timeout=default_timeout, headless=(headless == "true"))
    yield browser
    browser.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)  #определяет момент когда тест завалился
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
