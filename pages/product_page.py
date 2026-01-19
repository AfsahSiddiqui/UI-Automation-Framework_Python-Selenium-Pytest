from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    
    def add_to_cart(self):
        locator = (By.ID, "add-to-cart")
        self.click(locator)
    
    def go_to_cart(self):
        locator = (By.CLASS_NAME, "shopping_cart_link")
        self.click(locator)
