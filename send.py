from flask import *
import socket
import os
import netifaces as ni

@app.route("/")
def root():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ni.ifaddresses('eth0')
	host = ni.ifaddresses('eth0')[2][0]['addr']
	port = 6790
	sock.bind((host, port))
	sock.listen(5)
	conn, addr = sock.accept()
	fp = open('sendtest', 'rb')
	byte = fp.read(1024)
	while (byte):
		conn.send(byte)
		byte = fp.read(1024)
	fp.close()
	conn.close()
	return "Transfered successfully"



