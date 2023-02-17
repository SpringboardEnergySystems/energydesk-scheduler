import logging
from energydeskapi.sdk.common_utils import load_env
from energydeskapi.sdk.api_connection import ApiConnection
from energydeskapi.scheduler.scheduler_api import SchedulerApi
import environ
import requests
logger = logging.getLogger(__name__)

def update_ticker():
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    headers = {'Authorization': "token" + ' ' + tok}
    payload = {}
    full_url = url + "/api/energydesk/update-ticker/"
    result = requests.post(full_url, json=payload, headers=headers)
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    print("\nResult", result.status_code, full_url)
    logger.info("Updating ticker")

def update_energydesk_cache():
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    headers={'Authorization':  "token" + ' ' + tok}
    payload={}
    full_url = url + "/api/energydesk/update-cache/"
    result = requests.post(full_url, json=payload, headers=headers)
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    print("\nResult", result.status_code, full_url)
    logger.info("Updating energydesk cache")
