from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

## Story 3
@step('Enter promotion code "{promocodes}"')
def step_impl(context, promocodes):
	context.promotional_codes.enter_promocode(promocodes)

@step('User found message promotional code :"{element}"')
def step_impl(context, element):
	context.search_page.find_search_result("//*[@id='content']/p[2]")
	context.search_page.verify_text("//*[contains(text(), '" + element + "')]")
	# context.promotional_codes.validate_text(element)

@step('check discount "{element}"')
def step_impl(context, element):
	context.search_page.find_search_result("//*[@id='content']/p[2]")
	context.search_page.verify_text("//*[contains(text(), '" + element + "')]")