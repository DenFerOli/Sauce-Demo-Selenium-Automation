from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from configs.settings import BASE_URL

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, '//div[@class="error-message-container error"]//h3') 

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

    def invalid_login_no_username(self):
        self.open_url()
        self.type_text(self.USERNAME_INPUT, "")
        self.type_text(self.PASSWORD_INPUT, "test")
        self.click_on_element(self.LOGIN_BUTTON)
        return self

    def invalid_login_no_password(self):
        self.open_url()
        self.type_text(self.USERNAME_INPUT, "test")
        self.type_text(self.PASSWORD_INPUT, "")
        self.click_on_element(self.LOGIN_BUTTON)
        return self

    def locked_out_user(self):
        self.open_url()
        self.type_text(self.USERNAME_INPUT, "locked_out_user")
        self.type_text(self.PASSWORD_INPUT, "secret_sauce")
        self.click_on_element(self.LOGIN_BUTTON)
        return self

    def get_error_message(self):
        try:
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            
            error_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.ERROR_MESSAGE)
            )
            return error_element.text
        except:
            return None