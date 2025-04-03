# Python Client-Server Project

This project implements a basic client-server architecture using both TCP and UDP protocols. It is designed to handle multiple clients simultaneously and provides a framework for sending and receiving messages between clients and the server.

## Project Structure

```
python-client-server
├── client
│   ├── client.py        # Client implementation
├── server
│   ├── server.py        # Server implementation
├── tests
│   ├── test_client.py    # Unit tests for client
│   ├── test_server.py    # Unit tests for server
├── report.md            # Report on observed behaviors
└── README.md            # Project overview and instructions
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd python-client-server
   ```

2. **Install dependencies:**
   Ensure you have Python installed. You may need to install additional libraries depending on your implementation.

3. **Run the server:**
   Open a terminal and navigate to the `server` directory. Run the server using:
   ```
   python server.py
   ```

4. **Run the client:**
   Open another terminal and navigate to the `client` directory. Run the client using:
   ```
   python client.py
   ```

## Usage Guidelines

- The client will prompt for user input to send messages to the server.
- The server will respond to each message sent by the client.
- You can run multiple instances of the client to test the server's ability to handle simultaneous connections.

## Testing

To run the unit tests for both the client and server, navigate to the `tests` directory and execute:
```
python -m unittest test_client.py
python -m unittest test_server.py
```

## Report

Refer to `report.md` for a detailed analysis of the observed behaviors of the client-server connection, including comparisons between TCP and UDP protocols.