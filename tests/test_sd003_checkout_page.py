import sys
import os
import pytest
from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestCheckout:
    def test_sd001_fill_checkout_form(self, driver):
        fill_checkout = CheckoutPage(driver)
        fill_checkout.fill_checkout_form()
        checkout_text = fill_checkout.get_text((By.CLASS_NAME, "title"))
        expected_text = "Checkout: Overview"

        assert checkout_text == expected_text, f"Expected text: '{expected_text}', but receive: '{checkout_text}'"

#python -m pytest -v tests/test_sd003_checkout_page.py