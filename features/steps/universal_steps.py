from behave import *

from pages.BasePage import BasePage

use_step_matcher("parse")


@given("User is at {url_address} web page")
def step_impl(context, url_address):
    base_page = BasePage(context.driver)
    base_page.open_page(url_address)
