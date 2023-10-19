from elasticsearch import Elasticsearch, exceptions as es_exceptions
import os

# Funzione per esplorare una directory


def crawl_directory(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_list.append(path)
    return file_list


def main():
    directory_to_crawl = '/path/to/your/directory'  # Sostituisci con il tuo percorso
    files_to_index = crawl_directory(directory_to_crawl)

    # Connessione a Elasticsearch
    try:
        es = Elasticsearch(["http://localhost:9200"])

        # Verifica la connessione
        if not es.ping():
            print("Elasticsearch non è raggiungibile!")
            return

        # Crea un indice se non esiste già
        if not es.indices.exists(index="documenti_server"):
            es.indices.create(index="documenti_server")

        # Indicizzazione dei file in Elasticsearch
        for file_path in files_to_index:
            doc = {
                "path": file_path
            }
            try:
                # Modificato da "body" a "document"
                es.index(index="documenti_server", document=doc)
            except es_exceptions.RequestError as e:
                print(
                    f"Errore durante l'indicizzazione del file {file_path}: {e}")

        # Stampa il numero di documenti indicizzati
        doc_count = es.count(index="documenti_server")['count']
        print(f"Numero totale di documenti indicizzati: {doc_count}")

    except es_exceptions.ConnectionError:
        print("Errore di connessione a Elasticsearch!")
    except Exception as e:
        print(f"Si è verificato un errore generico: {e}")


if __name__ == "__main__":
    main()
