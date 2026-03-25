# app.py ist die zentrale Datei die Flask braucht um den Webserver zu starten. 

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/level1", methods=["GET", "POST"])
def level1():
    return render_template("Level1.html")

@app.route("/richtig")
def richtig():
    return redirect(url_for("level2"))

@app.route("/falsch")
def falsch():
    return render_template("Level1.html", fehler= "falsch")

@app.route("/level2")
def level2():
    return "<h1>Du hast Level 1 geschafft!</h1>"

app.run()