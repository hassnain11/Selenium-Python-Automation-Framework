import pytest

from pages.login_page import LoginPage
from utilities.json_reader import read_json_data

login_data = read_json_data("login_data.json")


@pytest.mark.parametrize("data", login_data)
def test_invalid_login_ddt(driver, data):

    login = LoginPage(driver)

    login.login(
        data["username"],
        data["password"]
    )

    actual_error = login.get_error_message()

    assert actual_error == data["expected_error"]