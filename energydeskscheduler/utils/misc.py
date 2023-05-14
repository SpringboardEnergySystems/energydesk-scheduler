import logging
import environ

logger = logging.getLogger(__name__)
def get_environment(token=None):
    env = environ.Env()
    url = env.str('ENERGYDESK_URL')
    if token is None:
        token = env.str('ENERGYDESK_TOKEN')
        headers = {'Authorization': "token" + ' ' + token}
    else:
        headers = {'Authorization': "Bearer" + ' ' + token}

    return url, headers