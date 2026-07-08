from pages.login_page import LoginPage
from config.config import *


def test_invalid_username(driver):

    login = LoginPage(driver)

    login.login(INVALID_USERNAME, STANDARD_PASSWORD)

    assert "Epic sadface" in login.get_error_message()