from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    def remove_product(self, product_name):
        product_name = product_name.lower().replace(' ','-')
        locator = (By.XPATH, f"//button[contains(@data-test,'{product_name}')]")
        self.click(locator)
    
    def continue_shopping(self):
        locator = (By.ID, "continue-shopping")
        self.click(locator)

    def proceed_to_checkout(self):
        locator = (By.ID, "checkout")
        self.click(locator)
