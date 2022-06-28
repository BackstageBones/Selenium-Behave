from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def set_chrome_options():
    options = ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--disable-popup-blocking')
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    options.headless = False
    return options


def _chrome_driver():
    options = set_chrome_options()
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def _edge_driver(*args):
    capabilities = args
    executable_path = EdgeChromiumDriverManager().install()
    return webdriver.Edge(
        executable_path=executable_path,
        capabilities=capabilities
    )


class DriverFactory:
    Drivers = {
        'chrome': _chrome_driver,
        'edge': _edge_driver,

    }

    @classmethod
    def create_driver(cls, driver_type):
        if driver_type not in cls.Drivers:
            raise ValueError
        return cls.Drivers[driver_type]()


class SeleniumActions:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self._driver = driver

    def find_element(self, locator):
        i = 0
        while i <= SeleniumActions.DEFAULT_TIMEOUT:
            try:
                element = self._driver.find_element(*locator)
            except Exception:
                i += 1
            else:
                return element

    def find_elements(self, locator):
        i = 0
        while i <= SeleniumActions.DEFAULT_TIMEOUT:
            try:
                elements = self._driver.find_elements(*locator)
            except Exception as e:
                i += 1
            else:
                return elements

    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self._driver, timeout=SeleniumActions.DEFAULT_TIMEOUT).until(
            ec.element_to_be_clickable(locator))

    def wait_for_element_to_be_displayed(self, locator):
        return WebDriverWait(self._driver, timeout=SeleniumActions.DEFAULT_TIMEOUT).until(
            ec.visibility_of_element_located(locator))

    def is_element_displayed(self, locator):
        try:
            self.wait_for_element_to_be_displayed(locator)
        except TimeoutException:
            return False
        else:
            return True

    def send_keys(self, locator, value):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)

    def click_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def select_element_by_text(self, locator, text):
        select_element = self.find_element(locator)
        select_object = Select(select_element)
        return select_object.select_by_visible_text(text)

    def set_element_value(self, locator, value):
        element = self.wait_for_element_clickable(locator)
        self._driver.execute_script(f"arguments[0].setAttribute('value', '{value}')", element)

    def click_by_javascript(self, locator):
        element = self.find_element(locator)
        self._driver.execute_script('arguments[0].click();', element)

    def scroll_to_element(self, element):
        action = ActionChains(self._driver)
        action.move_to_element(element).perform()
