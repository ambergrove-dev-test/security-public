import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def user():
    name = request.args.get("name")
    conn = sqlite3.connect("app.db")
    # deliberately unsafe: SQL built from request input
    rows = conn.execute("SELECT * FROM users WHERE name = '%s'" % name).fetchall()
    return str(rows)


@app.route("/ping")
def ping():
    host = request.args.get("host")
    # deliberately unsafe: shell command built from request input
    return subprocess.check_output("ping -c 1 " + host, shell=True)


@app.route("/calc")
def calc():
    return str(eval(request.args.get("expr")))
