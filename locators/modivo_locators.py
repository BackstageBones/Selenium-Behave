from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class ModivoLocators:
    woman_clothing_btn: By = (By.XPATH, '//section/ul/li[@class=\'item\'][1]')
    brand_new_clothing_header_btn: By = (By.XPATH, '//div//li[contains(@class, \'navigation-item _level-1\')][1]')
    clothes_tab_pane: By = (By.XPATH, '//div//li[contains(@class, \'item _level-1 is-active-level\')][1]')
    shirts_and_tshirts_tab: By = (By.XPATH, '//div//li[contains(@class, \'item _level-2 is-active-level\')][5]')
    size_filter_main_button: By = (By.CLASS_NAME, 'filter-desktop-wrapper filter nestedmultiselect size')
    upper_dressing_filter_button: By = (By.XPATH, '//div[contains(@class, \'category-box category-item\')][2]')
    choose_size_button:By = (By.CLASS_NAME, 'apply-btn base-button secondary normal')
    clothes_cc_cards:By = (By.CLASS_NAME, 'offer-box product-card wishlist-button-on-hover show-extend-info')
    add_to_cart_button_from_cc:By = (By.CLASS_NAME, 'add-to-cart base-button primary normal')
    show_basket_from_cc_button: By = (By.CLASS_NAME, 'action-button go-to-cart-button base-button primary small')
    proceed_to_checkout_button:By = (By.CLASS_NAME, 'proceed-to-checkout base-button primary normal')



    @classmethod
    def return_size_locator(cls, size_1, size_2):
        return (By.ID, f'checkbox-damskie_gorne_czesci_garderoby:{size_1}:{size_2}')

    @classmethod
    def return_cart_size_locator(cls, size):
        return (By.XPATH, f'//tr//div[contains(text(), {size})]')
