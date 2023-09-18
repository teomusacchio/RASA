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

# Inserisci alcuni dati di esempio
cursor.execute("INSERT INTO people (name, info) VALUES (?, ?)", ("Mario Rossi", "Mario Rossi è un famoso ingegnere italiano."))
# Aggiungi altre righe come questa per altri nomi

# Commit delle modifiche e chiusura
conn.commit()
conn.close()
