from assertpy import assert_that
from behave import *

from pages.modivo_online_shopping_page import ModivoOnlineShoppingPage
from utils.UsersData import USERS
from utils.modivo_enums import UpperClothingTypeEnum, ClothingType, Cards

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
    context.item_price = modivo.retrieve_price_tag_from_cc()
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


@step("User decides to continue checkout as a guest")
def step_impl(context):
    modivo = ModivoOnlineShoppingPage(context.driver)
    modivo.select_continue_as_a_guest()


@step("User fills billing data as {account}")
def step_impl(context, account):
    modivo = ModivoOnlineShoppingPage(context.driver)
    formatted_account = account.split()
    assertion_message = 'Billing detail fields for a guest user should be displayed, but are not.'
    assert_that(modivo.check_if_billing_fields_displayed(), assertion_message).is_true()
    for user in USERS:
        if formatted_account[0].strip() == user.First_name and formatted_account[1].strip() == user.Last_name:
            modivo.fill_billing_details(user)
            break
        else:
            raise NameError


@step("User chooses DHL shipment for his order")
def step_impl(context):
    modivo = ModivoOnlineShoppingPage(context.driver)
    modivo.select_dhl_shipment()


@step("User fills card payment form with invalid Visa card")
def step_impl(context):
    modivo = ModivoOnlineShoppingPage(context.driver)
    modivo.fill_card_form(Cards.VISA_UNAUTHENTICATED)


@step("User decides to finish his order with pay button")
def step_impl(context):
    modivo = ModivoOnlineShoppingPage(context.driver)
    modivo.click_order_button()


@then("User will see unfilled required terms error")
def step_impl(context):
    modivo = ModivoOnlineShoppingPage(context.driver)
    assertion_message = 'Only one validation error should be visible, but is not.'
    assert_that(modivo.check_for_validation_messages_under_required_fields(), assertion_message).is_equal_to(1)


@step("User Price on the checkout page matches price from basket")
def step_impl(context):
    modivo = ModivoOnlineShoppingPage(context.driver)
    assertion_message = 'Price tag on checkout page doesn\'t match the one from basket, but should.'
    assert_that(modivo.retrieve_price_form_checkout_page, assertion_message).is_equal_to(context.item_price)
