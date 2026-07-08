import pytest

from pages.login_page import LoginPage
from utilities.excel_reader import read_excel_data

login_data = read_excel_data(
    "login_data.xlsx",
    "LoginData"
)


@pytest.mark.parametrize("data", login_data)
def test_invalid_login_excel(driver, data):

    login = LoginPage(driver)

    login.login(
        data["username"],
        data["password"]
    )

    actual_error = login.get_error_message()

    assert actual_error == data["expected_error"]
    