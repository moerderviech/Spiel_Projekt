-- Datei: users_db.sql

-- Tabelle erstellen
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

-- Highscore Tabelle erstellen
CREATE TABLE IF NOT EXISTS highscores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    highscore INTEGER NOT NULL UNIQUE
)

-- Zum Testen:
-- Benutzername:    test
-- Passwort:        test
