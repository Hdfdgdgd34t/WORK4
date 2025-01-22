import socket
def connect_to_server(host='127.0.0.1', port=5555):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print(f"Successfully connected to server at {host}:{port}")
        return client_socket
    except ConnectionError as e:
        print(f"Failed to connect to server: {e}")
        return None
def handle_client_communication(client_socket):
    try:
        while True:
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.strip().lower() == 'exit':
                print("Closing connection.")
                break
            client_socket.sendall(message.encode('utf-8'))
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred during communication: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")
def start_client(host='127.0.0.1', port=5555):
    client_socket = connect_to_server(host, port)
    if client_socket:
        handle_client_communication(client_socket)
if __name__ == "__main__":
    start_client()