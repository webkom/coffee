import logging
import requests

logger = logging.getLogger(__name__)


class Integration:
    """Base integration class for default behaviour of integrations"""
    def notify(self):
        pass


class DummyIntegration(Integration):
    """Example integration"""
    def notify(self):
        print("I was notified")


class NotiwireIntegration(Integration):
    """Integration against Online Notiwire"""

    API_URL = 'https://passoa.online.ntnu.no/notipi/abakus/coffee'
    headers = {
        'User-Agent': 'Abakus Coffee'
    }

    def __init__(self, api_key):
        self.api_key = api_key

    def notify(self):
        try:
            r = requests.post(
                self.API_URL, data={'api_key': self.api_key},
                headers=self.headers, timeout=5
            )
            if r.status_code != 200:
                logger.warning('Notiwire returned error: ' + r.text)

        except requests.exceptions.RequestException as e:
            logger.warning('Exception occured when sending POST request to notiwire: ' + str(e))
