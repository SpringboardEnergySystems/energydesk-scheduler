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
        contract = ApiContract()
        contract.external_contract_id = t['external_contract_id']
        contract.trade_date = t['trade_date']
        contract.trade_datetime = t['trade_time']
        contract.trading_book = t['trading_book']
        contract.trader = t['trader']
        contract.contract_price = FormattedMoney(t['contract_price']['amount'], t['contract_price']['currency'])
        contract.quantity = t['quantity']
        contract.trading_fee = FormattedMoney(t['trading_fee']['amount'], t['trading_fee']['currency'])
        contract.clearing_fee = FormattedMoney(t['clearing_fee']['amount'], t['clearing_fee']['currency'])
        contract.commodity_type = t['commodity']['commodity_type']
        contract.instrument_type = InstrumentTypeEnum(t['commodity']['instrument_type'])
        contract.contract_status = t['contract_status']
        contract.buy_or_sell = t['buy_or_sell']
        contract.counterpart = t['counterpart']
        contract.market = MarketEnum(t['commodity']['market'])
        contract.marketplace_product = market_product_key
        contract.contract_status = t['contract_status']
        contract.commodity_profile = t['commodity']['commodity_profile']
        contract.delivery_type = t['commodity']['delivery_type']
        contract.commodity_delivery_from = t['commodity']['delivery_from']
        contract.commodity_delivery_until = t['commodity']['delivery_until']
        contract.product_code = t['commodity']['product_code']
        contract.contract_tags = t['contract_tags']
        print(contract.get_dict(api_conn))
        contracts.append(contract)
    print(contracts)
    full_url = proxy_url + "/api/elviztrades"
    print("\nResult", full_url)
    logger.info("Loading Elviz trades")
