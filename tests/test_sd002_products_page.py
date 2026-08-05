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


    # add all products to cart and remove all
    # add all products to cart to checkout and complete the purchase

# python -m pytest -v tests/test_sd002_products_page.py