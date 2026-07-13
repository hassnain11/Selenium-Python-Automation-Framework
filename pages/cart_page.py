from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def is_cart_page_displayed(self):
        return self.get_text(self.PAGE_TITLE) == "Your Cart"

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def click_checkout(self):

        checkout = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )

    # Scroll into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            checkout
        )

    # JS click (more reliable in headless)
        self.driver.execute_script(
            "arguments[0].click();",
            checkout
        )

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )

        print("URL after checkout:")
        print(self.driver.current_url)

    def remove_product(self):

        self.click(self.REMOVE_BUTTON)

        WebDriverWait(self.driver, 10).until(
            lambda d: len(
                d.find_elements(*self.CART_BADGE)
            ) == 0
        )

    def get_cart_count(self):

        badges = self.driver.find_elements(*self.CART_BADGE)

        if badges:
            return badges[0].text.strip()

        return "0"