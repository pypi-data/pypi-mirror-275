from contextlib import contextmanager
from logging import Logger, getLogger
from typing import Tuple, Generator

from selenium.webdriver.remote.webdriver import WebDriver
from seleniumwire.inspect import InspectRequestsMixin

from browser_hz.helpers.element_helper import ElementHelper
from browser_hz.helpers.network_helper import NetworkHelper
from browser_hz.helpers.wait_helper import WaitHelper

LOGGER: Logger = getLogger(__name__)


class Browser:

    def __init__(self, driver: WebDriver | InspectRequestsMixin):
        self._driver: WebDriver | InspectRequestsMixin = driver
        self._wait_helper: WaitHelper = WaitHelper(driver)
        self._element_helper: ElementHelper = ElementHelper(driver)
        self._network_helper: NetworkHelper = NetworkHelper(driver)

    def get_network_helpers(self) -> NetworkHelper:
        return self._network_helper

    def open_page(self, url: str) -> 'Browser':
        LOGGER.info(f'Open page [{url}]')
        self._driver.get(url)
        return self

    @contextmanager
    def click_with_redirect_to_new_tab(self, locator: Tuple[str, str]) -> Generator['Browser', None, None]:
        try:
            self._element_helper.click(locator)
            yield self
        finally:
            self.close_newly_opened_tab()

    def close_tab(self) -> 'Browser':
        LOGGER.info('Close tab')
        self._driver.close()
        return self

    def close_browser(self) -> 'Browser':
        LOGGER.info('Close web browser_hz')
        self._driver.quit()
        return self

    def close_newly_opened_tab(self) -> 'Browser':
        window_handles: list[str] = self._driver.window_handles
        if len(window_handles) == 2:
            self._driver.switch_to.window(window_handles[1])
            self.close_tab()
            self._driver.switch_to.window(window_handles[0])
        return self
