from flask import Flask, render_template
app = Flask(__name__)

@app.route('/html')
def html():
   	return render_template("index.html")

@app.route('/image')
def image():
	return render_template("image.html")	
