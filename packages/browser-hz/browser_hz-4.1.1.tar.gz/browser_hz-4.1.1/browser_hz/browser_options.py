import os
import sys

from selenium.webdriver.chrome.options import Options
from seleniumwire.webdriver import ChromeOptions

USER_AGENT_ENV: str = "USER_AGENT_ENV"


def get_chrome_options(options: Options = ChromeOptions()) -> Options:
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--mute-audio')
    options.add_argument('--disable-site-isolation-trials')
    _set_user_agent(options=options)
    _set_headless_mode(options=options)
    return options


def _set_user_agent(options: Options) -> None:
    if user_agent_env := os.getenv(USER_AGENT_ENV):
        options.add_argument(f'--user-agent={user_agent_env}')


def _set_headless_mode(options: Options) -> None:
    if not _is_run_in_debug_mode():
        options.add_argument('--headless=new')


def _is_run_in_debug_mode() -> bool:
    """
    Return True if the test has been run in debug mode, otherwise return False.
    """
    return sys.gettrace() is not None
