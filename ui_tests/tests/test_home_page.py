from ast import And
from pytest_bdd import scenarios, given, when, then, parsers
from ui_tests.page_objects.home_page import HomePage

scenarios('../features/home_page.feature')

@when("I open the home page")
def open_home_page(driver, config):
    HomePage(driver, config).open()

@then(parsers.parse('the page title is "{page_title}"'))
def page_title_equal(driver, config, page_title):
    assert HomePage(driver, config).get_title().text == page_title

@then(parsers.parse('the sub-header text is "{subheader}"'))
def subheader_is_equal(driver, config, subheader):
    assert HomePage(driver, config).get_subheader().text == subheader