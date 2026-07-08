from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = Logger.get_logger()

    def click(self, locator):
        self.logger.info(f"Clicking on element: {locator}")
        self.wait.until(
        EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        self.logger.info(f"Typing into element: {locator}")

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        self.logger.info(f"Reading text from: {locator}")
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text