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

        # Wait a moment for the element to be stable
        time.sleep(0.5)

        # Make sure element is focused and ready
        element.click()
        time.sleep(0.3)

        # Clear the field using JavaScript and trigger input event
        self.driver.execute_script("""
            arguments[0].value = '';
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, element)
        
        time.sleep(0.3)
        
        # Send the text
        element.send_keys(text)
        time.sleep(0.3)

        actual = element.get_attribute("value")
        actual = actual if actual else ""

        print(f"Expected: {text}")
        print(f"Actual  : {actual}")

        if actual != text:
            print("Retrying with alternative method...")
            # Use JavaScript to set the value directly
            self.driver.execute_script("""
                arguments[0].focus();
                arguments[0].value = arguments[1];
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('blur', { bubbles: true }));
            """, element, text)
            time.sleep(0.5)
            actual = element.get_attribute("value")
            actual = actual if actual else ""
            print(f"After retry - Expected: {text}, Actual: {actual}")

        if actual != text:
            raise AssertionError(f"Failed to type '{text}'. Actual value: '{actual}'")

    def get_text(self, locator):
        logger.info(f"Reading text: {locator}")

        element = self.wait.wait_for_element_visible(locator)

        return element.text.strip()

    def is_displayed(self, locator):
        try:
            return self.wait.wait_for_element_visible(locator).is_displayed()
        except Exception:
            return False
