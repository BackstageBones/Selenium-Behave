from behave import *
from pages.modivo_online_shopping_page import ModivoOnlineShoppingPage
use_step_matcher("parse")



@step("User chooses {type} clothing")
def step_impl(context, type):
    modivo = ModivoOnlineShoppingPage()
    if type == 'Womans':



@step("Users selects {header} type of clothing from the header pane")
def step_impl(context, header):
    if header == 'New Products':


@when("User chooses Size filter for {clothing_type} with detailed size {size}")
def step_impl(context, clothing_type, size):
    raise NotImplementedError(u'STEP: When User chooses Size filter for {clothing_type} with detailed filter {filter}')