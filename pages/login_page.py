from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def login(self, username, password):
        USERNAME = (By.ID, "user-name")
        PASSWORD = (By.ID, "password")
        LOGIN_BTN = (By.ID, "login-button")

        self.type(USERNAME, username)
        self.type(PASSWORD, password)
        self.click(LOGIN_BTN)
