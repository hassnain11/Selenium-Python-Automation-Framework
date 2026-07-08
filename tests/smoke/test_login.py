from pages.login_page import LoginPage

from config.credentials import (
    STANDARD_USERNAME,
    STANDARD_PASSWORD
)


def test_valid_login(driver):

    login = LoginPage(driver)

    login.login(
        STANDARD_USERNAME,
        STANDARD_PASSWORD
    )

    assert login.is_inventory_page_displayed()