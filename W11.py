import socket
def start_server(host='127.0.0.1', port=5555):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()
            print(f"Server is listening on {host}:{port}")
            while True:
                conn, addr = server_socket.accept()
                print(f"Connected by {addr}")
                handle_client(conn, addr)
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        print("Server shutting down.")
def handle_client(conn, addr):
    try:
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"Connection with {addr} closed.")
                    break

                message = data.decode('utf-8')
                print(f"Received from {addr}: {message}")
                conn.sendall(data)
    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        conn.close()
if __name__ == "__main__":
    start_server()