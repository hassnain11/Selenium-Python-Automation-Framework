from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def is_inventory_page_displayed(self):
        return self.get_text(self.TITLE).strip() == "Products"

    def add_backpack_to_cart(self):

        self.click(self.ADD_BACKPACK)

        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(
            self.CART_BADGE
        )
    )

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.REMOVE_BACKPACK)
        )



def open_cart(self):

    cart = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.SHOPPING_CART)
    )

    # Scroll the cart into view
    self.driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        cart
    )

    # Use JavaScript click (more reliable in headless mode)
    self.driver.execute_script(
        "arguments[0].click();",
        cart
    )

    WebDriverWait(self.driver, 10).until(
        EC.url_contains("cart.html")
    )

    print("URL after cart click:")
    print(self.driver.current_url)

    def get_cart_count(self):
        try:
            return self.get_text(self.CART_BADGE).strip()
        except Exception:
            return "0"