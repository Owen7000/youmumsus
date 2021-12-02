import time, sys, os, socket, threading
def start_server():
    global address, server_socket
    address = ('', 54545)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server_socket.bind(address)
    os.system("cls")
    print("Server setup complete")
    print("Your IP Address is:" + socket.gethostbyname(socket.gethostname()))

def listen_for_messages():
    while True:
        print("Listening")
        recv_data, addr = server_socket.recvfrom(2048)
        message = recv_data.decode()
        print(addr, ":", message)
        message = ("*"+str(message)+" Response").encode()
        server_socket.sendto(message, addr)


print(" ,---------------------------,\n","|  /---------------------\  |\n","| |                       | |\n","| |     Buggy             | |\n","| |      Software         | |\n","| |            co         | |\n","| |                       | |\n","|  \_____________________/  |\n","|___________________________|\n",",---\_____     []     _______/------,\n","/         /______________\           /|\n","/___________________________________ /  | ___\n","|                                   |   |    )\n","|  _ _ _                 [-------]  |   |   (\n","|  o o o                 [-------]  |  /    _)_\n","|__________________________________ |/     /  /\n","/-------------------------------------/|      ( )/\n","  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /\n","/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /\n","~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ","\nA Buggy Software game")
time.sleep(10)
os.system("cls") 
time.sleep(5)
print("Please wait")
x = threading.Thread(target=start_server, daemon=True)
x.start()
time.sleep(5)
x = threading.Thread(target=listen_for_messages)
print("Listening for messages")
x.start()