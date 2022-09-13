from pytest_bdd import scenarios, given, when, then, parsers
from ui_tests.page_objects.home_page import HomePage

scenarios('../features/home_page.feature')

@when("I open the home page")
def open_home_page(driver, config):
    home_page = HomePage(driver, config)
    home_page.open()