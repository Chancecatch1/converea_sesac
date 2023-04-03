import time
import socket

# HOST='172.17.247.230'
HOST='192.168.14.8'
PORT=7477

while True:
    print("connected...")
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST,7477))
    client_socket.sendall('data'.encode('utf-8'))
    data = client_socket.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
    client_socket.close()
    time.sleep(2)
