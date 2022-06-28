import random

from assertpy import assert_that
from selenium.common import ElementClickInterceptedException

from locators.modivo_locators import ModivoLocators
from pages.BasePage import BasePage


class ModivoOnlineShoppingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def accept_marketing_approvals(self):
        if self._actions.is_element_displayed(ModivoLocators.marketing_approvals_modal):
            self._actions.click_element(ModivoLocators.accept_marketing_approvals_btn)

    def select_womans_clothing(self):
        self._actions.click_element(ModivoLocators.woman_clothing_btn)

    def select_main_type_of_clothing(self, type):
        element = self._actions.find_element(ModivoLocators.choose_main_clothing_type(type))
        element.click()

    def select_upper_clothe_type(self, type):
        if self._actions.is_element_displayed(ModivoLocators.popup_close_button):
            self._actions.click_element(ModivoLocators.popup_close_button)
        self._actions.wait_for_element_to_be_displayed(ModivoLocators.return_upper_clothing_type_locator(type))
        self._actions.click_element(ModivoLocators.return_upper_clothing_type_locator(type))

    def choose_new_products_from_heading(self):
        self._actions.click_element(ModivoLocators.brand_new_clothing_header_btn)

    def select_size_filter(self):
        self._actions.click_element(ModivoLocators.size_filter_main_button)

    def select_top_garmets_from_size_filter(self):
        self._actions.click_element(ModivoLocators.upper_dressing_filter_button)

    def select_specific_size(self, size):
        size = size.split()
        element = self._actions.find_element(ModivoLocators.return_size_locator(size[0], size[1]))
        self._actions.scroll_to_element(element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self._actions.click_by_javascript(ModivoLocators.return_size_locator(size[0], size[1]))
        self.confirm_size_choosing()

    def confirm_size_choosing(self):
        assertion_message = 'Confirmation button should contain one size chose displayed, but it doesn\'t'
        element = self._actions.find_element(ModivoLocators.choose_size_button_label)
        assert_that(element.text.strip()[-2], assertion_message).is_equal_to('1')
        self._actions.click_element(ModivoLocators.choose_size_button)

    def select_random_cloth_cc_from_list(self):
        available_clothes = self._actions.find_elements(ModivoLocators.clothes_cc_cards)
        random_cc = random.choice(available_clothes)
        random_cc.click()

    def add_to_cart_from_cloth_cc(self, size):
        self._actions.wait_for_element_to_be_displayed(ModivoLocators.add_to_cart_button_from_cc)
        self._actions.click_element(ModivoLocators.add_to_cart_button_from_cc)
        self._actions.click_element((ModivoLocators.return_cart_size_locator(size)))

    def go_to_basket_from_cc(self):
        self._actions.wait_for_element_to_be_displayed(ModivoLocators.show_basket_from_cc_button)
        self._actions.click_element(ModivoLocators.show_basket_from_cc_button)
