from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass
class ModivoLocators:
    woman_clothing_btn: By = (By.XPATH, '//section/ul/li[@class=\'item\'][1]')
    brand_new_clothing_header_btn: By = (By.XPATH, '//div//li[contains(@class, \'navigation-item _level-1\')][1]')
    clothes_tab_pane: By = (By.XPATH, '//div//li[contains(@class, \'item _level-1 is-active-level\')][1]')
    shirts_and_tshirts_tab: By = (By.XPATH, '//div//li[contains(@class, \'item _level-2 is-active-level\')][5]')
    size_filter_main_button: By = (By.CLASS_NAME, 'filter-desktop-wrapper filter nestedmultiselect size')
    upper_dressing_flter_button: By = (By.XPATH, '//div[contains(@class, \'category-box category-item\')][2]')
    size_38: By = (By.ID, 'checkbox-damskie_gorne_czesci_garderoby:M:38')
