from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

## Story 3
@step('User open Mars Airlines Home Page')
def step_impl(context):
    context.home_page.navigate("https://marsair.thoughtworks-labs.net/chanisa")
    assert_equal(context.home_page.get_page_title(), "Mars Airlines: Home")

@step('User verify search flight box that existing')
def step_impl(context):
    context.home_page.searchfrom("content")

@step('User found "{text_name}" on search flight box')
def step_impl(context, text_name):
	context.search_page.verify_text("//*[text()='" + text_name + "']")

@step('User clicking MarsAir logo')
def step_impl(context):
	context.home_page.click_element("//*[@id='app']/h1/a")

@step('Redirect to home page')
def step_iml(context):
	assert_equal(context.home_page.get_page_title(), "Mars Airlines: Home")

@step('Redirect to Search Results page')
def step_iml(context):
	assert_equal(context.home_page.get_page_title(), "Mars Airlines: Search Results")

@step('User click search button')
def step_iml(context):
	context.home_page.click_element("//*[@id='content']/form/dl[4]/dd/input")
	assert_equal(context.home_page.get_page_title(), "Mars Airlines: Search Results")
    
@step('User can redirect to home page by clicking "{text_name}"')
def step_impl(context, text_name):
    context.home_page.searchfrom("text_name")

@step('User search flight by select departure July and return July next year')
def step_impl(context):
    assert_equal(context.search_results_page.get_page_title(), "Index of Packages Matching 'behave' : Python Package Index")

@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result))
