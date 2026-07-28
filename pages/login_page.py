from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from configs.settings import BASE_URL

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, '//button[@data-test="error-button"]')

    username = "standard_user"
    password = "secret_sauce"

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.open_url()
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click_on_element(self.LOGIN_BUTTON)
        return self

    def invalid_login(self):
        self.open_url()
        self.type_text(self.USERNAME_INPUT, "invalid")
        self.type_text(self.PASSWORD_INPUT, "invalid")
        self.click_on_element(self.LOGIN_BUTTON)
        return self

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except:
            return None