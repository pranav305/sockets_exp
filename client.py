import socket
import threading
import time

HEADER = 64
FORMAT = 'utf-8'
SERVER = "116.73.57.12"
DISCONNECT_MSG = "!d"
PORT = 150
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def recieve():
	while True:
		msg = client.recv(1024).decode(FORMAT)
		print(msg)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)

while True:
	thread = threading.Thread(target=recieve)
	thread.start()
	msg = input("Enter message to send >> ")
	if msg == DISCONNECT_MSG:
		send(msg)
		time.sleep(1)
		break
	send(msg)

print("[DISCONNECTED]")