from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from elasticsearch import Elasticsearch
from django.utils.safestring import mark_safe


class ActionMostraDocumento(Action):

    def name(self) -> str:
        return "action_mostra_documento"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: dict) -> list:
        # Collegamento a Elasticsearch
        es = Elasticsearch(["http://localhost:9200"])
        # Ottenere l'ultimo messaggio dell'utente (la query di ricerca)
        query = tracker.latest_message.get('text')

        try:
            # Eseguire la ricerca in Elasticsearch
            response = es.search(index="documenti", body={
                "query": {
                    "match": {
                        "nome_documento": query
                    }
                }
            })

            hits = response.get('hits', {}).get('hits', [])

            if hits:
                doc_info = hits[0]['_source']['nome_documento']
                link = hits[0]['_source']['url_documento']
                response_text = f"Documento trovato: {doc_info}. Link al documento: <a href='{link}'>Clicca qui</a>"
                dispatcher.utter_message(text=mark_safe(response_text))
            else:
                dispatcher.utter_message(text="Documento non trovato.")

        except Exception as e:
            # Stampa l'eccezione per diagnosticare il problema
            print(str(e))
            # Puoi anche inviare un messaggio all'utente
            # per informarlo che c'è stato un problema
            dispatcher.utter_message(text="Si è verificato un errore durante la ricerca. Riprova più tardi.")

        return []
