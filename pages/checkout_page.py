from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from configs.settings import BASE_URL


class checkout_page(BasePage):

    first_name_input = (By.ID, 'first-name')
    last_name_input = (By.ID, 'last-name')
    postal_code_input = (By.ID, 'postal-code')
    continue_button = (By.ID, 'continue')

    def __init__(self, driver):
        super().__init__(driver)

