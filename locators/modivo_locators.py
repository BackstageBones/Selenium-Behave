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
    choose_size_sidebar: By = (By.XPATH, '//div[@class=\'side-modal opened right  is-not-full-screen-on-mobile\']')
    clothes_cc_cards: By = (By.XPATH, '//li[@class=\'product\']')
    add_to_cart_button_from_cc: By = (By.XPATH, '//button[@class=\'add-to-cart base-button primary normal\']')
    show_basket_from_cc_button: By = (By.XPATH, '//button[@data-test-id=\'added-to-cart-go-to-cart-button\']')
    proceed_to_checkout_button: By = (By.XPATH, '//button[@data-test-id=\'cart-proceed-to-checkout\']')
    continue_as_a_guest_button: By = (By.XPATH, '//button[@data-test-id=\'continue-as-guest\']')
    marketing_approvals_modal: By = (By.ID, 'marketing-approvals')
    accept_marketing_approvals_btn: By = (By.XPATH, '//*[@id="marketing-approvals"]/div/footer/button[2]')
    popup_close_button: By = (By.XPATH, '//button[@class=\'button-icon close\']')
    item_price_tag: By = (
        By.XPATH, '//div[@class=\'product-price price big display-inline without-rating\']//div[@class=\'price\']')

    # Guest details form
    email_address: By = (By.ID, 'billing__email')
    telephone_number: By = (By.ID, 'billing__telephone')
    client_name: By = (By.ID, 'billing__firstname')
    client_last_name: By = (By.ID, 'billing__lastname')
    street_address: By = (By.ID, 'billing__street-0')
    house_number: By = (By.ID, 'billing__street-1')
    post_code: By = (By.ID, 'billing__postcode')
    city_address: By = (By.ID, 'billing__city')
    dhl_parcel_input: By = (By.ID, 'modivo_store_custom02')
    card_payment_input: By = (By.ID, 'payu_gateway_card')

    @classmethod
    def return_size_locator(cls, size_1, size_2):
        return (By.ID, f'checkbox-damskie_gorne_czesci_garderoby:{size_1}:{size_2}')

    @classmethod
    def return_cart_size_locator(cls, size):
        return (By.XPATH, f"//tr[@data-test-value='{size}']")

    @classmethod
    def choose_main_clothing_type(cls, type):
        return (By.XPATH, f'//li[@class=\'item _level-1 is-active-level\'][{type}]/a')

    @classmethod
    def return_upper_clothing_type_locator(cls, enum):
        return (By.XPATH, f'//div//li[contains(@class, \'item _level-2 is-active-level\')][{enum}]')
