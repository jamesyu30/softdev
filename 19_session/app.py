
from flask import Flask, session, render_template, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(6)
app.config['s'] = app.secret_key
user = "a"
passw = "1"

@app.route("/")
def login():
  #  session['username'] = "a"
    if session['username'] == "":
        return render_template('login.html')
    else:
        return "a"
    return render_template('login.html')

@app.route("/auth", methods=['GET', 'POST'])
def auth():
    print(request.form['username'])
    return render_template('response.html')

if __name__ == "__main__": 
    app.debug = True 
    app.run()    

print(request.form['username'])