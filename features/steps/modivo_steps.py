from behave import *

from pages.modivo_online_shopping_page import ModivoOnlineShoppingPage
from utils.modivo_enums import UpperClothingTypeEnum, ClothingType

use_step_matcher("parse")


@given("User is at modivo online shopping store")
def step_impl(context):
    modivo = ModivoOnlineShoppingPage(context.driver)
    modivo.open_page('https://modivo.pl/')
    modivo.accept_marketing_approvals()


@step("User chooses {type} clothing")
def step_impl(context, type):
    modivo = ModivoOnlineShoppingPage(context.driver)
    if type == 'Womans':
        modivo.select_womans_clothing()
    else:
        raise NotImplementedError('other selections not currently handled')


@step("Users selects {header} type of clothing from the header pane")
def step_impl(context, header):
    modivo = ModivoOnlineShoppingPage(context.driver)
    if header == 'New products':
        modivo.choose_new_products_from_heading()
    else:
        raise NotImplementedError('other heading selections not currently handled')


@when("User chooses Size filter for {clothing_type} with detailed size {size}")
def step_impl(context, clothing_type, size):
    modivo = ModivoOnlineShoppingPage(context.driver)
    modivo.select_size_filter()
    if clothing_type == 'Top garmets':
        modivo.select_top_garmets_from_size_filter()
        modivo.select_specific_size(size)

    else:
        raise NotImplementedError('Shoes and underwear filters are not currently handled')
    context.size = size.split()


@step("User adds a cloth to cart")
def step_impl(context):
    modivo = ModivoOnlineShoppingPage(context.driver)
    modivo.select_random_cloth_cc_from_list()
    modivo.add_to_cart_from_cloth_cc(context.size[0])


@step("User proceeds to checkout page")
def step_impl(context):
    modivo = ModivoOnlineShoppingPage(context.driver)
    modivo.go_to_basket_from_cc()


@step("User chooses {cloth_type} type of clothing with selection for {cloth_selection}")
def step_impl(context, cloth_type, cloth_selection):
    modivo = ModivoOnlineShoppingPage(context.driver)
    if cloth_type in ClothingType.Types.keys():
        modivo.select_main_type_of_clothing(ClothingType.Types[cloth_type])
    clothing = UpperClothingTypeEnum.__members__[cloth_selection]
    modivo.select_upper_clothe_type(clothing.value)
