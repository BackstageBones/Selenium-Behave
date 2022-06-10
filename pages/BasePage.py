from pages.selenium_factory import SeleniumActions


class BasePage:

    def __init__(self, driver):
        self.__driver = driver
        self._actions = SeleniumActions(driver)

    def open_page(self, url):
        self.__driver.get(url)
