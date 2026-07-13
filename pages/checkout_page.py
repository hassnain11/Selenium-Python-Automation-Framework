from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        super().__init__(driver)

    def is_checkout_page_displayed(self):
        return self.get_text(self.PAGE_TITLE).strip() == "Checkout: Your Information"

    def enter_first_name(self, first_name):
        self.type(self.FIRST_NAME, first_name)

    def enter_last_name(self, last_name):
        self.type(self.LAST_NAME, last_name)

    def enter_postal_code(self, postal_code):
        self.type(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        button = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(self.CONTINUE_BUTTON)
    )

        self.driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        button
    )

        WebDriverWait(self.driver, 2).until(
        lambda d: button.is_enabled()
    )

        self.driver.execute_script(
        "arguments[0].click();",
        button
    )

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()