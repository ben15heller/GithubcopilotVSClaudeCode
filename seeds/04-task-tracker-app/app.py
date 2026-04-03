"""
Morning Brew — Team Task Tracker
A simple Flask web app for the Azure deployment test.
Both tools receive this identical app and are asked to deploy it to Azure.
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Simple in-memory task store (persists for session)
# In a real app this would be a database
TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    assignee = request.form.get("assignee", "").strip()
    if title:
        tasks = load_tasks()
        tasks.append({
            "id": len(tasks) + 1,
            "title": title,
            "assignee": assignee or "Unassigned",
            "status": "To Do",
            "created": datetime.now().strftime("%b %d, %Y")
        })
        save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):
    tasks = load_tasks()
    status = request.form.get("status")
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            break
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
