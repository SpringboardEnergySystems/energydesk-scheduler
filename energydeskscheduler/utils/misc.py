import logging
import environ

logger = logging.getLogger(__name__)
def get_environment():
    env = environ.Env()
    tok = env.str('ENERGYDESK_TOKEN')
    url = env.str('ENERGYDESK_URL')
    headers = {'Authorization': "token" + ' ' + tok}
    return url, headers