from Classes.StreamSocket import StreamSocket as sock

HOST = 'localhost'
PORT = 11234

# Initiates and starts an HTTP server from StreamSocket class
# Sends specified data when requested
def start_server():
    data = bytes("HTTP/1.1 200 OK\r\n"\
    "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
    "<html>Congratulations! You've downloaded the first"\
    " Wireshark lab file!</html>\r\n", 'UTF-8')

    s = sock()
    s.http_server(data, HOST, PORT)

start_server()