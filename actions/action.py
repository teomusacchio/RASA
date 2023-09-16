from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckPersonName(Action):

    def name(self) -> Text:
        return "action_check_person_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Dizionario con informazioni specifiche per ogni nome
        people_info = {
            "Mario Rossi": "Mario Rossi è un ingegnere con oltre 10 anni di esperienza.",
            "Giuseppe Verdi": "Giuseppe Verdi è un famoso compositore italiano.",
            "Anna Bianchi": "Anna Bianchi lavora nel settore marketing da 5 anni."
        }

        person_name = tracker.get_slot("person_name")

        response = people_info.get(person_name, "Mi dispiace, ma non ho informazioni al riguardo.")

        dispatcher.utter_message(text=response)

        return []

