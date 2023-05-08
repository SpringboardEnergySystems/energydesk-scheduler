# runapscheduler.py
import logging
from energydeskapi.sdk.common_utils import load_env
from energydeskapi.sdk.api_connection import ApiConnection
from energydeskapi.scheduler.scheduler_api import SchedulerApi, ScheduledJobExecution
import environ
from os.path import join, dirname
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, JobExecutionEvent
from apscheduler.triggers.cron import CronTrigger
from miscutils.logutils import setup_service_logging
import datetime
import inspect

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

def scheduler_listener(event):
    # env = environ.Env()
    # tok = env.str('ENERGYDESK_TOKEN')
    # url = env.str('ENERGYDESK_URL')
    # api_conn = ApiConnection(url)
    # api_conn.set_token(tok, "Token")
    #
    # jobidspl = event.job_id.split(".")
    # jobid = jobidspl[len(jobidspl) - 1]
    # job = jobid.split("_")
    # func_name = ""
    # for i in range(0, len(job)):
    #     if i == 0:
    #         continue
    #     if i == len(job) - 1:
    #         func_name += job[i]
    #     else:
    #         func_name += job[i] + "_"
    # print(func_name)
    # job_definition = SchedulerApi.get_job_definitions(api_conn, {'func_name': func_name})
    # job_definition_url = SchedulerApi.get_job_definition_url(api_conn, job_definition[0]['pk'])
    # log_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None).isoformat() + 'Z'
    # print(job_definition_url)
    # print(log_time)


    #job_exec = ScheduledJobExecution()
    #job_exec.job = job_definition_url
    #job_exec.logtime = log_time
    #job_exec.message = event.job_id
    #job_exec.taskdone = True
    #job_exec.success = True
#
    #SchedulerApi.upload_scheduled_job_execution(api_conn, job_exec)

    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')
    return event.retval

def startup_scheduler(api_conn):
    scheduler = BlockingScheduler()
    # Add schedules, configure tasks here
    load_schedules(api_conn, scheduler)
    scheduler.add_listener(scheduler_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()

if __name__ == '__main__':
    load_env(dirname(__file__))
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    api_conn = ApiConnection(url)
    api_conn.set_token(tok, "Token")
    startup_scheduler(api_conn)


