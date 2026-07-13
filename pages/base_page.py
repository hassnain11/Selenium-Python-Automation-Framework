from email.mime import text

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from selenium.common.exceptions import (
    WebDriverException,
    StaleElementReferenceException,
)

from utilities.logger import logger
from utilities.wait_helper import WaitHelper


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    def click(self, locator):
        logger.info(f"Clicking: {locator}")

        element = self.wait.wait_for_element_clickable(locator)

        try:
            element.click()

        except (WebDriverException, StaleElementReferenceException):

            logger.warning(
                f"Normal click failed. Using JavaScript click for {locator}"
            )

            element = self.wait.wait_for_element_clickable(locator)

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    
    def type(self, locator, text):
        logger.info(f"Typing into: {locator}")

        element = WebDriverWait(
            self.driver,
            10,
            ignored_exceptions=[StaleElementReferenceException]
        ).until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        time.sleep(0.5)

        # Triple-click to select all existing content
        element.click()
        time.sleep(0.1)
        element.click()
        time.sleep(0.1)
        element.click()
        time.sleep(0.3)

        # Clear using keyboard
        element.send_keys(Keys.CONTROL + "a")
        time.sleep(0.1)
        element.send_keys(Keys.BACKSPACE)
        time.sleep(0.3)

        print(f"Typing text: {text}")
        
        # Type character by character with longer delays
        for char in text:
            element.send_keys(char)
            time.sleep(0.1)  # Increased delay

        time.sleep(0.5)

        actual = element.get_attribute("value")
        actual = actual if actual else ""

        print(f"Expected: {text}")
        print(f"Actual  : {actual}")

        # If still empty, try JavaScript as final fallback
        if not actual:
            print("Value empty after typing. Trying JavaScript assignment...")
            self.driver.execute_script("""
                const input = arguments[0];
                const value = arguments[1];
                
                // Set the value
                input.value = value;
                
                // Trigger all necessary events
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
                input.dispatchEvent(new Event('blur', { bubbles: true }));
            """, element, text)
            time.sleep(0.5)
            actual = element.get_attribute("value")
            actual = actual if actual else ""
            print(f"After JS fallback - Expected: {text}, Actual: {actual}")

        assert actual == text, f"Expected '{text}' but got '{actual}'"

    def get_text(self, locator):
        logger.info(f"Reading text: {locator}")

        element = self.wait.wait_for_element_visible(locator)

        return element.text.strip()

    def is_displayed(self, locator):
        try:
            return self.wait.wait_for_element_visible(locator).is_displayed()
        except Exception:
            return False
