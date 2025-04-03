import socket
import unittest
from server.server import start_server

class TestServer(unittest.TestCase):
    def setUp(self):
        self.server_socket = start_server()
        self.server_socket.setblocking(False)

    def tearDown(self):
        self.server_socket.close()

    def test_handle_multiple_clients(self):
        clients = []
        for i in range(10):
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            clients.append(client_socket)

        for i, client in enumerate(clients):
            message = f"Hello from client {i}"
            client.sendto(message.encode(), ('localhost', 12345))

        for i, client in enumerate(clients):
            response, _ = client.recvfrom(1024)
            self.assertEqual(response.decode(), f"Received: Hello from client {i}")

        for client in clients:
            client.close()

if __name__ == '__main__':
    unittest.main()