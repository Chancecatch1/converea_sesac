import sys
from time import sleep
import random
import time
import json
import socket

if __name__ == "__main__":
    HOST=''
    PORT=7477
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 7477))
    server_socket.listen(1)

    while True:
        try:
            client_socket,addr = server_socket.accept()
            data = client_socket.recv(1024)
            if not data:
                break

            result = 'hello'
            received = data.decode('utf-8')
            data = json.dumps(result)
            client_socket.sendall(data.encode('utf-8'))
            print(json.dumps(result))

        except Exception as e:
            print(e)
            continue