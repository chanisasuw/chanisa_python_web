from selenium import webdriver
from browser import Browser
from pages.home_page import HomePage
from pages.search_page import SearchPage
# import HTMLTestRunner

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.search_page = SearchPage()

def after_all(context):
    context.browser.close()