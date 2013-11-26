import unittest
import json

from coffee import server
from coffee.models import Status


class TestViews(unittest.TestCase):

    EXAMPLE_STATUS = {
        "status": True,
        "last_start": "2012-12-12 12:12",
    }
    UNKNOWN_STATUS = {
        "status": "unknown"
    }

    def setUp(self):
        self.app = server.app.test_client()
        self.status = Status()
        self.redis = self.status.redis
        self.redis.hmset('coffeestatus', self.EXAMPLE_STATUS)

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

    def test_no_status(self):
        self.redis.hdel('coffeestatus', 'status')
        self.redis.hdel('coffeestatus', 'last_start')
        response = self.app.get('/api/status')
        self.assertStatusCode(response, 200)
        self.assertEquals(
            json.loads(response.data)['coffee'],
            self.UNKNOWN_STATUS
        )


if __name__ == '__main__':
        unittest.main()
