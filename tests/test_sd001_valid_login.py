import pytest
from selenium.webdriver.common.by import By
import conftest
from conftest import driver
from pages.login_page import LoginPage

# class TestSD001:
#     def test_sd001_valid_login(self):
#         driver = conftest.driver
#         LoginPage
#         assert 


class TestLogin:
    def test_sd001_valid_login(self):
        