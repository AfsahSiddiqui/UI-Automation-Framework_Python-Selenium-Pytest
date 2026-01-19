from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def enter_details(self, fname, lname, zip_code):
        FIRST_NAME = (By.ID, "first-name")
        LAST_NAME = (By.ID, "last-name")
        POSTAL_CODE = (By.ID, "postal-code")
        CONTINUE_BTN = (By.ID, "continue")

        self.type(FIRST_NAME, fname)
        self.type(LAST_NAME, lname)
        self.type(POSTAL_CODE, zip_code)
        self.click(CONTINUE_BTN)
    
    def cancel_checkout(self):
        locator = (By.ID, "cancel")
        self.click(locator)

    def finish_checkout(self):
        locator = (By.ID, "finish")
        self.click(locator)
