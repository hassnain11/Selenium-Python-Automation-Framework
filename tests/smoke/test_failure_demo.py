from pages.login_page import LoginPage

from config.credentials import (
    STANDARD_USERNAME,
    STANDARD_PASSWORD
)


def test_failure_demo(driver):

    login = LoginPage(driver)

    login.login(
        STANDARD_USERNAME,
        STANDARD_PASSWORD
    )

    assert False