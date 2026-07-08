import logging
import os


class Logger:

    @staticmethod
    def get_logger():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger("AutomationFramework")

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            file_handler = logging.FileHandler(
                "logs/automation.log",
                mode="a"
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger