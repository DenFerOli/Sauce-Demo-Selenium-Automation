import sys
import os
import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestLogin:
    def test_sd001_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in driver.current_url.lower()

    def test_sd002_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.invalid_login()
        error_message = login_page.get_error_message()
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        
        assert error_message == expected_message, f"Expected message: '{expected_message}', but receive: '{error_message}'"

    def test_sd003_invalid_login_no_password(self, driver):
        login_page = LoginPage(driver)
        login_page.invalid_login_no_password()
        error_message = login_page.get_error_message()
        expected_message = "Epic sadface: Password is required"

        assert error_message == expected_message, f"Expected message: '{expected_message}', but receive: '{error_message}'"

    def test_sd004_invalid_login_no_username(self, driver):
        login_page = LoginPage(driver)
        login_page.invalid_login_no_username()
        error_message = login_page.get_error_message()
        expected_message = "Epic sadface: Username is required"

        assert error_message == expected_message, f"Expected message: '{expected_message}', but receive: '{error_message}'"

    def test_sd005_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.locked_out_user()
        error_message = login_page.get_error_message()
        expected_message = "Epic sadface: Sorry, this user has been locked out."

        assert error_message == expected_message, f"Expected message: '{expected_message}', but receive: '{error_message}'"

# python -m pytest -v tests/test_sd001_login_page.py