from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

# 🔐 API KEY (added)
API_KEY = "12345"

# 🔒 API security (added)
@app.before_request
def check_api_key():
    if request.path.startswith("/api"):
        key = request.args.get("api_key")
        if key != API_KEY:
            return {"error": "Unauthorized"}, 401

# DB connection (same)
def get_data(query):
    conn = sqlite3.connect("village.db")
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

# 🌐 UI route (same)
@app.route("/", methods=["GET", "POST"])
def home():
    data = []

    if request.method == "POST":
        search_type = request.form["type"]
        value = request.form["value"]

        if search_type == "state":
            query = f"SELECT * FROM villages WHERE `STATE NAME` LIKE '%{value}%' LIMIT 50"

        elif search_type == "district":
            query = f"SELECT * FROM villages WHERE `DISTRICT NAME` LIKE '%{value}%' LIMIT 50"

        else:
            query = f"SELECT * FROM villages WHERE `Area Name` LIKE '%{value}%' LIMIT 50"

        data = get_data(query)

    return render_template("index.html", data=data)

# 🚀 API routes (added)
@app.route("/api/state/<name>")
def api_state(name):
    query = f"SELECT * FROM villages WHERE `STATE NAME` LIKE '%{name}%' LIMIT 50"
    data = get_data(query)
    return jsonify(data)

@app.route("/api/district/<name>")
def api_district(name):
    query = f"SELECT * FROM villages WHERE `DISTRICT NAME` LIKE '%{name}%' LIMIT 50"
    data = get_data(query)
    return jsonify(data)

@app.route("/api/village/<name>")
def api_village(name):
    query = f"SELECT * FROM villages WHERE `Area Name` LIKE '%{name}%' LIMIT 50"
    data = get_data(query)
    return jsonify(data)

# 📊 stats route (added)
@app.route("/stats")
def stats():
    conn = sqlite3.connect("village.db")
    cursor = conn.cursor()
    total = cursor.execute("SELECT COUNT(*) FROM villages").fetchone()[0]
    conn.close()
    return f"Total Records: {total}"

# ▶️ run (same)
if __name__ == "__main__":
    app.run(debug=True)