from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WaitHelper:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def wait_for_element_to_be_clickable(self, locator: Tuple[str, str]) -> None:
        wait: WebDriverWait = WebDriverWait(self._driver, timeout=5)
        wait.until(expected_conditions.element_to_be_clickable(locator))
