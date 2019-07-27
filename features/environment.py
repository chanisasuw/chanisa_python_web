from selenium import webdriver
from browser import Browser
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.promotional_codes import PromotionalCodes
# import HTMLTestRunner

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.search_page = SearchPage()
    context.promotional_codes = PromotionalCodes()

def after_all(context):
    context.browser.close()