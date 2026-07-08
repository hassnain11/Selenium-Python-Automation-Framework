from pages.login_page import LoginPage
from config.config import *


def test_valid_login(driver):

    login = LoginPage(driver)

    inventory = login.login(
        STANDARD_USERNAME,
        STANDARD_PASSWORD
    )

    assert inventory.is_inventory_page_displayed()