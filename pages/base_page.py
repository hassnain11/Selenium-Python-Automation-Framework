from email.mime import text
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    WebDriverException,
    StaleElementReferenceException
)
from selenium.webdriver import Keys

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

    from selenium.webdriver.common.keys import Keys

    def type(self, locator, text):
        logger.info(f"Typing into: {locator}")

        element = self.wait.wait_for_element_visible(locator)

    # Wait until enabled
        WebDriverWait(self.driver, 10).until(
        lambda d: element.is_enabled()
        )

    # Scroll into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

    # Click to focus
        element.click()

    # Clear the field
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)

    # Type the value
        element.send_keys(text)

    # Fallback for GitHub Actions
        if element.get_attribute("value") != text:
            self.driver.execute_script(
                "arguments[0].value = arguments[1];",
                element,
                text
        )

        assert element.get_attribute("value") == text, \
            f"Failed to type '{text}' into {locator}"

    def get_text(self, locator):
        logger.info(f"Reading text: {locator}")

        element = self.wait.wait_for_element_visible(locator)

        return element.text.strip()

    def is_displayed(self, locator):
        try:
            return self.wait.wait_for_element_visible(locator).is_displayed()
        except Exception:
            return False