import logging
from energydeskapi.conversions.elvizlink_api import ElvizLinksApi
from energydeskapi.contracts.contracts_api import Contract as ApiContract, ContractTag, ContractsApi
from energydeskapi.marketdata.products_api import ProductsApi
from energydeskapi.sdk.api_connection import ApiConnection
from os.path import join, dirname
import environ
import requests
logger = logging.getLogger(__name__)

def load_elviz_trades():
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    proxy_url = env.str('ELVIZ_PROXY')
    headers = {'Authorization': "token" + ' ' + tok}
    payload = {}
    api_conn = ApiConnection(url)
    api_conn.set_token(tok, "Token")
    elviz_trades = ElvizLinksApi.get_latest_elviz_trades(api_conn, 1)
    contracts = []
    for t in elviz_trades:
        # success, json_res, status_code, error_msg = ProductsApi.generate_market_product_from_ticker(api_conn,
        #                                                                                             "Nordic Power",
        #                                                                                             t['commodity'][
        #                                                                                                 'product_code'])
        contract_obj = ApiContract.from_simple_dict(t)
        contracts.append(contract_obj)

    print("Loaded ", len(contracts), " contracts from Elviz")
    ContractsApi.bulk_insert_contracts(api_conn, contracts)
