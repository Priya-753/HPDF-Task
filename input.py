from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'Welcome %s' % name

@app.route('/input',methods = ['POST', 'GET'])
def input():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('name')
      return redirect(url_for('success',name = user))

