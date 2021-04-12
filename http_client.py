from Classes.StreamSocket import StreamSocket as sock

HOST = 'gaia.cs.umass.edu'
PORT = 80
MESSAGE = bytes("GET /wireshark-labs/HTTP-wireshark-file3.html"
" HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n", 'UTF-8')

# Starts a connection and makes an HTTP requests
# Receives and prints the responsse data.
def send_client_request(host, port, msg):
    s = sock()
    if s.start_connection(HOST, PORT):
        data = s.http_client(msg)
        print(data.decode())
        s.close_connection()
    else:
        print("No connection created.")

send_client_request(HOST, PORT, MESSAGE)

