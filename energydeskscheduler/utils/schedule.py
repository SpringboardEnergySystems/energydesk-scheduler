import logging
from energydeskapi.sdk.common_utils import load_env
from energydeskapi.sdk.api_connection import ApiConnection
from energydeskapi.scheduler.scheduler_api import SchedulerApi
import environ
import requests
logger = logging.getLogger(__name__)

def log_jobstart(name):
    logger.info("Sending job start signal for job " + str(name))
    #SchedulerApi.upsert_jobsexecution()

def log_jobend(name):
    logger.info("Sending job end signal for job " + str(name))
    #SchedulerApi.upsert_jobsexecution()