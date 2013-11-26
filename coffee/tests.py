import unittest
import json
from datetime import datetime

from coffee import server
from coffee.models import Status


class TestViews(unittest.TestCase):

    EXAMPLE_STATUS = {
        "status": True,
        "last_start": datetime.now().strftime('%Y-%m-%d %H:%M'),
    }
    UNKNOWN_STATUS = {
        "status": "unknown"
    }

    def setUp(self):
        self.app = server.app.test_client()
        self.status = Status()
        self.redis = self.status.redis
        self.redis.hmset('coffeestatus', self.EXAMPLE_STATUS)
        self.redis.hmset('coffeestats', {datetime.now().strftime('%Y-%m-%d'): 1})

    def tearDown(self):
        pass

    def assertStatusCode(self, response, expected):
        self.assertEquals(response._status_code, expected)

    def test_index(self):
        response = self.app.get('/')
        self.assertStatusCode(response, 200)

    def test_status(self):
        response = self.app.get('/api/status')
        self.assertStatusCode(response, 200)
        self.assertEquals(
            json.loads(response.data)['coffee'],
            self.EXAMPLE_STATUS
        )

    def test_stats(self):
        response = self.app.get('/api/stats')
        self.assertStatusCode(response, 200)
        self.assertEquals(
            json.loads(response.data)['stats'],
            {
                datetime.now().strftime('%Y-%m-%d'): '1'
            }
        )

    def test_no_status(self):
        self.redis.hdel('coffeestatus', 'status')
        self.redis.hdel('coffeestatus', 'last_start')
        response = self.app.get('/api/status')
        self.assertStatusCode(response, 200)
        self.assertEquals(
            json.loads(response.data)['coffee'],
            self.UNKNOWN_STATUS
        )

    def test_coffeetxt(self):
        response = self.app.get('/coffee.txt')
        self.assertStatusCode(response, 200)
        self.assertEqual(response.data, '1\n%s' % datetime.now().strftime('%d. %B %Y %H:%M:00'))


if __name__ == '__main__':
        unittest.main()
