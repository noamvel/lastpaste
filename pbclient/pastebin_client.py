import sys
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from abc import abstractmethod
import logging


class PastebinClient:

    __pb_home_url = 'https://pastebin.com'
    __timeout = 2
    __retries = 3
    __backoff_factor = 3
    __status_forcelist = (500, 502, 504)
    retry_policy = Retry(
        total=__retries,
        read=__retries,
        connect=__retries,
        backoff_factor=__backoff_factor,
        status_forcelist=__status_forcelist,
    )

    def __init__(self, relative_path=None):
        self.url = PastebinClient.__pb_home_url + relative_path
        self.adapter = HTTPAdapter(max_retries=PastebinClient.retry_policy)

    def get(self):
        session = requests.Session()
        session.mount(self.url, self.adapter)
        try:
            response = session.get(self.url, timeout=PastebinClient.__timeout)
            response.raise_for_status()
        except Exception as e:
            return self.handle_exception(e)
        return response.text

    @abstractmethod
    def handle_exception(self, exception):
        pass

    @classmethod
    def set_retries(cls, retries):
        cls.__retries = retries

    @classmethod
    def set_timeout(cls, timeout):
        cls.__timeout = timeout

    @classmethod
    def set_backoff_factor(cls, backoff_factor):
        cls.__backoff_factor = backoff_factor


class PastebinArchiveClient(PastebinClient):

    def __init__(self):
        super().__init__('/archive')

    def handle_exception(self, e):
        logging.error("'Archive page currently unavailable.\n {}\nExiting ...'".format(e))
        sys.exit(1)


class PastebinSinglePasteClient(PastebinClient):
    # 'Single paste' page doesn't change, unlike 'Archive' page -> increase backoff_factor
    __backoff_factor = 30

    def __init__(self, href):
        super().__init__(href)

    def handle_exception(self, e):
        logging.error("'Paste page currently unavailable.\n {}\nSkipping ...'".format(e))
        return None











