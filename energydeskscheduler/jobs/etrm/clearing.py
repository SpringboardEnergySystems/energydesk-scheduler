import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_download_clearing_reports():
    base_url, headers=get_environment()
    payload = {}
    full_url = base_url + "/api/clearing/download-clearing-reports/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Downloading clearing reports")

def download_clearing_reports():
    thread = Thread(target=impl_download_clearing_reports)
    thread.start()

def impl_perform_reconciliation():
    base_url, headers=get_environment()
    date_today = (datetime.date.today()).strftime("%Y-%m-%d")
    payload = {"date": date_today}
    full_url = base_url + "/api/clearing/perform-reconciliation/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Reconciling trades")

def perform_reconciliation():
    thread = Thread(target=impl_perform_reconciliation)
    thread.start()