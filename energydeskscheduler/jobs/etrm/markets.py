import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
logger = logging.getLogger(__name__)


def impl_download_spotdata(api_conn):
    log_jobstart("download_spotdata")
    base_url=api_conn.get_base_url()
    headers=api_conn.get_authorization_header()
    payload = {}
    full_url = base_url + "/api/markets/download-spotdata/"
    result = requests.post(full_url, json=payload, headers=headers)
    logger.info("\nResult " + str(result.status_code) + str(full_url))
    logger.info("Downloading spotdata")
    log_jobend("download_spotdata")

def download_spotdata(api_conn):
    thread = Thread(target=impl_download_spotdata, args=[token])
    thread.start()

def impl_download_nasdaqdata(api_conn):
    base_url=api_conn.get_base_url()
    headers=api_conn.get_authorization_header()
    payload = {}
    full_url = base_url + "/api/markets/download-nasdaqdata/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Downloading nasdaqdata")

def download_nasdaqdata(api_conn):
    thread = Thread(target=impl_download_nasdaqdata, args=[api_conn])
    thread.start()