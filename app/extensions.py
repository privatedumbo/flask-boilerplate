import requests
from flask_sqlalchemy import SQLAlchemy
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


db = SQLAlchemy()


def _requests_client() -> requests.Session:
    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["HEAD", "GET", "OPTIONS"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)
    return http


restclient = _requests_client()
