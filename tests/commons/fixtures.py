import selenium.webdriver
import logging

from behave import fixture

LOGGER = logging.getLogger(__name__)


@fixture
def web_browser(context):
    LOGGER.info("Running fixture")
    browser_name = "chrome"
    context.driver = initialize_remote_driver(browser_name, "http://localhost:4444")

    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.driver.delete_all_cookies()
    yield context.driver
    context.driver.quit()


def initialize_remote_driver(browser_name, grid_url):
    LOGGER.info("Web Driver [ {} ] using [ Selenium Grid ]".format(browser_name))
    if browser_name == 'chrome':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities={
                'browserName': 'chrome',
                'acceptInsecureCerts': True
            })
    elif browser_name == 'firefox':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities={
                'browserName': 'firefox',
                'acceptInsecureCerts': True
            })
    elif browser_name == 'safari':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities={
                'browserName': 'operablink',
                'acceptInsecureCerts': True
            })
    elif browser_name == 'edge':
        driver = selenium.webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities={
                'browserName': 'MicrosoftEdge',
                'acceptInsecureCerts': True
            })
    return driver
