from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)

    def is_complete_page_displayed(self):
        return self.get_text(self.PAGE_TITLE) == "Checkout: Complete!"

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def click_back_home(self):
        self.click(self.BACK_HOME)