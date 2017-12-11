from flask import Flask,request,redirect

app=Flask(__name__)

@app.route("/robots.txt")
def robots():
	return redirect("http://httpbin.org/deny",code = 302)


