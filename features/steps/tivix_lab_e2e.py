from behave import *
from assertpy import assert_that
from pages.tivix_labs_page import TivixLabsPage

use_step_matcher("parse")


@given("User is at {url_address} web page")
def step_impl(context, url_address):
    tivix_page = TivixLabsPage(context.driver)
    tivix_page.open_page(url_address)



@step("User waits for Car rental page to be loaded")
def step_impl(context):
    tivix_page = TivixLabsPage(context.driver)
    tivix_page.wait_for_page_to_be_loaded()


@when("User selects desired country to {country}")
def step_impl(context, country):
    tivix_page = TivixLabsPage(context.driver)
    tivix_page.choose_country(country)


@step("User selects desired city to {city}")
def step_impl(context, city):
    tivix_page = TivixLabsPage(context.driver)
    tivix_page.choose_city(city)


@step("User Chooses desired card model {model}")
def step_impl(context, model):
    tivix_page = TivixLabsPage(context.driver)
    tivix_page.choose_model(model)


@step("User sets car pick up date to {pickup_date}")
def step_impl(context, pickup_date):
     tivix_page = TivixLabsPage(context.driver)
     tivix_page.choose_pickup_date(pickup_date)


@step("User sets car drop off date to {drop_off_date}")
def step_impl(context, drop_off_date):
     tivix_page = TivixLabsPage(context.driver)
     tivix_page.choose_drop_off_date(drop_off_date)


@step("User clicks search button")
def step_impl(context):
    tivix_page = TivixLabsPage(context.driver)
    tivix_page.click_search_button()


@then("User will see list of available cars for rent")
def step_impl(context):
    tivix_page = TivixLabsPage(context.driver)
    search_resulsts = tivix_page.count_results()
    assert_that(search_resulsts).is_greater_than(0)