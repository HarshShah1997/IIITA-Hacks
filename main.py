from flask import *
import socket
import sys

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/connect", methods=['GET', 'POST'])
def connect():

	if request.method == 'POST':
		ip_addr = request.form['ip_addr']
		#Sending request on IP
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_port = 6790
		sock_host = ip_addr
		sock.connect((sock_host, sock_port))
		fp = open("recvtest", "wb")
		l = sock.recv(1024)
		while (l):
			fp.write(l)
			l = sock.recv(1024)
		fp.close()
		sock.close()


if __name__ == '__main__':
	port = int(sys.argv[1])
	app.run(debug=True, port=port)


