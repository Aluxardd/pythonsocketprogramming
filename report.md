# Report on Client-Server Connection

## Introduction
This report documents the implementation and observed behaviors of a basic client-server connection that was expanded to handle multiple clients simultaneously. The project transitioned from using TCP to UDP protocols, highlighting the differences in behavior and performance.

## Project Overview
The project consists of a client and server implementation, capable of handling up to 10 clients concurrently. The client sends messages to the server and receives responses, while the server processes these messages and responds accordingly.

## TCP vs. UDP

### TCP (Transmission Control Protocol)
- **Connection-Oriented**: TCP establishes a connection before data can be sent, ensuring reliable communication.
- **Reliability**: Guarantees that data is delivered in order and without loss. If packets are lost, TCP will retransmit them.
- **Flow Control**: Manages data transmission rates to prevent overwhelming the receiver.
- **Use Case**: Suitable for applications where data integrity and order are critical, such as file transfers and web browsing.

### UDP (User Datagram Protocol)
- **Connectionless**: UDP does not establish a connection before sending data, allowing for faster transmission.
- **No Reliability Guarantees**: There is no guarantee that packets will arrive, and they may arrive out of order or be duplicated.
- **Lower Overhead**: With less error-checking and no connection setup, UDP has lower latency and is more efficient for certain applications.
- **Use Case**: Ideal for applications where speed is more critical than reliability, such as video streaming and online gaming.

## Observed Behaviors

### Client-Server Interaction
- **TCP Implementation**: The client successfully connected to the server, sent messages, and received responses. The server handled multiple connections, ensuring that messages were processed in the order they were received.
- **UDP Implementation**: The client was able to send messages to the server without establishing a connection. However, some messages were lost during transmission, and responses were not guaranteed to arrive in the same order they were sent.

### Performance
- **Latency**: The UDP implementation exhibited lower latency compared to TCP, making it more suitable for real-time applications.
- **Throughput**: While TCP maintained a steady throughput due to its reliability mechanisms, UDP allowed for higher throughput in scenarios where some data loss was acceptable.

## Conclusion
The transition from TCP to UDP in the client-server project demonstrated significant differences in behavior, particularly in terms of reliability and performance. While TCP is suitable for applications requiring guaranteed delivery, UDP offers advantages in speed and efficiency for less critical data transmission. This project serves as a foundational exploration of client-server architecture and the implications of protocol choice.