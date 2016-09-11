from flask import Flask, request, render_template, redirect
import socket
import sys
import netifaces as ni

app = Flask(__name__)

database = {}
database['file'] = []

@app.route("/upload")
def upload():
	return render_template('upload.html')

@app.route("/uploadfile", methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		ip_addr = request.form['ip_addr']
		database['file'].append(ip_addr)
		return redirect('http://localhost:4999/send')
		# return render_template('seeding.html')

@app.route("/download")
def download():
	return render_template('download.html', database=database)

if __name__ == '__main__':
	if (len(sys.argv) == 1):
		port = 5000
	else:
		port = int(argv[1])
	host = ni.ifaddresses('eno1')[2][0]['addr']
	app.run(host=host, debug=True, port=port)

