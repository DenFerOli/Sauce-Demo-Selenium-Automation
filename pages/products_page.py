from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from configs.settings import BASE_URL

class ProductsPage(BasePage):

    sauce_labs_backpack_add_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-backpack')
    shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')
    cart_title = (By.XPATH, "//span[@class='title' and @data-test='title' and text()='Your Cart']")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login("standard_user", "secret_sauce")
        self.wait_for_element(self.sauce_labs_backpack_add_to_cart_button)
        self.click_on_element(self.sauce_labs_backpack_add_to_cart_button)
        self.wait_for_element(self.shopping_cart_link)
        self.click_on_element(self.shopping_cart_link)
        
        return self

    def get_cart_title_text(self):
        element = self.wait_for_element(self.cart_title)
        return element.text

    