import logging
from energydeskapi.sdk.common_utils import load_env
from energydeskapi.sdk.api_connection import ApiConnection
from energydeskapi.scheduler.scheduler_api import SchedulerApi
import environ
import requests
logger = logging.getLogger(__name__)

def download_spotdata():
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    headers = {'Authorization': "token" + ' ' + tok}
    payload = {}
    result = requests.post(url + "/api/markets/download-spotdata/", json=payload, headers=headers)
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    print(result.text)
    logger.info("Downloading spotdata")

def download_nasdaqdata():
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    headers = {'Authorization': "token" + ' ' + tok}
    payload = {}
    result = requests.post(url + "/api/markets/download-nasdaqdata/", json=payload, headers=headers)
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    print(result.text)
    logger.info("Downloading nasdaqdata")