from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    # Locators
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
        self.click(self.CHECKOUT_BUTTON)

    def remove_product(self):
        self.click(self.REMOVE_BUTTON)

    def get_cart_count(self):
        try:
            return self.get_text(self.CART_BADGE)
        except Exception:
            return "0"