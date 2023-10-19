import sqlite3

# Crea una nuova connessione al database
conn = sqlite3.connect('people_database.db')
cursor = conn.cursor()

# Crea una nuova tabella
cursor.execute('''
CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    info TEXT
)
''')


conn.commit()
conn.close()
