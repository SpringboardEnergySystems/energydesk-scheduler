import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_download_forward_curve():
    base_url, headers = get_environment()
    payload = {}
    full_url = base_url + "/api/curvemanager/download-curvedata/"
    result = requests.post(full_url, json=payload, headers=headers)
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    print("\nResult", result.status_code, full_url)
    logger.info("Downloading spotdata")

def download_forward_curve():
    thread = Thread(target=impl_download_forward_curve)
    thread.start()
