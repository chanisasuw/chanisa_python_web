from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.common.keys import Keys

class PromotionalCodesLocator(object):

	PROMOCODE_FIELD = (By.ID, "promotional_code")
	PROMOCODE_MESSAGE = (By.XPATH, "//*[@id='content']/p[2]")

class PromotionalCodes(Browser):
    # Search Results Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def enter_promocode(self, promocode):
    	self.fill(promocode, *PromotionalCodesLocator.PROMOCODE_FIELD)

    def get_text(self, text, *locator):
        self.driver.getText(*locator).contains(text)

    def validate_text(self, text):
    	self.get_text(text, *PromotionalCodesLocator.PROMOCODE_MESSAGE)