from behave import use_fixture
from commons.fixtures import web_browser


def before_scenario(context, scenario):
    use_fixture(web_browser, context)
