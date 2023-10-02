from elasticsearch import Elasticsearch
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckPersonName(Action):

    def name(self) -> Text:
        return "action_check_person_name"

    def get_person_info(self, name: str) -> str:
        # Connetti al cluster di Elasticsearch
        es = Elasticsearch(
            hosts=[{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
        # Cerca il nome in Elasticsearch
        result = es.search(index="people", body={
            "query": {
                "match": {
                    "name": name
                }
            }
        })

        hits = result['hits']['hits']

        if hits:
            return hits[0]['_source']['info']
        else:
            return None

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        person_name = tracker.get_slot("person_name")
        print(tracker.current_state())
        if person_name:
            person_name = person_name.lower()
            print(
                "---- DEBUGGING ----\nValore estratto per"
                "'person_name': {person_name}")
            info = self.get_person_info(person_name)

            if info:
                response = f"Conosco {person_name}! {info}"
            else:
                response = "Mi dispiace, ma non ho"
                "informazioni su {person_name}."
        else:
            response = "Mi dispiace, ma non ho ricevuto un nome valido."

        print(f"Risposta generata: {response}")
        dispatcher.utter_message(text=response)

        return []
