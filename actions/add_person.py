import sqlite3

def add_person(name, info):
    conn = sqlite3.connect('people_database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO people (name, info) VALUES (?, ?)", (name, info))
    conn.commit()

    conn.close()

# Usa la funzione per aggiungere persone
add_person("Mario Rossi", "E' solo un nome d'esempio presente nel database.")
add_person("Titina Iannucci", "È mia moglie, e guai a chi me la tocca!")
add_person("Angela Rocchia", "E' un'insegnante della scuola primaria, responsabile della funzione strumentale sull'aggiornamento del PTOF, incaricata delle prove invalsi e del sistema di valutazione della scuola")
add_person("Mariantonietta del MOnte", "E' la vicepreside vicaria della scuola, con delega al cordinamento della scuola primaria.")
add_person("Cristina Becci", "Appartiene allo Staff di Presidenza, vicepreside con delega del coordinamento della scuola secondaria di 1° grado")
add_person("Lucia Palmieri", "Cordinatrice del plesso della primaria di Nuova Cliternia")
add_person("Olga Fraccacreta", "Coordinatrice della scuola dell'infanzia")

# ... e così via per ogni persona che desideri aggiungere

