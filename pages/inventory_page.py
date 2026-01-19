from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    
    def add_product_to_cart(self, product_name):
        product_name = product_name.lower().replace(' ','-')
        locator = (By.XPATH, f"//button[contains(@data-test,'{product_name}')]")
        self.click(locator)
    
    def remove_product_from_cart(self, product_name):
        product_name = product_name.lower().replace(' ','-')
        locator = (By.XPATH, f"//button[contains(@data-test,'{product_name}')]")
        self.click(locator)

    def see_product_page(self, product_name):
        locator = (By.XPATH, f"//div[contains(text(),'{product_name}')]")
        self.click(locator)

    def go_to_cart(self):
        locator = (By.CLASS_NAME, "shopping_cart_link")
        self.click(locator)
