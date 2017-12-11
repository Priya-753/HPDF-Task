from flask import Flask
import requests
app= Flask(__name__)

@app.route('/authors')
def authors():
	r=requests.get("https://jsonplaceholder.typicode.com/users")
	return jsonify(r.json())
