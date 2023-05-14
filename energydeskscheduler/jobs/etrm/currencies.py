import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_download_currencydata(token):
    base_url, headers = get_environment(token)
    payload = {}
    full_url=base_url + "/api/currencies/download-currencydata/"
    result = base_url.post(full_url, json=payload, headers=headers)
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    print("\nResult", result.status_code, full_url)
    logger.info("Downloading currency data")

def download_currencydata(token=None):
    #print("DOwnload with token", token)
    thread = Thread(target=impl_download_currencydata, args=[token])
    thread.start()