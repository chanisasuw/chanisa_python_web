from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.support.select import Select

class SearchPageLocator(object):
    # Search Results Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")


class SearchPage(Browser):
    # Search Results Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_element_by_xpath(self, *locator):
     	self.driver.find_element_by_xpath(*locator)

    def get_element_by_id(self, *locator):
    	self.driver.find_element_by_id(*locator)

    def verify_text(self, *locator):
    	self.driver.find_element_by_xpath(*locator)

    def click_element(self, *locator):
    	self.driver.find_element_by_xpath(*locator).click()

    def get_page_title(self):
        return self.driver.title

    # def find_search_result(self, search_result):
    #     return self.get_element(By.LINK_TEXT, search_result)

    def find_search_result(self, *locator):
    	return self.driver.find_element_by_xpath(*locator).text