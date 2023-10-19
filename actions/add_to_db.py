import sqlite3

def add_person_to_db(name, info):
    conn = sqlite3.connect('people_database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO people (name, info) VALUES (?, ?)", (name, info))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    while True:
        name = input("Inserisci il nome della persona (o 'esci' per terminare): ")
        
        # Se l'utente inserisce 'esci', termina il ciclo
        if name.lower() == 'esci':
            break

        # Converti il nome in minuscolo
        name = name.lower()

        info = input(f"Inserisci le informazioni su {name}: ")

        add_person_to_db(name, info)
        print(f"{name} è stato aggiunto al database con successo!")

