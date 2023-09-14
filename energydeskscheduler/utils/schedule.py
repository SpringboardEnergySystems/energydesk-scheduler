import logging

logger = logging.getLogger(__name__)

def log_jobstart(name):
    logger.info("Sending job start signal for job " + str(name))
    #SchedulerApi.upsert_jobsexecution()

def log_jobend(name):
    logger.info("Sending job end signal for job " + str(name))
    #SchedulerApi.upsert_jobsexecution()