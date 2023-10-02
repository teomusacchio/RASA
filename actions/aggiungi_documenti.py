from elasticsearch import Elasticsearch

# Collegamento a Elasticsearch
es = Elasticsearch(hosts=["http://localhost:9200"])


def inserisci_documento():
    # Raccolta dei dati
    nome_documento = input(
        "Inserisci il nome del documento (o 'exit' per uscire): ")

    if nome_documento == "exit":
        return False

    url_documento = input("Inserisci l'URL del documento: ")
    # Crea il documento
    documento = {
        "nome_documento": nome_documento,
        "url_documento": url_documento
    }

# Inserimento del documento in Elasticsearch
    es.index(index="documenti", document=documento)
    # Usa 'document' al posto di 'body'
    print("Documento inserito con successo!\n")
    return True


def main():
    print("Inserimento dei documenti in Elasticsearch")
    print("-----------------------------------------\n")

    while inserisci_documento():
        pass

    print("Uscita dall'inserimento dei documenti.")


if __name__ == "__main__":
    main()
    main()
