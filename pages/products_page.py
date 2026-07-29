from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from configs.settings import BASE_URL

class ProductsPage():

    def __init__(self, driver):
        super().__init__(driver)

    