import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_update_ticker(api_conn):
    base_url=api_conn.get_base_url()
    headers=api_conn.get_authorization_header()
    payload = {}
    full_url = base_url + "/api/energydeskscheduler/update-ticker/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Updating ticker")

def update_ticker(api_conn):
    thread = Thread(target=impl_update_ticker, args=[api_conn])
    thread.start()

def impl_update_energydesk_cache(api_conn):
    base_url=api_conn.get_base_url()
    headers=api_conn.get_authorization_header()
    payload={}
    full_url = base_url + "/api/energydeskscheduler/update-cache/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Updating energydeskscheduler cache")
def update_energydesk_cache(api_conn):
    thread = Thread(target=impl_update_energydesk_cache, args=[api_conn])
    thread.start()

def backup_database(api_conn):
    base_url = api_conn.get_base_url()
    headers = api_conn.get_authorization_header()
    payload = {}
    full_url = base_url + "/api/energydesk/backup-database/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Backing up Energydesk database")
