from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from selenium.webdriver.common.by import By
from configs.settings import BASE_URL

class CheckoutPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, 'checkout')
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')

    def __init__(self, driver):
        super().__init__(driver)

    def fill_checkout_form(self):
        self.open_url()
        products_page = ProductsPage(self.driver)
        products_page.add_product_to_cart()
        self.click_on_element(self.CHECKOUT_BUTTON)
        self.type_text(self.FIRST_NAME_INPUT, "First")
        self.type_text(self.LAST_NAME_INPUT, "Last")
        self.type_text(self.POSTAL_CODE_INPUT, "123456")
        self.click_on_element(self.CONTINUE_BUTTON)
        return self

    def complete_checkout(self):
        self.open_url()
        products_page = ProductsPage(self.driver)
        products_page.add_product_to_cart()
        self.click_on_element(self.CHECKOUT_BUTTON)
        self.type_text(self.FIRST_NAME_INPUT, "First")
        self.type_text(self.LAST_NAME_INPUT, "Last")
        self.type_text(self.POSTAL_CODE_INPUT, "123456")
        self.click_on_element(self.CONTINUE_BUTTON)
        self.click_on_element(self.FINISH_BUTTON)




        # login_page = LoginPage(self.driver)
        # login_page.login("standard_user", "secret_sauce")