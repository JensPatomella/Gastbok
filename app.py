from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

class Subs:
    def __init__(self, First_Name, Last_Name):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guestbook")
def guestbook():
    return render_template("guestbook.html")

@app.route("/submitted")
def guestbook():
    a = Subs(request.form.get('First_Name', ''), request.form.get('Last_Name', ''))
    return render_template("guestbook.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')