from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from selenium.webdriver.common.by import By
from configs.settings import BASE_URL

class checkout_page(BasePage):

    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

    def __init__(self, driver):
        super().__init__(driver)

    def fill_checkout_form(self):
        self.open_url()

        ProductsPage.add_product_to_cart()

        self.type_text(self.FIRST_NAME_INPUT, "First")
        self.type_text(self.LAST_NAME_INPUT, "Last")
        self.type_text(self.POSTAL_CODE_INPUT, "86027540")
        self.click_on_element(self.CONTINUE_BUTTON)
        return self

    