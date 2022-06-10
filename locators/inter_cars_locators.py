from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class InterCarsLocators:
    search_widget: By = (By.ID, 'ICSW_searchWidget')
    search_by_car_button: By = (By.ID, 'ICSW_tabsToggler')
    search_input: By = (By.ID, 'ICSW_query')
    search_button: By = (By.ID, 'ICSW_search')
    select_make_dropdown: By = (By.ID, 'ICSW_marka')
    select_model_dropdown: By = (By.ID, 'ICSW_model')
    select_type_dropdown: By = (By.ID, 'ICSW_typ')
    select_car_search_button: By = (By.ID, 'ICSW_selectThis')
    todo_popup: By = (By.XPATH, '//h3[contains(text(), \'Co chcesz\')]')
    products_list: By = (By.XPATH, '//ul[contains(@class, \'products-list\')]')
