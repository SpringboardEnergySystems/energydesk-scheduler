import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_check_for_unavailability(api_conn):
    base_url=api_conn.get_base_url()
    headers=api_conn.get_authorization_header()
    payload = {}
    full_url = base_url + "/api/fundamentals/check-for-unavailability/"
    result = requests.post(full_url, json=payload, headers=headers)
    print("\nResult", result.status_code, full_url)
    logger.info("Checking for unavailability")

def check_for_unavailability(api_conn):
    thread = Thread(target=impl_check_for_unavailability, args=[api_conn])
    thread.start()