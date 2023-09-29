from elasticsearch import Elasticsearch


def create_index():
    # Connetti al cluster di Elasticsearch
    es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
    
    # Verifica se l'indice esiste già
    if not es.indices.exists(index="people"):
        # Definizione dello schema dell'indice
        mapping = {
            "mappings": {
                "properties": {
                    "name": {
                        "type": "text"
                    },
                    "info": {
                        "type": "text"
                    }
                }
            }
        }
        
        # Crea l'indice
        es.indices.create(index="people", body=mapping)
        print("Indice 'people' creato con successo!")
    else:
        print("L'indice 'people' esiste già!")


if __name__ == "__main__":
    create_index()
