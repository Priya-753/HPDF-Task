from flask import Flask,make_response,request
app = Flask(__name__)

@app.route("/setcookie")
def setcookie():
	resp = make_response('Setting Cookie')
	resp.set_cookie('name','Priyadarshini T')
	resp.set_cookie('age','20')
	return resp

@app.route("/getcookie")
def getcookie():
	name = request.cookies.get('name')
	age = request.cookies.get('age')
	return 'Name : ' + name +' Age : ' + age

if __name__ == '__main__':
	app.run(debug=True)
