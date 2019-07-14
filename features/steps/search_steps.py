from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I open TrueID Home Page')
def step_impl(context):
    context.home_page.navigate("https://home.trueid.net")
    assert_equal(context.home_page.get_page_title(), "TrueID ทรูไอดี ที่เดียวครบสุด.. ทุกความสนุกและสิทธิพิเศษ ดูหนังออนไลน์ ดูช่องทีวีดิจิตอลฟรี")

@step('I verify main menu that existing "{menu_name}"')
def step_impl(context, menu_name):
    context.home_page.menu(menu_name)

@step('I am taken to the PyPi Search Results page')
def step_impl(context):
    assert_equal(context.search_results_page.get_page_title(), "Index of Packages Matching 'behave' : Python Package Index")

@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result))
