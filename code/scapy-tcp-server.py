# Implement a TCP server.
# Please note that this script must be executed as "root" (because we use the function "sendp()").
#
# Under Debian 10:
#       xhost +
#       sudo su
# And, eventually (if you use pipenv):
#       pipenv shell


from scapy.layers.inet import Ether
from scapy.all import *


SERVER_ADDRESS: str = '127.0.0.1'
SERVER_PORT: int = 10000


# Read a given number of bytes from a socket.
# @param in_connection The socket.
# @param in_count The number of bytes to receive.
# @return Upon successful completion, the function returns the bytes that have been read.
#         Otherwise, ir returns the value b"".
def read_bytes_from_socket(in_connection, in_count):
    data = b""
    while len(data) < in_count:
        d = in_connection.recv(in_count - len(data))
        if not d:
            return b""
        data = data + d
    return data


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the port
print(f'Starting up on {SERVER_ADDRESS:s}:{SERVER_PORT:d}')
server_address = (SERVER_ADDRESS, SERVER_PORT)
sock.bind(server_address)

# Listen for incoming connections
print('Listen for connexion requests')
sock.listen(1)

while True:
    # Wait for a connection
    print("Wait for connexion request...")
    connection, client_address = sock.accept()

    try:
        print(f'Connection request')
        while True:
            # Get the size
            size = read_bytes_from_socket(connection, 2)
            if not size:
                print("Client closed the connexion")
                break
            print(f"data = {str(size):s}")
            expected_payload_length = struct.unpack('>H', size)[0]
            print(f"Get the length: {expected_payload_length:d}")

            # Get the payload
            payload = read_bytes_from_socket(connection, expected_payload_length)
            if not payload:
                print("Client closed the connexion")
                break

            # Send the data to the network
            print(f"Send {expected_payload_length:d} bytes")
            print(f"{str(payload):s}")
            packet = sendp(Ether(payload), iface='eno1')
    finally:
        # Clean up the connection
        print("An error occurred!")
        connection.close()
