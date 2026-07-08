import os


def take_screenshot(driver, file_path):
    """
    Saves a screenshot to the given file path.
    """

    directory = os.path.dirname(file_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    driver.save_screenshot(file_path)