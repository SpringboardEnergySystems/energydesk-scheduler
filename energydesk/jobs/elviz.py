import logging
from energydeskapi.sdk.common_utils import init_api
from energydeskapi.conversions.elvizlink_api import ElvizLinksApi
from energydeskapi.sdk.money_utils import FormattedMoney
from energydeskapi.contracts.contracts_api import Contract as ApiContract, ContractTag, ContractsApi
from energydeskapi.marketdata.products_api import ProductsApi
from energydeskapi.types.company_enum_types import CompanyTypeEnum, CompanyRoleEnum
from energydeskapi.types.market_enum_types import MarketEnum, InstrumentTypeEnum
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
    elviz_trades = ElvizLinksApi.get_latest_elviz_trades(api_conn)
    contracts = []
    for t in elviz_trades:
        success, json_res, status_code, error_msg = ProductsApi.generate_market_product_from_ticker(api_conn,
                                                                                                    "Nordic Power",
                                                                                                    t['commodity'][
                                                                                                        'product_code'])
        if success:
            print(json_res)
            market_product_key = json_res[0]['pk']
        print(t)

        contract_obj = ApiContract.from_simple_dict(t)
        print(contract_obj.get_dict(api_conn))
        contracts.append(contract_obj)
    print(contracts)
    full_url = proxy_url + "/api/elviztrades"
    print("\nResult", full_url)
    logger.info("Loading Elviz trades")
