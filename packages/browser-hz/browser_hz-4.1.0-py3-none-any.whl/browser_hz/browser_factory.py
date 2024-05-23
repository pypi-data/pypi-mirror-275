from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from .browser import Browser
from .browser_options import get_chrome_options
from .browsers import Browsers


def create_browser(browser: Browsers = Browsers.CHROME) -> Browser:
    match browser:
        case Browsers.CHROME:
            return init_chrome_browser()
        case _:
            raise ValueError(f"'{browser}' is not supported")


def init_chrome_browser() -> Browser:
    ChromeDriverManager().install()
    driver = webdriver.Chrome(options=get_chrome_options())
    driver.maximize_window()
    return Browser(driver=driver)
