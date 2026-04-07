import sqlite3
import os
 
# Dateinamen
DB_NAME = "users.db"
SQL_FILE = "create_DB.sql"
 
def init_db():
    # DB erstellen / öffnen
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
 
    try:
        # SQL Datei lesen
        with open(SQL_FILE, "r", encoding="utf-8") as f:
            sql_script = f.read()
 
        # SQL ausführen
        cursor.executescript(sql_script)
        conn.commit()
 
        print("Datenbank erfolgreich erstellt aus SQL-Datei!")
 
    except FileNotFoundError:
        print(f"SQL-Datei '{SQL_FILE}' nicht gefunden!")
    except sqlite3.Error as e:
        print("SQLite Fehler:", e)
    finally:
        conn.close()
 
if __name__ == "__main__":
    init_db()


