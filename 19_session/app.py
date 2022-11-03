
from flask import Flask, sessions, render_template, request

app = Flask(__name__)
@app.route("/")
def login():
    return render_template('login.html')

@app.route("/auth", methods=['GET', 'POST'])
def auth():
    return render_template('response.html')

if __name__ == "__main__": 
    app.debug = True 
    app.run()    

