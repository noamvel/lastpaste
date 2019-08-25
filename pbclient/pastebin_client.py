import sys
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from abc import ABC, abstractmethod
import logging


class PastebinClient:

    pb_home_url = 'https://pastebin.com'
    timeout = 1
    retries = 3
    backoff_factor = 0.8
    status_forcelist = (500, 502, 504)
    retry_policy = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )

    def __init__(self, relative_path=None):
        self.url = PastebinClient.pb_home_url + relative_path
        self.adapter = HTTPAdapter(max_retries=PastebinClient.retry_policy)

    def get(self):
        session = requests.Session()
        session.mount(self.url, self.adapter)
        try:
            response = session.get(self.url, timeout=PastebinClient.timeout)
            response.raise_for_status()
        except Exception as e:
            self.handle_exception(e)
        return response.text

    @abstractmethod
    def handle_exception(self, exception):
        pass

    @classmethod
    def set_retries(cls, retries):
        cls.retries = retries

    @classmethod
    def set_timeout(cls, timeout):
        cls.timeout = timeout

    @classmethod
    def set_backoff_factor(cls, backoff_factor):
        cls.backoff_factor = backoff_factor


class PastebinArchiveClient(PastebinClient):

    def __init__(self):
        super().__init__('/archive')

    def handle_exception(self, exception):
        logging.error("'Archive page currently unavailable.\n {}\nExiting ...'".format(exception))
        sys.exit(1)


class PastebinSinglePasteClient(PastebinClient):

    def __init__(self, href):
        super().__init__(href)

    def handle_exception(self, exception):
        logging.error("'Paste page currently unavailable.\n {}\nSkipping ...'".format(exception))
        return None











