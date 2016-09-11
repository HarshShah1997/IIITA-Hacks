from flask import *

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")

@app.route("/connect", methods=['GET', 'POST'])
def connect():
	if request.method == 'POST':
		ip_addr = request.form['ip_addr']
		#Sending request on IP 

if __name__ == '__main__':
	app.run(debug=True)


