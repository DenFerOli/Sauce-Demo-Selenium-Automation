from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from configs.settings import BASE_URL
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class ProductsPage(BasePage):

    products_list = [
        "add-to-cart-sauce-labs-backpack",
"add-to-cart-sauce-labs-bike-light",
"add-to-cart-sauce-labs-bolt-t-shirt",
"add-to-cart-sauce-labs-fleece-jacket",
"add-to-cart-sauce-labs-onesie",
"add-to-cart-test.allthethings()-t-shirt-(red)"
    ]

    sauce_labs_backpack_add_to_cart_button = (By.ID, products_list[0])
    shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')
    cart_title = (By.XPATH, "//span[@class='title' and @data-test='title' and text()='Your Cart']")
    inventory_name = (By.CLASS_NAME, 'inventory_item_name')
    cart_item = (By.CLASS_NAME, 'cart_item')
    cart_item_name = (By.CLASS_NAME, 'inventory_item_name')
    cart_remove_button = (By.ID, 'remove-sauce-labs-backpack')



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

    def add_all_products_to_cart(self):

        for product in self.products_list:
            add_to_cart_button = (By.ID, product)
            try:
                self.wait_for_element(add_to_cart_button, timeout=5)
                self.click_on_element(add_to_cart_button)
                time.sleep(0.3)
            except TimeoutException:
                print(f"Error: Could not add product with ID '{product}': {e}")
                raise
            
 
            

    def remove_product_from_cart(self):

        self.wait_for_element(self.cart_remove_button)
        self.click_on_element(self.cart_remove_button)

        return self

    def is_element_present(self, locator, timeout=2):
        try:
            self.wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_not_present(self, locator, timeout=2):
        try:
            self.wait_for_element(locator, timeout)
            return False
        except TimeoutException:
            return True

    def get_cart_items_count(self):
        # cart_items = self.driver.find_elements(*self.cart_item)
        # return len(cart_items)
        try:
            badge = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
            return int(badge.text)
        except NoSuchElementException:
            return 0
        
    def get_cart_title_text(self):
        element = self.wait_for_element(self.cart_title)
        return element.text

    