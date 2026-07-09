from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        super().__init__(driver)

    def is_overview_page_displayed(self):
        return self.get_text(self.PAGE_TITLE) == "Checkout: Overview"

    def click_finish(self):
        self.click(self.FINISH_BUTTON)