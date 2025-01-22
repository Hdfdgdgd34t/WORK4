import socket
import os
def file_exists(file_path):
    return os.path.isfile(file_path)
def establish_connection(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")
    return client_socket
def send_file_content(file_path, client_socket, buffer_size=4096):
    with open(file_path, "rb") as file:
        while (chunk := file.read(buffer_size)):
            client_socket.sendall(chunk)
def send_file(file_path, host='127.0.0.1', port=5555, buffer_size=4096):
    if not file_exists(file_path):
        print(f"Error: File {file_path} not found.")
        return
    file_name = os.path.basename(file_path)
    client_socket = establish_connection(host, port)
    client_socket.send(file_name.encode())
    send_file_content(file_path, client_socket, buffer_size)
    print(f"File {file_name} sent successfully to the server.")
    client_socket.close()
if __name__ == "__main__":
    file_path = input("Please enter the file path: ").strip()
    send_file(file_path)