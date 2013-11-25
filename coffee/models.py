import redis

from datetime import datetime


class Status (object):

    def __init__(self, pool):
        self.redis = redis.Redis(connection_pool=pool)
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

    def get_last_start(self, status):
        if status and not datetime.now() > datetime.strptime(self.last_start, '%Y-%m-%d %H:%M'):
            return datetime.now().strftime('%Y-%m-%d %H:%M')
        else:
            return self.last_start

    def update(self, new_status):
        if not self.current_status == new_status:
            self.current_status = new_status
            self.last_start = self.calculate_last_start()
            self.save()
