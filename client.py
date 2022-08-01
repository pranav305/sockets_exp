from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import sys
import socket
import threading
import time

FORMAT = 'utf-8'
DISCONNECT_MSG = "!d"


class MainUI(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("app.ui", self)
		self.ConnectBTN.clicked.connect(self.connect_server)
		self.SendBTN.clicked.connect(self.send)
		self.DisconnectBTN.clicked.connect(self.disconnect)
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.show()
	
	def connect_server(self):
		self.server = self.IPEdit.text()
		self.port = self.PortEdit.text()
		self.username = self.UsernameEdit.text()
		self.addr = (self.server, int(self.port))
		self.client.connect(self.addr)
		time.sleep(0.5)
		reciever.start()
	
	def send(self):
		msg = self.messageEdit.text()
		self.messageEdit.clear()
		message = f"[{self.username}]: {msg}".encode(FORMAT)
		self.client.sendall(message)
	
	def disconnect(self):
		self.client.sendall(DISCONNECT_MSG.encode(FORMAT))

def recieve():
	while True:
		msg = UIWindow.client.recv(1024).decode(FORMAT)
		UIWindow.MessagesDisplay.insertPlainText(msg + "\n")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	UIWindow = MainUI()
	reciever = threading.Thread(target=recieve)
	app.exec_()