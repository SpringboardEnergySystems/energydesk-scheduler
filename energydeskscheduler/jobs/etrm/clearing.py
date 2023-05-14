import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_download_clearing_reports(api_conn):
    base_url=api_conn.get_base_url()
    headers=api_conn.get_authorization_header()
    payload = {}
    full_url = base_url + "/api/clearing/download-clearing-reports/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Downloading clearing reports")

def download_clearing_reports(api_conn):
    thread = Thread(target=impl_download_clearing_reports, args=[api_conn])
    thread.start()

def impl_perform_reconciliation(api_conn):
    base_url=api_conn.get_base_url()
    headers=api_conn.get_authorization_header()
    date_today = (datetime.date.today()).strftime("%Y-%m-%d")
    payload = {"date": date_today}
    full_url = base_url + "/api/clearing/perform-reconciliation/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Reconciling trades")

def perform_reconciliation(api_conn):
    thread = Thread(target=impl_perform_reconciliation, args=[api_conn])
    thread.start()