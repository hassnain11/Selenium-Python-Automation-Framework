import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.regression
def test_cart_page(logged_in_driver):

    inventory = InventoryPage(logged_in_driver)

    inventory.add_backpack_to_cart()

    inventory.open_cart()

    cart = CartPage(logged_in_driver)

    assert cart.is_cart_page_displayed()

    assert cart.get_product_name() == "Sauce Labs Backpack"

    assert cart.get_cart_count() == "1"

@pytest.mark.regression
def test_remove_product_from_cart(logged_in_driver):

    inventory = InventoryPage(logged_in_driver)

    inventory.add_backpack_to_cart()

    inventory.open_cart()

    cart = CartPage(logged_in_driver)

    cart.remove_product()

    assert cart.get_cart_count() == "0"