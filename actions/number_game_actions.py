from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random


class ActionStartGame(Action):
    def name(self):
        return "action_start_game"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Genera un numero random tra 1 e 10 e lo salva come slot
        dispatcher.utter_message(
            text="Ho pensato a un numero tra 1 e 10. Prova a indovinarlo!"
        )
        number = random.randint(1, 10)
        return [SlotSet("secret_number", number), SlotSet("game_on", True)]


class ActionGuessNumber(Action):
    def name(self):
        return "action_guess_number"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        user_guess = tracker.get_slot("number")
        
        if user_guess is None or not user_guess.isdigit():
            dispatcher.utter_message(text="Mi scuso, non ho ricevuto un numero valido.")
            return []

        guess = int(user_guess)
        secret_number = tracker.get_slot("secret_number")

        if guess == secret_number:
            dispatcher.utter_message(text="Bravo! Hai indovinato!")
            return [SlotSet("game_on", False)]
        else:
            dispatcher.utter_message(text="Non è corretto. Prova ancora!")
            return []
