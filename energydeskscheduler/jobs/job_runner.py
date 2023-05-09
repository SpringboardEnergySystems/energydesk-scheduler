
import logging
import environ
from energydeskscheduler.utils.logutils import setup_service_logging


environ.Env.read_env()
setup_service_logging("energydeskscheduler-scheduler")
logger = logging.getLogger(__name__)

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)


# Used by Portal to execute a job right away instead of waiting for the scheduler
def run_job( python_module, functon_name, arguments=[]):
    logger.info("Exec " + python_module + "/" + functon_name )
    job_function = import_from(python_module, functon_name)
    job_function()
