from elasticsearch import Elasticsearch


def add_person(name, info):
    es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
    
    # Dati della persona
    person_data = {
        "name": name,
        "info": info
    }
  
    # Aggiungi la persona all'indice
    es.index(index="people", body=person_data)


if __name__ == "__main__":
    while True:
        print("\n--- Inserimento dati persona ---")
        name = input("Inserisci il nome (o 'exit' per uscire): ")
        if name.lower() == "exit":
            break
        info = input(f"Inserisci le informazioni per {name}: ")
        add_person(name, info)
        print(f"\n{name} è stato aggiunto con successo!")
