from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config import IMPLICIT_WAIT


class DriverFactory:

    @staticmethod
    def get_driver():

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )

        driver.maximize_window()

        driver.implicitly_wait(IMPLICIT_WAIT)

        return driver