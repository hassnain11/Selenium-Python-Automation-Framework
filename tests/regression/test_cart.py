import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.regression
def test_cart_page(logged_in_driver):

    inventory = InventoryPage(logged_in_driver)

    inventory.add_backpack_to_cart()

    print("Current URL after add:")
    print(logged_in_driver.current_url)

    inventory.open_cart()

    print("Current URL after cart click:")
    print(logged_in_driver.current_url)

    print("Page Source:")
    print(logged_in_driver.page_source[:2000])

    cart = CartPage(logged_in_driver)

    print("Title Text:")
    print(cart.get_text(cart.PAGE_TITLE))

    assert cart.is_cart_page_displayed()