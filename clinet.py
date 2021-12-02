import socket, threading, os, sys, pygame, time
from importlib.machinery import SourceFileLoader

global address, client_socket, hostname
address = ('<broadcast>', 54545)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
hostname = socket.gethostname()
playerID = False

def listen_for_messages():
    while True:
        recv_data, addr = client_socket.recvfrom(2048)
        message = recv_data.decode()
        print(addr, message)
        if hostname in message:
            message.strip(hostname)

def send_message(message, flag):
    print(message)
    client_socket.sendto(message.encode(), address)


send_message("Ping", 1)
x = threading.Thread(target=listen_for_messages, daemon=True)
x.start()

for loop in range(10):
    send_message("Ping", 1)
    time.sleep(1)

