from datetime import datetime, timedelta

import dateutil.parser
import redis

from coffee.config import app_config, integrations


class Status (object):

    def __init__(self):
        self.integrations = integrations

        self.redis = redis.Redis(
            host=app_config['REDIS_HOST'],
            port=app_config['REDIS_PORT'],
            password=app_config['REDIS_PW'],
            charset='utf-8',
            decode_responses=True
        )
        try:
            self.get()
        except:
            self.current_status = False
            self.last_start = datetime(1977, 11, 21, 12, 0)
            span = datetime.utcnow() - self.last_start
            self.hours_since = (span.days * 24) + (span.seconds // 3600)
            self.minutes_since = (span.seconds//60) % 60

    def save(self):
        self.redis.hmset('coffeestatus', self.to_dict())

    def get(self):
        previous = self.redis.hgetall('coffeestatus')
        self.current_status = previous['status'] == 'True'
        self.last_start = dateutil.parser.parse(previous['last_start'])
        span = datetime.utcnow() - self.last_start
        self.hours_since = (span.days*24)+(span.seconds//3600)
        self.minutes_since = (span.seconds//60) % 60

    def to_dict(self):
        return {
            'status': self.current_status,
            'last_start': self.last_start.isoformat(),
            'time_since': {
                'hours': self.hours_since,
                'minutes': self.minutes_since
            }
        }

    def calculate_last_start(self, status):
        if status and datetime.utcnow() > self.last_start:
            return datetime.utcnow()
        else:
            return self.last_start

    def update(self, new_status):
        if self.current_status == new_status:
            return
        self.current_status = new_status
        if self.last_start + timedelta(seconds=40) < datetime.utcnow():
            self.log_status(new_status)
            self.notify_integrations()
        self.last_start = self.calculate_last_start(new_status)
        self.save()

    def notify_integrations(self):
        for integration in self.integrations:
            integration.notify()

    def log_status(self, status):
        if status:
            self.redis.hincrby('coffeestats', datetime.utcnow().strftime('%Y-%m-%d'), 1)

    def get_count(self, date):
        return self.redis.hget('coffeestats', date.strftime('%Y-%m-%d')) or 0

    def get_stats(self):
        return self.redis.hgetall('coffeestats')
