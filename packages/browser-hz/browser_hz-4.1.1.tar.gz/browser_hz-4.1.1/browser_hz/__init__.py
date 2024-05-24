from contextlib import contextmanager
from logging import Logger, getLogger
from typing import Generator

from browser_hz.browser import Browser
from browser_hz.browser_factory import create_browser
from browser_hz.browsers import Browsers

LOGGER: Logger = getLogger(__name__)


@contextmanager
def open_browser(web_browser: Browsers) -> Generator[Browser, None, None]:
    browser_: Browser | None = None
    try:
        LOGGER.info(f'Open web browser [{web_browser}]')
        browser_ = create_browser(web_browser)
        yield browser_
    finally:
        browser_.close_tab()
        browser_.close_browser()
