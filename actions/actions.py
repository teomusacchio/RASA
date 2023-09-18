import sqlite3
# import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#from number_game_actions import ActionGuessNumber, ActionStartGame


class ActionCheckPersonName(Action):

    def name(self) -> Text:
        return "action_check_person_name"

    def get_person_info(self, name: str) -> str:
        # Connetti al database
        conn = sqlite3.connect('people_database.db')
        cursor = conn.cursor()

        # Cerca il nome nel database
        cursor.execute("SELECT info FROM people WHERE name=?", (name,))
        result = cursor.fetchone()

        conn.close()

        if result:
            return result[0]
        else:
            return None

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        person_name = tracker.get_slot("person_name").lower()
        print(f"---- DEBUGGING ----\nValore estratto"
              "per 'person_name': {person_name}")

        info = self.get_person_info(person_name)

        if info:
            response = f"Conosco {person_name}! {info}"
        else:
            response = f"Mi dispiace, ma non ho informazioni su {person_name}."

        print(f"Risposta generata: {response}")
        dispatcher.utter_message(text=response)

        return []
