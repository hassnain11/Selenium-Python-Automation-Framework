import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


@pytest.mark.regression
def test_complete_purchase(logged_in_driver):

    inventory = InventoryPage(logged_in_driver)

    inventory.add_backpack_to_cart()
    inventory.open_cart()

    WebDriverWait(logged_in_driver, 10).until(
        EC.url_contains("cart.html")
    )

    cart = CartPage(logged_in_driver)

    assert cart.is_cart_page_displayed()

    cart.click_checkout()

    WebDriverWait(logged_in_driver, 10).until(
        EC.url_contains("checkout-step-one.html")
    )

    checkout = CheckoutPage(logged_in_driver)

    assert checkout.is_checkout_page_displayed()

    checkout.fill_checkout_information(
        "Muhammad",
        "Hassnain",
        "75000"
    )

    WebDriverWait(logged_in_driver, 10).until(
        EC.url_contains("checkout-step-two.html")
    )

    overview = CheckoutOverviewPage(logged_in_driver)

    assert overview.is_overview_page_displayed()

    overview.click_finish()

    WebDriverWait(logged_in_driver, 10).until(
        EC.url_contains("checkout-complete.html")
    )

    complete = CheckoutCompletePage(logged_in_driver)

    assert complete.is_complete_page_displayed()

    assert complete.get_success_message() == "Thank you for your order!"