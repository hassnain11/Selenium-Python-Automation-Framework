from selenium.webdriver.common.by import By

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
        return self.get_text(self.PAGE_TITLE).strip() == "Your Cart"

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def click_checkout(self):
        button = self.wait.wait_for_element_clickable(self.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    def remove_product(self):
        button = self.wait.wait_for_element_clickable(self.REMOVE_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)

        if not badges:
            return "0"

        return badges[0].text.strip()