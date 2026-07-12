from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.config import (
    BROWSER,
    HEADLESS,
    IMPLICIT_WAIT,
)

from utilities.logger import logger


class DriverFactory:

    @staticmethod
    def get_driver(browser=None, headless=None):

        browser = (browser or BROWSER).lower()
        headless = HEADLESS if headless is None else headless

        logger.info("=" * 60)
        logger.info(f"Starting {browser.upper()} WebDriver")
        logger.info(f"Headless : {headless}")

        if browser == "chrome":

            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")

            driver = webdriver.Chrome(options=options)

        elif browser == "edge":

            options = EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")

            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                ),
                options=options
            )

        elif browser == "firefox":

            options = FirefoxOptions()

            if headless:
                options.add_argument("-headless")

            driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                ),
                options=options
            )

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        if not headless:
            driver.maximize_window()

        driver.implicitly_wait(IMPLICIT_WAIT)

        logger.info("WebDriver started successfully.")
        logger.info("=" * 60)

        return driver