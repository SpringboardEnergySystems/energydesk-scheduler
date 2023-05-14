
import logging
import environ
from energydeskscheduler.utils.logutils import setup_service_logging
from energydeskapi.sdk.api_connection import ApiConnection

environ.Env.read_env()
setup_service_logging("energydeskscheduler-scheduler")
logger = logging.getLogger(__name__)

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)


# Used by Portal to execute a job right away instead of waiting for the scheduler
def run_job(token, python_module, functon_name, arguments=[]):
    logger.info("Exec " + python_module + "/" + functon_name)
    env = environ.Env()
    base_url = env.str('ENERGYDESK_URL')
    api_conn = ApiConnection(base_url)
    if token==None:
        token = env.str('ENERGYDESK_TOKEN')
        api_conn.set_token(token, "Token")
    else:
        api_conn.set_token(token, "Bearer")
    job_function = import_from(python_module, functon_name)
    job_function(api_conn)
