# tests/test_sd001_valid_login.py
import sys
import os

# Adiciona o diretório pai ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from pages.login_page import LoginPage

# NÃO precisa importar conftest! O pytest encontra automaticamente


class TestLogin:
    def test_sd001_valid_login(self, driver):  # <-- driver vem do conftest automaticamente
        """Teste de login válido no SauceDemo"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url.lower()

# pytest -v tests/test_sd001_valid_login.py