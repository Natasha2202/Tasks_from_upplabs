#  в этом файле расширения для нашего браузера
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time


class WebDriver(webdriver.Remote):
    def __init__(self, url, headless, timeout=10):
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1402,800")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        if headless:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        dc = DesiredCapabilities.CHROME
        # noinspection PyCallByClass
        webdriver.Chrome.__init__(
            self,
            service=ChromeDriverManager().install(),
            options=options,
            desired_capabilities=dc
        )
        self.set_window_size(1402, 800)
        self.url = url
        self.implicitly_wait(timeout)
        self.timeout = int(timeout)

    def get_element(self, element):
        try:
            found_element = self.find_element(*element["selector"])
            return found_element
        except NoSuchElementException:
            assert False, f"element {element['name']} is not found"

    def smart_click(self, _object):
        element = self.get_element(_object)
        for i in range(self.timeout * 2):
            try:
                element.click()
                return
            except WebDriverException:
                time.sleep(0.5)
        assert False, f"time expired, {_object['name']} is not clickable"

    def smart_send_keys(self, _object, value):
        input1 = self.get_element(_object)
        for i in range(self.timeout * 2):
            try:
                input1.send_keys(value)
                return
            except WebDriverException:
                time.sleep(0.5)
        assert False, f"time expired, {_object['name']} is not found"

    def scroll_to(self, element):
        self.execute_script("return arguments[0].scrollIntoView(true);", element)
