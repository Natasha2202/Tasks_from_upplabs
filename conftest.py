# This page is for storing frequently used fixtures and storing global settings
import pytest
import selenium
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, ru, ...(etc.)")
    parser.addoption("--base_url", action='store', default=None)
    parser.addoption("--timeout", action='store', default="10")
    parser.addoption("--headless", action='store', default="false")


@pytest.fixture(scope="function")
def browser_url(request):
    base_url = "http://juliemr.github.io/protractor-demo"
    assert base_url is not None, "url is not correct"
    default_timeout = request.config.getoption("timeout")
    assert default_timeout.isnumeric() and 0 < int(default_timeout) < 120, "timeout is not correct"
    headless = request.config.getoption("headless")
    assert (headless == "true" or headless == "false"), "incorrect headless value"
    # browser = WebDriver(url=base_url, timeout=default_timeout, headless=(headless == "false"))
    browser = selenium.webdriver.Chrome("/usr/local/bin/chromedriver")
    browser.get(base_url)
    yield browser
    browser.quit()
