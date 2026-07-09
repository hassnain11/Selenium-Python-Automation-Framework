from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config.config import IMPLICIT_WAIT


class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome", headless=False):

        browser = browser.lower()

        if browser == "chrome":

            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                ),
                options=options
            )

        elif browser == "edge":

            options = EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

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
            raise Exception(f"Unsupported browser: {browser}")

        driver.maximize_window()

        driver.implicitly_wait(IMPLICIT_WAIT)

        return driver