from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet

class ActionCheckPersonName(Action):

    def name(self) -> Text:
        return "action_check_person_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        person_name = tracker.get_slot("person_name")
        print(f"---- DEBUGGING ----\nValore estratto per 'person_name': {person_name}")
    

        # Qui puoi definire una lista di nomi che il bot riconosce
        known_names = ["Mario Rossi", "Giuseppe Verdi", "Anna Bianchi"]

        person_name = tracker.get_slot("person_name")
        
        # Aggiungi le seguenti righe:
        print("---- DEBUGGING ----")
        print(f"Valore estratto per 'person_name': {person_name}")

        if person_name in known_names:
            response = f"Conosco {person_name}! È nel nostro database."
        else:
            response = f"Mi dispiace, ma non ho informazioni su {person_name}."            
        # Aggiungi anche questo:
        print(f"Risposta generata: {response}")
    
        dispatcher.utter_message(text=response)
        return []

