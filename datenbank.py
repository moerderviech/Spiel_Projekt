import sqlite3
 
# Dateinamen
DB_NAME = "users.db"

def add_highscore(username, score):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO highscores (username, highscore) VALUES (?, ?)", 
                   (username, score))
    
    conn.commit()

def get_top10_highscores():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT username, MIN(highscore) FROM highscores GROUP BY username ORDER BY highscore DESC LIMIT 10")

    return dict(cursor.fetchall())