# runapscheduler.py
import logging
from energydeskapi.sdk.common_utils import load_env
from energydeskapi.sdk.api_connection import ApiConnection
from energydeskapi.scheduler.scheduler_api import SchedulerApi
import environ
from os.path import join, dirname
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from miscutils.logutils import setup_service_logging

environ.Env.read_env()
setup_service_logging("energydesk-scheduler")
logger = logging.getLogger(__name__)

def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)

def setup_job(scheduler,crontab, python_module, functon_name, arguments=[]):
    logger.info("Scheduling " + python_module + "/" + functon_name + "(" + crontab + ")")
    job_function = import_from(python_module, functon_name)
    scheduler.add_job(
        job_function,
        trigger=CronTrigger.from_crontab(crontab),  # Every 10 seconds
        id=python_module + "_" + functon_name,
        args=arguments,
        max_instances=1,
        replace_existing=True,
    )

def load_schedules(api_conn, scheduler):
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    api_conn = ApiConnection(url)
    api_conn.set_token(tok, "Token")
    df=SchedulerApi.get_scheduled_jobs_embedded_df(api_conn)
    print(df)
    for index, row in df.iterrows():
        setup_job(scheduler, row['crontab'], row['job_definition']['python_module'], row['job_definition']['func_name'])

def startup_scheduler(api_conn):
    scheduler = BlockingScheduler()
    # Add schedules, configure tasks here
    load_schedules(api_conn, scheduler)
    scheduler.start()

if __name__ == '__main__':
    load_env(dirname(__file__))
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    api_conn = ApiConnection(url)
    api_conn.set_token(tok, "Token")
    startup_scheduler(api_conn)


