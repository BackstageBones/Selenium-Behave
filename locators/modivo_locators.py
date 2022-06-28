from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class ModivoLocators:
    woman_clothing_btn: By = (By.XPATH, '//section/ul/li[@class=\'item\'][1]')
    brand_new_clothing_header_btn: By = (By.XPATH, '//div//li[contains(@class, \'navigation-item _level-1\')][1]')
    clothes_tab_pane: By = (By.XPATH, '//div//li[contains(@class, \'item _level-1 is-active-level\')][1]')

    size_filter_main_button: By = (By.XPATH,
                                   '//div[(@class=\'filter-desktop-wrapper filter nestedmultiselect size\')]//span[contains(@class, \'filter-label filter-wrapper-label\')]')
    upper_dressing_filter_button: By = (By.XPATH, '//div[contains(@class, \'category-box category-item\')][2]')
    choose_size_button: By = (By.XPATH, '//button[@class=\'apply-btn base-button secondary normal\']')
    choose_size_button_label: By = (By.XPATH, '//button[@class=\'apply-btn base-button secondary normal\']/span')
    clothes_cc_cards: By = (By.CLASS_NAME, 'offer-box product-card wishlist-button-on-hover show-extend-info')
    add_to_cart_button_from_cc: By = (By.CLASS_NAME, 'add-to-cart base-button primary normal')
    show_basket_from_cc_button: By = (By.CLASS_NAME, 'action-button go-to-cart-button base-button primary small')
    proceed_to_checkout_button: By = (By.CLASS_NAME, 'proceed-to-checkout base-button primary normal')
    marketing_approvals_modal: By = (By.ID, 'marketing-approvals')
    accept_marketing_approvals_btn: By = (By.XPATH, '//*[@id="marketing-approvals"]/div/footer/button[2]')
    popup_close_button: By = (By.XPATH, '//button[@class=\'button-icon close\']')

    @classmethod
    def return_size_locator(cls, size_1, size_2):
        return (By.ID, f'checkbox-damskie_gorne_czesci_garderoby:{size_1}:{size_2}')

    @classmethod
    def return_cart_size_locator(cls, size):
        return (By.XPATH, f'//tr//div[contains(text(), {size})]')

    @classmethod
    def return_clothing_type_locator(cls, enum):
        return (By.XPATH, f'//div//li[contains(@class, \'item _level-2 is-active-level\')][{enum}]')
