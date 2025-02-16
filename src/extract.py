import requests
from dotenv import load_dotenv
import os

def extract(currency: str = "eur", date: str = "latest") -> dict:

    url = get_url(currency, date)

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception

    return response.json()


def get_url(currency, date):

    load_dotenv()

    url_template = os.getenv("URL_TEMPLATE")
    api_version = os.getenv("API_VERSION")

    url = url_template.format(date=date, api_version=api_version, endpoint=currency)

    return url