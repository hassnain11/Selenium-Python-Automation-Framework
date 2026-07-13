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

        # Click to focus the element
        element.click()
        time.sleep(0.2)

        # Clear field completely
        element.send_keys(Keys.CONTROL + "a")
        time.sleep(0.1)
        element.send_keys(Keys.DELETE)
        time.sleep(0.2)

        # Type text one character at a time
        print(f"Typing text: {text}")
        for char in text:
            element.send_keys(char)
            time.sleep(0.05)

        time.sleep(0.3)

        # Verify the text was entered
        actual = element.get_attribute("value")
        actual = actual if actual else ""

        print(f"Expected: {text}")
        print(f"Actual  : {actual}")

        # If keyboard didn't work, use JavaScript with React event handling
        if actual != text:
            print("Using JavaScript to set value...")
            self.driver.execute_script("""
                const input = arguments[0];
                const value = arguments[1];
                
                // Clear and set value
                input.value = '';
                input.value = value;
                
                // Try to find React onChange handler
                const keys = Object.keys(input);
                const reactKey = keys.find(k => k.startsWith('__reactProps'));
                
                if (reactKey && input[reactKey].onChange) {
                    // Call React's onChange directly
                    input[reactKey].onChange({ target: { value: value } });
                } else {
                    // Fallback: dispatch events
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                }
            """, element, text)
            
            time.sleep(0.3)
            actual = element.get_attribute("value")
            actual = actual if actual else ""
            print(f"After JavaScript - Expected: {text}, Actual: {actual}")

        assert actual == text, f"Failed to type '{text}'. Got: '{actual}'"

    def get_text(self, locator):
        logger.info(f"Reading text: {locator}")

        element = self.wait.wait_for_element_visible(locator)

        return element.text.strip()

    def is_displayed(self, locator):
        try:
            return self.wait.wait_for_element_visible(locator).is_displayed()
        except Exception:
            return False
