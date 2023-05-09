import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import datetime
logger = logging.getLogger(__name__)

def impl_generate_baselines():
    base_url, headers=get_environment()
    payload = {"num_days": 5, "model_name": "WeekDay Profile"}
    full_url = base_url + "/api/baselines/exec-generate-baselines/"
    result = requests.post(full_url, json=payload, headers=headers)
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    print("\nResult", result.status_code, full_url)
    logger.info("Generating baselines")

def generate_baselines():
    thread = Thread(target=impl_generate_baselines)
    thread.start()