from locators.tivix_labs_locators import TivixLabsLocators
from pages.BasePage import BasePage


class TivixLabsPage(BasePage):
    date_format = '2022-05-14'

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_to_be_loaded(self):
        self._actions.wait_for_element_to_be_displayed(TivixLabsLocators.rental_form)
        self._actions.wait_for_element_to_be_displayed(TivixLabsLocators.rental_country)

    def choose_country(self, country):
        self._actions.select_element_by_text(TivixLabsLocators.rental_country, country)

    def choose_city(self, city):
        self._actions.select_element_by_text(TivixLabsLocators.rental_city, city)

    def choose_model(self, model):
        self._actions.send_keys(TivixLabsLocators.rental_model, model)

    def choose_pickup_date(self, start_date):
        self._actions.set_element_value(TivixLabsLocators.rental_pickup_date, start_date)

    def choose_drop_off_date(self, end_date):
        self._actions.set_element_value(TivixLabsLocators.rental_drop_off_Date, end_date)

    def click_search_button(self):
        self._actions.click_element(TivixLabsLocators.rental_search_button)

    def count_results(self):
        return len(self._actions.find_elements(TivixLabsLocators.list_of_cars))