from behave import fixture, use_fixture
from virtualenv.report import LOGGER

from pages.selenium_factory import DriverFactory


@fixture
def selenium_browser_chrome(context):
    context.driver = DriverFactory.create_driver('chrome')
    yield context.driver
    context.driver.close()

@fixture
def selenium_browser_edge(context):
    context.driver = DriverFactory.create_driver('edge')
    yield context.driver
    context.driver.close()

def before_scenario(context, scenario):
    """Run before each scenario"""
    LOGGER.info('BEFORE SCENARIO')
    use_fixture(selenium_browser_chrome, context)





