import socket
import threading

FORMAT = 'utf-8'
DISCONNECT_MSG = "!d"
PORT = 150
SERVER = "192.168.0.2"

ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()

def send2clients(msg):
	with clients_lock:
		for c in clients:
			c.sendall(msg.encode(FORMAT))

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected!")
	try:
		connected = True
		while connected:
			msg = conn.recv(1024).decode(FORMAT)			
			if msg == DISCONNECT_MSG:
				connected = False
			print(f"[{addr}]: {msg}")
			send2clients(msg)
	finally:
		with clients_lock:
			clients.remove(conn)
		conn.close()

def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {ADDR}")
	while True:
		conn, addr = server.accept()
		with clients_lock:
			clients.add(conn)
		thread = threading.Thread(target=handle_client, args=(conn,addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {len(clients)}") 

print("[STARTING]")
start()