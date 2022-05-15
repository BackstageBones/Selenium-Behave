from dataclasses import dataclass
from selenium.webdriver.common.by import By

@dataclass
class TivixLabsLocators:

    rental_form: By = (By.ID, 'search_form')
    rental_country: By = (By.ID, 'country')
    rental_city: By = (By.ID, 'city')
    rental_model: By = (By.ID, 'model')
    rental_pickup_date: By = (By.ID, 'pickup')
    rental_drop_off_Date: By = (By.ID, 'dropoff')
    rental_search_button: By = (By.XPATH, '//*[@id="search_form"]/button')