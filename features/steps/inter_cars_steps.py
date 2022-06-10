from assertpy import assert_that
from behave import *

from pages.inter_cars_page import InterCarsPage

use_step_matcher("parse")


@step("User waits for search bar to be loaded")
def step_impl(context):
    inter_cars = InterCarsPage(context.driver)
    inter_cars.await_for_search_bar_to_present()


@when("User enters car part {car_part} in the search bar")
def step_impl(context, car_part):
    inter_cars = InterCarsPage(context.driver)
    inter_cars.search_for_car_part(car_part)


@when("User chooses vehicle make {make}, model {model} and type {type}")
def step_impl(context, make, model, type):
    inter_cars = InterCarsPage(context.driver)
    inter_cars.choose_search_by_car(make, model, type)


@then("User will see that search results are {condition}")
def step_impl(context, condition):
    inter_cars = InterCarsPage(context.driver)
    if condition == 'displayed':
        assert_that(inter_cars.are_results_displayed()).is_true()
        assert_that(len(inter_cars.list_results())).is_greater_than(0)
    if condition.startswith('not'):
        assert_that(inter_cars.are_results_displayed()).is_false()


@then("User will see that ToDo popup is displayed")
def step_impl(context):
    inter_cars = InterCarsPage(context.driver)
    assert_that(inter_cars.is_popup_displayed()).is_true()
