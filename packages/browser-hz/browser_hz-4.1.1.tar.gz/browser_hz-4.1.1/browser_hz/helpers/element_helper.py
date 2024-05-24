from logging import Logger, getLogger
from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from browser_hz.helpers.wait_helper import WaitHelper

LOGGER: Logger = getLogger(__name__)


class ElementHelper:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait_helper: WaitHelper = WaitHelper(driver)

    def click(self, locator: Tuple[str, str]) -> None:
        LOGGER.info(f'Click element with locator [{locator}]')
        self._wait_helper.wait_for_element_to_be_clickable(locator=locator)
        element_to_be_clicked: WebElement = self._driver.find_element(by=locator[0], value=locator[1])
        element_to_be_clicked.click()
