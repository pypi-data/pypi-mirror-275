import re
from logging import Logger, getLogger

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from seleniumwire.inspect import InspectRequestsMixin
from seleniumwire.thirdparty.mitmproxy.net.http import Request

LOGGER: Logger = getLogger(__name__)


class NetworkHelper:

    def __init__(self, driver: WebDriver | InspectRequestsMixin):
        self._driver = driver

    def get_network_traffic(self, requests_paths_to_wait: list[str], timeout: int = 1) -> list[Request]:
        requests: list[Request] = []
        for request_path_to_wait in requests_paths_to_wait:
            try:
                requests.append(self._driver.wait_for_request(pat=re.escape(request_path_to_wait), timeout=timeout))
            except TimeoutException:
                requests.append(self.__get_unsuccessfully_processed_request(request_path_to_wait))
        return requests

    def __get_unsuccessfully_processed_request(self, request_path_to_wait: str) -> Request:
        if request := [request for request in self._driver.requests if request_path_to_wait in request.url]:
            return request[0]
        raise NoSuchElementException(f'Request with path matching {request_path_to_wait} has not been sent')

    @staticmethod
    def get_request_with_path(requests: list[Request], path: str) -> Request | None:
        for request in requests:
            if re.search(re.escape(path), request.url):
                return request
        return None
