from pages.login_page import LoginPage

from config.credentials import (
    INVALID_USERNAME,
    STANDARD_PASSWORD
)


def test_invalid_username(driver):

    login = LoginPage(driver)

    login.login(
        INVALID_USERNAME,
        STANDARD_PASSWORD
    )

    actual_error = login.get_error_message()

    assert actual_error == "Epic sadface: Username and password do not match any user in this service"