import sys
import os
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestProducts:
    
    def test_sd002_add_product(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in driver.current_url.lower()