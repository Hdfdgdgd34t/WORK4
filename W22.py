import threading
import socket
def test_client(host, port, message, client_id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Client {client_id}: Connected to {host}:{port}")
            client_socket.sendall(message.encode('utf-8'))
            print(f"Client {client_id}: Sent message: {message}")
            data = client_socket.recv(1024)
            print(f"Client {client_id}: Response from server: {data.decode('utf-8')}")
    except Exception as e:
        print(f"Client {client_id}: Encountered an error - {e}")
if __name__ == "__main__":
    host, port = '127.0.0.1', 5555
    num_clients = 5
    threads = []
    for i in range(num_clients):
        message = f"Hello from client {i + 1}"
        t = threading.Thread(target=test_client, args=(host, port, message, i + 1))
        threads.append(t)
        t.start()
        print(f"Client {i + 1}: Thread started.")
    for t in threads:
        t.join()
    print("All client threads have finished.")