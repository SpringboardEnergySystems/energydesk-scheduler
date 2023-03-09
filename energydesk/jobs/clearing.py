import logging
from energydeskapi.sdk.common_utils import load_env
from energydeskapi.sdk.api_connection import ApiConnection
from energydeskapi.scheduler.scheduler_api import SchedulerApi
import environ
import requests
import datetime
logger = logging.getLogger(__name__)

def download_clearing_reports():
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    headers = {'Authorization': "token" + ' ' + tok}
    payload = {}
    full_url = url + "/api/clearing/download-clearing-reports/"
    result = requests.post(full_url, json=payload, headers=headers)
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    print("\nResult", result.status_code, full_url)
    logger.info("Downloading clearing reports")

def perform_reconciliation():
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    headers = {'Authorization': "token" + ' ' + tok}
    date_today = (datetime.date.today()).strftime("%Y-%m-%d")
    payload = {"date": date_today}
    full_url = url + "/api/clearing/perform-reconciliation/"
    result = requests.post(full_url, json=payload, headers=headers)
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    print("\nResult", result.status_code, full_url)
    logger.info("Reconciling trades")
