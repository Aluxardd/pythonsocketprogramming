import socket
import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client('localhost', 12345)

    def test_connection(self):
        self.assertTrue(self.client.connect())

    def test_send_receive(self):
        self.client.connect()
        message = "Hello, Server!"
        response = self.client.send_message(message)
        self.assertEqual(response, "Echo: Hello, Server!")

    def tearDown(self):
        self.client.close()

if __name__ == '__main__':
    unittest.main()