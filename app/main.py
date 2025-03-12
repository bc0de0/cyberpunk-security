from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)


# Database setup
def init_db():
    conn = sqlite3.connect("security.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logins (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      ip TEXT,
                      timestamp DATETIME,
                      status TEXT)''')
    conn.commit()
    conn.close()


init_db()


# Check for brute force attempts
def check_brute_force(ip):
    conn = sqlite3.connect("security.db")
    cursor = conn.cursor()
    time_threshold = datetime.now() - timedelta(minutes=5)
    cursor.execute("SELECT COUNT(*) FROM logins WHERE ip=? AND timestamp > ? AND status='failed'", (ip, time_threshold))
    attempts = cursor.fetchone()[0]
    conn.close()
    return attempts >= 5


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    ip = request.remote_addr
    status = "failed"
    if check_brute_force(ip):
        return jsonify({"message": "Too many failed attempts. IP blocked."}), 403

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "securepass":
        status = "success"
        message = "Login successful"
    else:
        message = "Invalid credentials"

    conn = sqlite3.connect("security.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logins (ip, timestamp, status) VALUES (?, ?, ?)", (ip, datetime.now(), status))
    conn.commit()
    conn.close()

    return jsonify({"message": message})


@app.route("/logins")
def get_logins():
    conn = sqlite3.connect("security.db")
    cursor = conn.cursor()
    cursor.execute("SELECT ip, timestamp, status FROM logins ORDER BY timestamp DESC LIMIT 50")
    logs = cursor.fetchall()
    conn.close()
    return jsonify(logs)


if __name__ == "__main__":
    app.run(debug=True)
