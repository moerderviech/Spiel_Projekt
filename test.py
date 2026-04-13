# Alte User löschen:

import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "users.db")

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("DELETE FROM users")  # löscht ALLE User

conn.commit()
conn.close()

print("Alle User wurden gelöscht.")

#Clickcounter 
        # let click_count = parseInt( `{{ clicks }}`) || 0;

        # document.addEventListener("click", function(event)
        # {
        # click_count++;
        #  document.getElementById("clicks").value = click_count;
        # })