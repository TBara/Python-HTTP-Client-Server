# References:
# https://realpython.com/python-sockets/#echo-client
# https://stackoverflow.com/questions/17667903/python-socket-receive-large-amount-of-data
# https://realpython.com/python-sockets/#echo-server

import socket

BUFFER = 2048

# Simple HTTP client and server class
class StreamSocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            )
            # Prevent [Errno 98] Address already in use
            self.sock.setsockopt(socket.SOL_SOCKET, \
                socket.SO_REUSEADDR, 1)
        else:
            self.sock = sock

    # Connects to provided host on a given port
    def start_connection(self, host, port):
        try:
            self.sock.connect((host, port))
        except socket.error as err:
            print(err)
            return False
        return True

    # Close socket
    def close_connection(self):
        self.sock.close()

    # Accepts a bytes formatted http request and sends it
    # to the server. Returns server provided data
    def http_client(self, request):
        self.sock.sendall(request)

        data = b''
        while True:
            packet = self.sock.recv(BUFFER)
            data += packet
            if len(packet) == 0:
                break
        return data

    # Start a simple server by binding and listening
    # to provided host and port. Once request is received,
    # it sends provided data to the client.
    def http_server(self, data, host, port):
        self.sock.bind((host, port))
        self.sock.listen(5)

        conn, addr = self.sock.accept()
        with conn:
            try:
                print(f'Connected by {addr}\n')
                req = conn.recv(BUFFER)   
                print('Received: ', req)
                
                print("\nSending>>>>>>>>>>>>>>")
                conn.sendall(data)
                print(data.decode())
                print("<<<<<<<<<<<<<<<<")
                
            except socket.error as e:
                print("Socket error: %s", e)
            finally:
                conn.close()
                self.close_connection()
        return