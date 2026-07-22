import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests import conftest


class TestLogin:
    def test_sd001_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("standard", "secret_sauce")
        assert "inventory" in driver.current_url.lower()