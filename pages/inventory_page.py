from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    SHOPPING_CART = (By.ID, "shopping_cart_container")
    TITLE = (By.CLASS_NAME, "title")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def is_inventory_page_displayed(self):
        return "inventory.html" in self.driver.current_url

    def get_page_title(self):
        return self.get_text(self.TITLE)

    def open_cart(self):
        self.click(self.SHOPPING_CART)

    def open_menu(self):
        self.click(self.BURGER_MENU)

    def logout(self):
        self.open_menu()
        self.click(self.LOGOUT_LINK)