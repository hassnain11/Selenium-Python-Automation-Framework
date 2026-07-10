from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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

        title = self.get_text(self.PAGE_TITLE)

        print("=" * 60)
        print("CURRENT URL:", self.driver.current_url)
        print("PAGE TITLE:", repr(title))
        print("=" * 60)

        return title.strip() == "Your Cart"

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME).strip()

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    
    def remove_product(self):
        self.click(self.REMOVE_BUTTON)

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.CART_BADGE)
    )

    def get_cart_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            print("BADGE:", repr(badge.text))
            return badge.text.strip()
        except NoSuchElementException:
            print("BADGE NOT FOUND")
            return "0"