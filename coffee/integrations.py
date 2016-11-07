import requests


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
        requests.post(self.API_URL, data={'api_key': self.api_key}, headers=self.headers)
