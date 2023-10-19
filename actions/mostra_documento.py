from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from elasticsearch import Elasticsearch
from django.utils.safestring import mark_safe


class ActionMostraDocumento(Action):

    def name(self) -> str:
        return "action_mostra_documento"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        # Collegamento a Elasticsearch
        es = Elasticsearch(["http://localhost:9200"])

        # Ottenere l'ultimo messaggio dell'utente
        query = tracker.latest_message.get('text')

        try:
            # Eseguire la ricerca full-text in Elasticsearch
            response = es.search(index="documenti", body={
                "query": {
                    "match": {
                        "nome_documento": query
                    }
                }
            })

            hits = response.get('hits', {}).get('hits', [])

            if hits:
                response_texts = []
                for hit in hits:
                    doc_info = hit['_source']['nome_documento']
                    link = hit['_source']['url_documento']
                    text = (f"Documento: {doc_info}. "
                            f"Link: <a href='{link}'>Clicca qui</a>")
                    response_texts.append(text)

                # Unisci i risultati in un singolo messaggio
                dispatcher.utter_message(
                    text=mark_safe('\n'.join(response_texts)))
            else:
                dispatcher.utter_message(text="Documento non trovato.")

        except Exception as e:
            # Stampa l'eccezione per diagnosticare il problema
            print(str(e))
            # Invia un messaggio all'utente
            dispatcher.utter_message(
                text="Si è verificato un errore. Riprova più tardi."
            )
