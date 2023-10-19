# elastic_actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from elasticsearch import Elasticsearch

ELASTICSEARCH_HOST = 'localhost'
ELASTICSEARCH_PORT = 9200
BASE_URL = "http://didatticafutura.it:8000"


class ActionSearchElasticsearch(Action):

    def name(self) -> Text:
        return "action_search_elasticsearch"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Ottieni il termine di ricerca dall'ultimo messaggio dell'utente
        query = tracker.latest_message.get('text')

        es = Elasticsearch(
            [f"http://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}"])
        results = es.search(index="documenti_server", body={
            "query": {
                "match": {
                    "path": query
                }
            }
        })

        # Estrai i percorsi dei file dai risultati di Elasticsearch e crea link di download
        file_links = [
            f"{BASE_URL}/rasa/download/{hit['_source']['path']}" for hit in results['hits']['hits']]

        # Se non ci sono risultati, invia un messaggio appropriato
        if not file_links:
            dispatcher.utter_message(
                text="Mi dispiace, non ho trovato risultati per la tua ricerca.")
            return []

        # Altrimenti, costruisci e invia il messaggio con i link
        response_message = "Risultati per la tua ricerca:\n" + \
            "\n".join([f"<a href='{link}'>{link}</a>" for link in file_links])
        dispatcher.utter_message(text=response_message, html=response_message)

        return []
