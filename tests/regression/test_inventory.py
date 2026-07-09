import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from config.credentials import (
    STANDARD_USERNAME,
    STANDARD_PASSWORD
)


@pytest.mark.regression
def test_add_backpack_to_cart(driver):

    login = LoginPage(driver)

    login.login(
        STANDARD_USERNAME,
        STANDARD_PASSWORD
    )

    inventory = InventoryPage(driver)

    assert inventory.is_inventory_page_displayed()

    inventory.add_backpack_to_cart()

    assert inventory.get_cart_count() == "1"