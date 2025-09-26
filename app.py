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
    return render_template("guestbook.html")

@app.route("/submitted", methods=['POST'])
def submitted():
    first_name = request.form.get('fname', '')
    last_name = request.form.get('lname', '')
    new_entry = {
        "FirstName": first_name,
        "LastName": last_name
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
    return render_template("guestbook.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')