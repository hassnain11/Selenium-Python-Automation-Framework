from selenium.common.exceptions import (
    WebDriverException,
    StaleElementReferenceException
)

from selenium.webdriver.support.ui import WebDriverWait

from utilities.logger import logger
from utilities.wait_helper import WaitHelper


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    def click(self, locator):

        logger.info(f"Clicking: {locator}")

        for _ in range(3):

            try:

                element = self.wait.wait_for_element_clickable(locator)

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                WebDriverWait(self.driver, 5).until(
                    lambda d: element.is_displayed()
                )

                try:
                    element.click()

                except WebDriverException:

                    logger.warning("Normal click failed. Using JS click.")

                    self.driver.execute_script(
                        "arguments[0].click();",
                        element
                    )

                return

            except StaleElementReferenceException:

                logger.warning("Retrying after stale element...")

        raise Exception(f"Unable to click {locator}")

    def type(self, locator, text):

        logger.info(f"Typing into: {locator}")

        element = self.wait.wait_for_element_visible(locator)

        element.clear()

        element.send_keys(text)

    def get_text(self, locator):

        logger.info(f"Reading text: {locator}")

        return self.wait.wait_for_element_visible(locator).text.strip()

    def is_displayed(self, locator):

        try:
            return self.wait.wait_for_element_visible(locator).is_displayed()
        except:
            return False