from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from haystack import Finder
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.retriever.sparse import ElasticsearchRetriever

class ActionCheckPersonName(Action):

    def name(self) -> str:
        return "action_check_person_name"

    def __init__(self):
        # Configurazione di Haystack per lavorare con Elasticsearch
        self.document_store = ElasticsearchDocumentStore(host="localhost", index="people")
        self.retriever = ElasticsearchRetriever(document_store=self.document_store)
        self.finder = Finder(reader=None, retriever=self.retriever)

    def get_person_info(self, name: str) -> str:
        # Utilizza Haystack per effettuare la ricerca
        results = self.finder.get_answers_via_similar_questions(question=name, top_k_retriever=1)

        if results and results['answers']:
            return results['answers'][0]['answer']
        else:
            return None

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        person_name = tracker.get_slot("person_name").lower()
        print(f"---- DEBUGGING ----\nValore estratto per 'person_name': {person_name}")

        info = self.get_person_info(person_name)

        if info:
            response = f"Conosco {person_name}! {info}"
        else:
            response = f"Mi dispiace, ma non ho informazioni su {person_name}."

        print(f"Risposta generata: {response}")
        dispatcher.utter_message(text=response)

        return []

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from haystack import Finder
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.retriever.sparse import ElasticsearchRetriever

class ActionCheckPersonName(Action):

    def name(self) -> str:
        return "action_check_person_name"

    def __init__(self):
        # Configurazione di Haystack per lavorare con Elasticsearch
        self.document_store = ElasticsearchDocumentStore(host="localhost", index="people")
        self.retriever = ElasticsearchRetriever(document_store=self.document_store)
        self.finder = Finder(reader=None, retriever=self.retriever)

    def get_person_info(self, name: str) -> str:
        # Utilizza Haystack per effettuare la ricerca
        results = self.finder.get_answers_via_similar_questions(question=name, top_k_retriever=1)

        if results and results['answers']:
            return results['answers'][0]['answer']
        else:
            return None

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        person_name = tracker.get_slot("person_name").lower()
        print(f"---- DEBUGGING ----\nValore estratto per 'person_name': {person_name}")

        info = self.get_person_info(person_name)

        if info:
            response = f"Conosco {person_name}! {info}"
        else:
            response = f"Mi dispiace, ma non ho informazioni su {person_name}."

        print(f"Risposta generata: {response}")
        dispatcher.utter_message(text=response)

        return []

        return []
