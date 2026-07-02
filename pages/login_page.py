from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from configs.settings import BASE_URL

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    #ERROR_MESSAGE = (By.CSS_SELECTOR, '')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.open()
        self.wait_for_element(self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self
    
    def get_error_message(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except:
            return None