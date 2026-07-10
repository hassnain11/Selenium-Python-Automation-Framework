from selenium.common.exceptions import WebDriverException
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

        except WebDriverException:

            logger.warning(
                f"Normal click failed. Using JavaScript click for {locator}"
            )

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    def type(self, locator, text):
        logger.info(f"Typing into: {locator}")

        element = self.wait.wait_for_element_visible(locator)

        element.clear()

        if text:
            element.send_keys(text)

    def get_text(self, locator):
        logger.info(f"Reading text: {locator}")

        element = self.wait.wait_for_element_visible(locator)

        return element.text.strip()

    def is_displayed(self, locator):
        try:
            return self.wait.wait_for_element_visible(locator).is_displayed()
        except Exception:
            return False