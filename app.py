from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search_jobs():
    role = request.args.get("role", "").lower()
    location = request.args.get("location", "").lower()

    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()

    query = "SELECT company, role, location, apply_link FROM jobs WHERE LOWER(role) LIKE ? AND LOWER(location) LIKE ?"
    c.execute(query, (f"%{role}%", f"%{location}%"))
    jobs = c.fetchall()
    
    conn.close()

    if not jobs:
        return jsonify({"message": "No jobs found"}), 404

    return jsonify([{"company": job[0], "role": job[1], "location": job[2], "apply_link": job[3]} for job in jobs])

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

