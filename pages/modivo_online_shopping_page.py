from pages.BasePage import BasePage
from locators.modivo_locators import ModivoLocators


class ModivoOnlineShoppingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_womans_clothing(self):
        self._actions.click_element(ModivoLocators.woman_clothing_btn)