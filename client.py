import socket
import threading

def handle_server_response(sock):
    while True:
        try:
            response = sock.recv(1024).decode('utf-8')
            if response:
                print(f"Server: {response}")
            else:
                break
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

def main():
    server_address = ('localhost', 12345)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    threading.Thread(target=handle_server_response, args=(sock,), daemon=True).start()

    while True:
        message = input("Enter message to send to server (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        sock.sendto(message.encode('utf-8'), server_address)

    sock.close()

if __name__ == "__main__":
    main()