from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        super().__init__(driver)

    def is_overview_page_displayed(self):
        return self.get_text(self.PAGE_TITLE) == "Checkout: Overview"

    def click_finish(self):
        finish = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            finish
        )

        self.driver.execute_script(
            "arguments[0].click();",
            finish
        )

        print("URL after Finish:")
        print(self.driver.current_url)

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-complete.html")
    )