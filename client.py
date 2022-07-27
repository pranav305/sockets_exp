import socket

HEADER = 64
FORMAT = 'utf-8'
SERVER = "26.200.3.189"
DISCONNECT_MSG = "!d"
PORT = 5000
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)

while True:
	msg = input("Enter message to send >> ")
	if msg == DISCONNECT_MSG:
		break
	send(msg)