from flask import Flask, render_template, request
import socket
import os
import netifaces as ni
import sys
from threading import Thread
import sqlite3

app = Flask(__name__)
file_name = None

def waitSocket(file_name):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                      #Sends File
	host = ni.ifaddresses('eno1')[2][0]['addr']
	port = 6790
	sock.bind((host, port))
	sock.listen(5)
	while (True):
		conn, addr = sock.accept()
		fp = open(file_name, 'rb')
		byte = fp.read(1024)
		while (byte):
			conn.send(byte)
			byte = fp.read(1024)
		fp.close()
		conn.close()

@app.route("/send")
def send():
	global file_name
	file_name = request.args.get('file_name')
	socketThread=Thread(target=waitSocket,args=[file_name])
	socketThread.start()
	return render_template('wait.html')

@app.route("/stop")
def stop():
	return "Closed successfully"
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cur.execute('DELETE FROM data WHERE filename = ?', file_name)
	conn.commit()
	conn.close()
	

if __name__ == '__main__':
	if (len(sys.argv) == 1):
		port = 4999
	else:
		port = int(sys.argv[1])
	app.run(debug=True, port=port)

