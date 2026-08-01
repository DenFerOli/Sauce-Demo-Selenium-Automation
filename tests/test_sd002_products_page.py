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

# python -m pytest -v tests/test_sd002_products_page.py