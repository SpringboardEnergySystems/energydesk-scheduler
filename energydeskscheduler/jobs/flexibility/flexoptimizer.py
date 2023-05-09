import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_check_scheduled_dispatches():
    base_url, headers=get_environment()
    payload = {}
    full_url=base_url + "/api/flexoptimizer/exec-check-scheduled-dispatches/"
    # result = requests.post(full_url, json=payload, headers=headers)
    # # api_conn = ApiConnection(url)
    # # api_conn.set_token(tok, "Token")
    # print("\nResult", result.status_code, full_url)
    # logger.info("Checking scheduled dispatches")

def check_scheduled_dispatches():
    thread = Thread(target=impl_check_scheduled_dispatches)
    thread.start()

def impl_optimize_battery():
    base_url, headers=get_environment()
    payload = {}
    full_url=base_url + "/api/flexoptimizer/exec-optimize-battery/"
    # result = requests.post(full_url, json=payload, headers=headers)
    # # api_conn = ApiConnection(url)
    # # api_conn.set_token(tok, "Token")
    # print("\nResult", result.status_code, full_url)
    # logger.info("Optimizing battery")

def optimize_battery():
    thread = Thread(target=impl_optimize_battery)
    thread.start()