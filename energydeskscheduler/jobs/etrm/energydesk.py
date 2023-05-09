import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_update_ticker():
    base_url, headers = get_environment()
    payload = {}
    full_url = base_url + "/api/energydeskscheduler/update-ticker/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Updating ticker")

def update_ticker():
    thread = Thread(target=impl_update_ticker)
    thread.start()

def impl_update_energydesk_cache():
    base_url, headers = get_environment()
    payload={}
    full_url = base_url + "/api/energydeskscheduler/update-cache/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Updating energydeskscheduler cache")
def update_energydesk_cache():
    thread = Thread(target=impl_update_energydesk_cache)
    thread.start()
