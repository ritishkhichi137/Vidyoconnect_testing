from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class WaitHandler:
    @staticmethod
    def wait_for_element(driver, xpath, timeout=20, demo_mode=False):
        """Wait for element to be clickable with optional demo mode delay"""
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            if demo_mode:
                WebDriverWait(driver, 3).until(lambda x: True)  # 3-second delay for demo
            return element
        except TimeoutException:
            raise TimeoutException(f"Element not clickable: {xpath}")