import pytest

from utilities.driver_factory import DriverFactory
from utilities.screenshot import Screenshot
from utilities.logger import Logger


logger = Logger.get_logger()


@pytest.fixture
def driver(request):

    driver = DriverFactory.get_driver()

    yield driver

    if request.node.rep_call.failed:

        path = Screenshot.capture(driver, request.node.name)

        logger.error(f"Test Failed - Screenshot saved: {path}")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)