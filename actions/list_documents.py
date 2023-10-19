
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from elasticsearch import Elasticsearch
from django.utils.safestring import mark_safe


class ActionListAllDocuments(Action):

    def name(self) -> str:
        return "action_list_all_documents"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:

        es = Elasticsearch(["http://localhost:9200"])

        try:
            # Eseguire una ricerca in Elasticsearch per ottenere tutti i documenti
            response = es.search(index="documenti", body={
                "query": {
                    "match_all": {}  # Questa query restituirà tutti i documenti
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
                dispatcher.utter_message(text=('\n'.join(response_texts)))
            else:
                dispatcher.utter_message(
                    text="Non ci sono documenti disponibili.")

        except Exception as e:
            # Stampa l'eccezione per diagnosticare il problema
            print("Errore dettagliato:", str(e))
            dispatcher.utter_message(
                text="Si è verificato un errore. Riprova più tardi.")
