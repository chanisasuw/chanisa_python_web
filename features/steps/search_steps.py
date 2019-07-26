from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys

@step('It should be "{text_name}" field')
def step_impl(context, text_name):
	context.search_page.verify_text("//*[text()='" + text_name + "']")

@step('Finding "{element}" Flights leave field')
def step_impl(context, element):
	context.search_page.get_element_by_xpath("//*[@id='"+ element +"']")

@step('Select "{transfer}" : "{state}"')
def step_impl(context, transfer, state):
	context.search_page.click_element("//select[@id='" + transfer +"']")
	context.search_page.click_element("//select[@id='" + transfer +"']/option[text()='"+ state +"']")

@step('"{transfer}" found flight leave on "{state}"')
def step_impl(context, transfer ,state):
	context.search_page.get_element_by_xpath("//*[@id='" + transfer +"']/option[text()='"+ state +"']")

@step('Search flight without promo code')
def step_impl(context):
	context.search_page.click_element("//input[@type='submit']")
	assert_equal(context.home_page.get_page_title(), "Mars Airlines: Search Results")

@step('User found message "{element}"')
def step_impl(context, element):
	context.search_page.find_search_result("//*[@id='content']/p[1]")
	context.search_page.verify_text("//*[text()='" + element + "']")

