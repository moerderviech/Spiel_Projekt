# app.py ist die zentrale Datei die Flask braucht um den Webserver zu starten. 

# Flask importieren 
from flask import Flask, render_template, redirect, url_for, request

# SQL importieren 
import sqlite3

# Bildschirm leeren
import os

# Passwort verbergen
from werkzeug.security import generate_password_hash, check_password_hash
 
# Flask starten
app = Flask(__name__)

# Link zur Datenbank 
DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.db")
 
# Verbindung zur Datenbank herstellen
def get_db():

    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    return conn


# Route zu Level 1
@app.route("/level1", methods=["GET", "POST"])

def level1():

    return render_template("Level1.html")
 

# Route zu Level 2
@app.route("/level2", methods=["GET", "POST"])

def level2():
    if request.method == "POST":
        wert = int(request.form["regler"])
        if wert == 67:
            return redirect(url_for("level3"))
        else:
            return render_template("Level2.html", fehler="Falscher Wert!")
    return render_template("Level2.html")


# Route zu Level 3 
@app.route("/level3", methods=["GET", "POST"])

def level3():

    return render_template("Level3.html")
 
# Route zu Level 4
@app.route("/level4", methods=["GET", "POST"])

def level4():

    return render_template("Level4.html")

# Route zu Level 5
@app.route("/level5", methods=["GET", "POST"])
def level5():
    if request.method == "POST":
        buchstaben = request.form.getlist("buchstabe")
 
        # Wort zusammenbauen + Case ignorieren
        wort = "".join(buchstaben).upper()
 
        if wort == "BERNDSCHOBER":
            return redirect(url_for("start"))
        else:
            return render_template("Level5.html", fehler="Falsch!")
 
    return render_template("Level5.html")
 
# Route zum Start-Menue
@app.route("/start", methods=["GET", "POST"])

def start():

    return render_template("start.html")
 
 
@app.route("/richtig")

def richtig():

    return redirect(url_for("level2"))
 
 
@app.route("/falsch")

def falsch():

    return render_template("Level1.html", fehler="falsch")
 
# Route zur Registrierung
@app.route("/registrieren", methods=["GET", "POST"])

def registrierung():

    fehler = None

    erfolg = None
 
    if request.method == "POST":

        username = request.form.get("username", "").strip()

        password = request.form.get("password", "")

        password2 = request.form.get("password2", "")
 
        if not username or not password or not password2:

            fehler = "Bitte alle Felder ausfüllen."
 
        elif password != password2:

            fehler = "Die Passwörter stimmen nicht überein."
 
        else:

            password_hash = generate_password_hash(password)
 
            try:

                conn = get_db()

                cursor = conn.cursor()
 
                cursor.execute(

                    "INSERT INTO users (username, password) VALUES (?, ?)",

                    (username, password_hash)

                )
 
                conn.commit()

                conn.close()
 
                erfolg = "Registrierung erfolgreich."

                return redirect(url_for("anmeldung"))
 
            except sqlite3.IntegrityError:

                fehler = "Benutzername existiert bereits."

                conn.close();
 
            except sqlite3.Error:

                fehler = "Datenbankfehler bei der Registrierung."
 
    return render_template("Registrierung.html", fehler=fehler, erfolg=erfolg)
 

# Route zur Anmeldung
@app.route("/anmeldung", methods=["GET", "POST"])
def anmeldung():
    fehler = None

    # Formular wird verschickt wenn user auf weiter klickt 
    if request.method == "POST":

        # Eingaben vom user aus dem Formular holen
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        # Prüfen, ob es leere Felder gibt
        if not username or not password:
            # Wenn ja Fehlermeldung ausgeben 
            fehler = "Bitte Benutzername und Passwort eingeben."
            return render_template("Anmeldung.html", fehler=fehler)

        try:
            conn = get_db()
            cursor = conn.cursor()

            # User anhand von username aus der Datenbank holen
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            conn.close()

            if user:
                # Passwort prüfen
                if check_password_hash(user["password"], password):

                    # Zur Startseite wenn Login erfolgreich
                    return redirect(url_for("start"))
                else:
                    fehler = "Benutzername oder Passwort ist falsch."
            else:
                fehler = "Benutzername oder Passwort ist falsch."

        except sqlite3.Error:
            fehler = "Datenbankfehler bei der Anmeldung."

    return render_template("Anmeldung.html", fehler=fehler)


if __name__ == "__main__":

    app.run(debug=True)
 