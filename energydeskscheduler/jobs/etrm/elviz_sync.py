import logging
from energydeskapi.conversions.elvizlink_api import ElvizLinksApi
from energydeskapi.contracts.contracts_api import Contract as ApiContract, ContractTag, ContractsApi
from energydeskapi.marketdata.products_api import ProductsApi
from energydeskapi.sdk.api_connection import ApiConnection
import logging
from energydeskscheduler.utils.misc import get_environment
import requests
from energydeskscheduler.utils.schedule import log_jobstart, log_jobend
from time import sleep
from threading import Thread
import requests
import environ
logger = logging.getLogger(__name__)

def impl_load_elviz_trades(token=None):
    env = environ.Env()
    base_url = env.str('ENERGYDESK_URL')
    payload = {}
    api_conn = ApiConnection(base_url)
    if token==None:
        token = env.str('ENERGYDESK_TOKEN')
        api_conn.set_token(token, "Token")
    else:
        api_conn.set_token(token, "Bearer")

    elviz_trades = ElvizLinksApi.get_latest_elviz_trades(api_conn, 1)
    contracts = []
    for t in elviz_trades:
        contract_obj = ApiContract.from_simple_dict(t)
        contracts.append(contract_obj)

    print("Loaded ", len(contracts), " contracts from Elviz")
    ContractsApi.bulk_insert_contracts(api_conn, contracts)

def load_elviz_trades(token=None):
    thread = Thread(target=impl_load_elviz_trades, args=[token])
    thread.start()