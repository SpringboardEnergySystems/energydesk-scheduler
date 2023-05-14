import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_update_ticker(token=None):
    base_url, headers = get_environment(token)
    payload = {}
    full_url = base_url + "/api/energydeskscheduler/update-ticker/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Updating ticker")

def update_ticker(token=None):
    thread = Thread(target=impl_update_ticker, args=[token])
    thread.start()

def impl_update_energydesk_cache(token=None):
    base_url, headers = get_environment(token)
    payload={}
    full_url = base_url + "/api/energydeskscheduler/update-cache/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Updating energydeskscheduler cache")
def update_energydesk_cache(token=None):
    thread = Thread(target=impl_update_energydesk_cache, args=[token])
    thread.start()
