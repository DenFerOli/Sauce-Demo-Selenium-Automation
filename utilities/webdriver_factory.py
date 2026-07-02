from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from configs.settings import (
    IMPLICIT_WAIT,
    PAGE_LOAD_TIMEOUT,
    PAGE_LOAD_STRATEGY,
    SCREENSHOTS_DIR,
    REPORTS_DIR
)
import os

class WebDriverFactory:
    @staticmethod
    def get_driver():
        chrome_options = Options()
        chrome_options.page_load_strategy = PAGE_LOAD_STRATEGY
        chrome_options.add_argument('--start-maximized')
        #chrome_options.add_argument('--headless')  # Uncomment this line to run in headless mode
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(IMPLICIT_WAIT)
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

        return driver