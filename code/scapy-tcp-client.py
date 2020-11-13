from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from scapy.layers.inet import IP, TCP, UDP, Ether
from scapy.volatile import RandShort
from scapy.packet import Raw
from scapy.all import *
import os

import socket

HOST = '127.0.0.1'
PORT = 10000
SIZE = 128

print(f'Open connection to {HOST:s}:{PORT:d}')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f'Connect to {HOST:s}:{PORT:d}')

message = struct.pack(">H", SIZE) + os.urandom(SIZE)

n = client.send(message)
if n != len(message):
    print("An error occurred while sending the message to the server!")
else:
    print("OK")

print("Disconnect")
client.close()
