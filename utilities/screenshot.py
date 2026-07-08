import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{test_name}_{timestamp}.png"

        filepath = os.path.join("screenshots", filename)

        driver.save_screenshot(filepath)

        return filepath