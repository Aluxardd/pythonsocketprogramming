import socket
import threading


def handle_client(client_socket, address):
    print(f"Connection from {address} has been established.")
    while True:
        try:
            message, addr = client_socket.recvfrom(1024)
            if not message:
                break
            print(f"Received from {addr}: {message.decode()}")
            response = f"Echo: {message.decode()}"
            client_socket.sendto(response.encode(), addr)
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()
    print(f"Connection from {address} has been closed.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", 9999))
    print("Server is listening on port 9999...")

    while True:
        message, address = server.recvfrom(1024)
        threading.Thread(target=handle_client, args=(server, address)).start()

if __name__ == "__main__":
    main()