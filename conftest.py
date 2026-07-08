import os
from datetime import datetime

import pytest

from config.config import BASE_URL
from utilities.driver_factory import DriverFactory
from utilities.screenshot import take_screenshot
from utilities.logger import logger


@pytest.fixture
def driver():

    driver = DriverFactory.get_driver()

    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call":

        if report.failed:

            driver = item.funcargs["driver"]

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_name = f"{item.name}_{timestamp}.png"

            screenshot_path = os.path.join(
                "screenshots",
                screenshot_name
            )

            take_screenshot(driver, screenshot_path)

            logger.error(
                f"Test Failed - Screenshot saved: {screenshot_path}"
            )