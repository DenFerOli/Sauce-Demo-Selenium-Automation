import sys
import os
import pytest
from pages.products_page import ProductsPage

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestProducts:
    
    def test_sd002_add_product(self, driver):
        products_page = ProductsPage(driver)
        products_page.add_product_to_cart()
        cart_message = products_page.get_cart_title_text()
        expected_message = "Your Cart"

        assert cart_message == expected_message, f"Expected message: '{expected_message}', but receive: '{cart_message}'"

    def test_sd003_remove_product(self, driver):
        products_page = ProductsPage(driver)
        products_page.add_product_to_cart()
        assert products_page.get_cart_items_count() == 1, "Expected 1 item in the cart after adding a product."
        products_page.remove_product_from_cart()
        assert products_page.get_cart_items_count() == 0, "Expected 0 items in the cart after removing the product."

    def test_sd004_add_all_products(self, driver):
        products_page = ProductsPage(driver)
        products_page.add_all_products_to_cart()
        cart_count = products_page.get_cart_items_count()

        assert cart_count == len(products_page.products_list), f"Expected {len(products_page.products_list)} items, but got {cart_count}"

        badge_text = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert int(badge_text) == len(products_page.products_list)

    # add all products to cart and remove all
    # add all products to cart to checkout and complete the purchase

# python -m pytest -v tests/test_sd002_products_page.py