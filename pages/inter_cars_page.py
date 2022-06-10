from pages.BasePage import BasePage
from locators.inter_cars_locators import InterCarsLocators


class InterCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def await_for_search_bar_to_present(self):
        self._actions.wait_for_element_to_be_displayed(InterCarsLocators.search_by_car_button)
        self._actions.wait_for_element_to_be_displayed(InterCarsLocators.search_widget)
        self._actions.wait_for_element_to_be_displayed(InterCarsLocators.search_input)
        self._actions.wait_for_element_to_be_displayed(InterCarsLocators.search_button)

    def search_for_car_part(self, part):
        self._actions.send_keys(InterCarsLocators.search_input, part)
        self._actions.click_element(InterCarsLocators.search_button)

    def choose_search_by_car(self, make, model, type):
        search_by_car = self._actions.wait_for_element_to_be_displayed(InterCarsLocators.search_by_car_button)
        self._actions.scroll_to_element(search_by_car)
        self._actions.click_by_javascript(InterCarsLocators.search_by_car_button)
        self.select_car_make(make)
        self.select_car_model(model)
        self.select_car_type(type)
        self.click_dropdown_search_button()

    def select_car_make(self, make):
        self._actions.select_element_by_text(InterCarsLocators.select_make_dropdown, make)

    def select_car_model(self, model):
        self._actions.select_element_by_text(InterCarsLocators.select_model_dropdown, model)

    def select_car_type(self, type):
        self._actions.select_element_by_text(InterCarsLocators.select_type_dropdown, type)

    def click_dropdown_search_button(self):
        self._actions.click_element(InterCarsLocators.select_car_search_button)

    def is_popup_displayed(self):
        return self._actions.is_element_displayed(InterCarsLocators.todo_popup)

    def are_results_displayed(self):
        return self._actions.is_element_displayed(InterCarsLocators.products_list)

    def list_results(self):
        return self._actions.find_elements(InterCarsLocators.products_list)
