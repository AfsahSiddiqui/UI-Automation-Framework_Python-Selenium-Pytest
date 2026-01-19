from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):

    def get_success_message(self):
        locator = (By.CLASS_NAME, "complete-header")
        return self.get_text(locator)
