from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException
)

class WaitHelper:

    def __init__(self, driver, timeout=10):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            timeout,
            ignored_exceptions=[
                StaleElementReferenceException
            ]
        )

    def wait_for_element_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )