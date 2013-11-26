import redis

from datetime import datetime

from coffee.config import app_config


class Status (object):

    def __init__(self):
        self.redis = redis.Redis(
            host=app_config['REDIS_HOST'],
            port=app_config['REDIS_PORT'],
            db=app_config['REDIS_DB'],
            password=app_config['REDIS_PW']
        )
        previous = self.redis.hgetall('coffeestatus')
        try:
            self.current_status = previous['status'] == 'True'
            self.last_start = previous['last_start']
        except:
            self.current_status = False
            self.last_start = '1977-11-21 12:00'

    def save(self):
        self.redis.hmset('coffeestatus', self.to_dict())

    def get(self):
        previous = self.redis.hgetall('coffeestatus')
        self.current_status = previous['status'] == 'True'
        self.last_start = previous['last_start']

    def to_dict(self):
        return {
            'status': self.current_status,
            'last_start': self.last_start
        }

    def calculate_last_start(self, status):
        if status and datetime.now() > datetime.strptime(self.last_start, '%Y-%m-%d %H:%M'):
            return datetime.now().strftime('%Y-%m-%d %H:%M')
        else:
            return self.last_start

    def update(self, new_status):
        if not self.current_status == new_status:
            self.current_status = new_status
            self.last_start = self.calculate_last_start()
            self.save()
            self.log_status(new_status)

    def log_status(self, status):
        if status:
            self.redis.hincrby('coffeestats', datetime.now().strftime('%Y-%m-%d'), 1)
