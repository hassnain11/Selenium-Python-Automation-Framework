import os
from datetime import datetime

import pytest

from config.config import BASE_URL
from config.credentials import STANDARD_USERNAME, STANDARD_PASSWORD
from pages.login_page import LoginPage
from utilities.driver_factory import DriverFactory
from utilities.logger import logger
from utilities.screenshot import take_screenshot


@pytest.fixture
def driver():

    driver = DriverFactory.get_driver()

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

    if report.when == "call" and report.failed":

        driver = item.funcargs.get("driver")

        if driver:

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}_{timestamp}.png"
            )

            take_screenshot(driver, screenshot_path)

            logger.error(
                f"Test Failed - Screenshot saved: {screenshot_path}"
            )