-- Datei: users_db.sql

-- Tabelle erstellen
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

-- Beispiel-Nutzer einfügen (Passwort im Klartext nur zum Testen)
INSERT INTO users (username, password) VALUES 
('alice', 'password123'),
('bob', 'geheim');