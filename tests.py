import unittest
import server
import json


class TestViews(unittest.TestCase):

    EXAMPLE_STATUS = {
        "status": "on",
        "last_start": "2012-12-12 12:12",
    }

    def setUp(self):
        self.app = server.app.test_client()
        self.redis = server.r
        self.redis.hmset('coffeestatus', self.EXAMPLE_STATUS)

    def tearDown(self):
        pass

    def assertStatusCode(self, response, expected):
        self.assertEquals(response._status_code, expected)

    def test_index(self):
        response = self.app.get('/')
        self.assertStatusCode(response, 200)

    def test_status(self):
        response = self.app.get('/?json')
        self.assertStatusCode(response, 200)
        self.assertEquals(
            json.loads(response.data),
            self.EXAMPLE_STATUS
        )

if __name__ == '__main__':
        unittest.main()
