from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from configs.settings import BASE_URL

class ProductsPage():

    sauce_labs_backpack_add_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-backpack')
    cart_message = (By.XPATH, "//span[@class='title' and @data-test='title' and text()='Your Cart']")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self):
        self.open_url()
        LoginPage.login(self, "standard_user", "secret_sauce")
        self.wait_for_element_to_be_clickable(self.sauce_labs_backpack_add_to_cart_button)
        self.click_on_element(self.sauce_labs_backpack_add_to_cart_button)
        self.wait_for_element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))
        self.click_on_element(By.CLASS_NAME, 'shopping_cart_link')
        # <a class="shopping_cart_link" data-test="shopping-cart-link"><span class="shopping_cart_badge" data-test="shopping-cart-badge">1</span></a>
        
        return self


    