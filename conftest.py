import os
from datetime import datetime

import pytest

from config.config import BASE_URL
from config.credentials import STANDARD_USERNAME, STANDARD_PASSWORD
from pages.login_page import LoginPage
from utilities.driver_factory import DriverFactory
from utilities.logger import logger


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser: chrome | edge | firefox"
    )


@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")

    driver = DriverFactory.get_driver(browser=browser)

    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):

    login = LoginPage(driver)

    login.login(
        STANDARD_USERNAME,
        STANDARD_PASSWORD
    )

    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            file_path = os.path.join(
                "screenshots",
                f"{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(file_path)

            logger.error(
                f"Screenshot saved: {file_path}"
            )