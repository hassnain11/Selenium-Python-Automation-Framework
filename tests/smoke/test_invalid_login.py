from pages.login_page import LoginPage
from config.config import username, password


def test_invalid_username(driver):

    login = LoginPage(driver)
    login.login(username,password)

    assert "Epic sadface" in login.get_error_message()