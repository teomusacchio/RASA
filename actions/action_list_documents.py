from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from elasticsearch import Elasticsearch


class ActionListAllDocuments(Action):

    def name(self) -> str:
        return "action_list_all_documents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: dict) -> list:

        es = Elasticsearch(["http://localhost:9200"])

        try:
            response = es.search(index="documenti", body={
                "query": {
                    "match_all": {}
                }
            })

            hits = response.get('hits', {}).get('hits', [])

            if hits:
                response_texts = []
                for index, hit in enumerate(hits, start=1):
                    doc_info = hit['_source']['nome_documento']
                    link = hit['_source']['url_documento']
                    text = f"Documento: {doc_info}. Link: <a href='{link}' target='_blank' rel='noopener noreferrer'>Clicca qui</a>"

                    response_texts.append(text)

                # Unisci i risultati in un singolo messaggio
                formatted_response = "".join(response_texts)
                dispatcher.utter_message(text=formatted_response)
            else:
                dispatcher.utter_message(
                    text="Non ci sono documenti disponibili.")
        except Exception as e:
            print("Errore dettagliato:", str(e))
            dispatcher.utter_message(
                text="Si è verificato un errore. Riprova più tardi.")
