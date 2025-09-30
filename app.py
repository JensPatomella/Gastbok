from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)
JSON_FILE = "data.json"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guestbook")
def guestbook():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    return render_template("guestbook.html", guests=data)

@app.route("/submitted", methods=['POST'])
def submitted():
    first_name = request.form.get('fname', '')
    email = request.form.get('email', '')
    time = request.form.get('time', '')
    new_entry = {
        "Name": first_name,
        "Email": email,
        "Time": time
    }
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    data = [data]
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(new_entry)
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    return render_template("guestbook.html", guests=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')