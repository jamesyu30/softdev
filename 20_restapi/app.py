from flask import Flask, session, render_template, request, redirect
import requests
import json
app = Flask(__name__)

@app.route("/")
def get():
    with open('key_nasa.txt') as f:
        k = f.readlines() #nasa api key
    key = k[0]#changes the key from a list to a string
    data = requests.get(url=f"https://api.nasa.gov/planetary/apod?api_key={key}")
    url = json.loads(data.text)["url"] #res.text turns res into a string, json.loads converts json string to dictionary
    explanation = json.loads(data.text)["explanation"]
    return render_template("main.html", url=url, e=explanation)
 
if __name__ == "__main__":
    app.debug = True
    app.run()
