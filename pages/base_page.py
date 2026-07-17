from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from configs.settings import DEFAULT_TIMEOUT, BASE_URL, SCREENSHOTS_DIR
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL
        self.timeout = DEFAULT_TIMEOUT
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def type_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    


    def open(self, url=''):
        full_url = self.base_url + url
        self.driver.get(full_url)
        return self
    
    def wait_for_element(self, locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def take_screenshot(self, name=None):

        if not name:
            name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        filepath = os.path.join(SCREENSHOTS_DIR, f"{name}.png")
        self.driver.save_screenshot(filepath)
        return filepath
    