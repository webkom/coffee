import json
import unittest
from datetime import datetime

from coffee import server
from coffee.models import Status


class TestViews(unittest.TestCase):

    NOW = datetime.utcnow().isoformat()

    EXAMPLE_STATUS = {
        "status": True,
        "last_start": NOW,
    }

    EXAMPLE_OUTPUT = {
        "status": True,
        "last_start": NOW,
        "time_since": {
            "hours": 0,
            "minutes": 0
        }
    }

    UNKNOWN_STATUS = {
        "status": "unknown"
    }

    def setUp(self):
        self.app = server.app.test_client()
        self.status = Status()
        self.redis = self.status.redis
        self.redis.hmset('coffeestatus', self.EXAMPLE_STATUS)
        self.redis.hmset('coffeestats', {datetime.utcnow().strftime('%Y-%m-%d'): 1})

    def tearDown(self):
        pass

    def assertStatusCode(self, response, expected):
        self.assertEqual(response._status_code, expected)

    def test_index(self):
        response = self.app.get('/')
        self.assertStatusCode(response, 200)

    def test_status(self):
        response = self.app.get('/api/status')
        self.assertStatusCode(response, 200)
        self.assertEqual(
            json.loads(response.data.decode())['coffee'],
            self.EXAMPLE_OUTPUT
        )

    def test_stats(self):
        response = self.app.get('/api/stats')
        self.assertStatusCode(response, 200)
        self.assertEqual(
            json.loads(response.data.decode())['stats'],
            {
                datetime.utcnow().strftime('%Y-%m-%d'): '1'
            }
        )

    def test_no_status(self):
        self.redis.hdel('coffeestatus', 'status')
        self.redis.hdel('coffeestatus', 'last_start')
        response = self.app.get('/api/status')
        self.assertStatusCode(response, 200)
        self.assertEqual(
            json.loads(response.data.decode())['coffee'],
            self.UNKNOWN_STATUS
        )

    def test_coffeetxt(self):
        response = self.app.get('/coffee.txt')
        self.assertStatusCode(response, 200)
        self.assertEqual(
            response.data.decode(), '1\n%s' % datetime.utcnow().strftime('%d. %B %Y %H:%M:%S')
        )


if __name__ == '__main__':
        unittest.main()
