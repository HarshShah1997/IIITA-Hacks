#Main_Server is the hosted server that contains the files in different client machines and their IPs

from flask import Flask, request, render_template, redirect
import socket
import sys
import netifaces as ni
import sqlite3

app = Flask(__name__)

@app.route("/upload")
def upload():                                           #Renders Upload Template
	return render_template('upload.html')

@app.route("/uploadfile", methods=['GET', 'POST'])
def upload_file():                                      #Adds IP list to database dictionary
	if request.method == 'POST':
		ip_addr = request.form['ip_addr']
		file_name = request.form['file_name']
		insert_to_database(ip_addr, file_name)
		return redirect('http://localhost:4999/send?file_name=' + file_name)
		# return render_template('seeding.html')

@app.route("/download")
def download():                                       #Renders Download Template
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	result = cur.execute('SELECT filename, ipaddr FROM data')
	data = cur.fetchall()
	print(data)
	return render_template('download.html', database=data)

def insert_to_database(ip_addr, file_name):
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cur.execute('INSERT INTO data (ipaddr, filename) VALUES (?, ?)', (ip_addr, file_name))
	conn.commit()
	conn.close()

if __name__ == '__main__':
	if (len(sys.argv) == 1):
		port = 5000
	else:
		port = int(argv[1])
	host = ni.ifaddresses('eno1')[2][0]['addr']
	app.run(host=host, debug=True, port=port)
