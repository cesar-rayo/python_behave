import logging
from behave import *
from pages.home import HomePage

LOGGER = logging.getLogger(__name__)


@when(u'The Customer visits Home Page')
def step_impl(context):
    context.test_data = {}

    LOGGER.info("> Loading Home page")
    home_page = HomePage(context.driver)
    home_page.load()

    context.current_page = home_page


@then(u'Home Page is displayed')
def step_impl(context):
    home_page = context.current_page
    assert "508 Resource Limit Is Reached" not in home_page.title(), "Seems the page is not available"
