from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random


class ActionStartGame(Action):
    def name(self) -> str:
        return "action_start_game"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        # Genera un numero random tra 1 e 10 e lo salva come slot
        number = random.randint(1, 10)
        # dispatcher.utter_message(text=f"Ho pensato al numero {number}. Prova a indovinarlo!") # Aggiunto solo per debug, poi rimuovilo
        return [SlotSet("secret_number", number), SlotSet("game_on", True)]


class ActionGuessNumber(Action):
    def name(self) -> str:
        return "action_guess_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        guess = tracker.get_slot("number")
        print("Valore di 'number':", guess)
        if guess is None:
            dispatcher.utter_message(text="Mi scuso, non ho ricevuto un numero valido.")
            return []
        secret_number = tracker.get_slot("secret_number")
        # Stampa i valori dei slot
        print("Valore di 'number':", guess)
        if secret_number:
            print("Valore di 'secret_number':", secret_number)
        else:
            print("Valore di 'secret_number' non trovato.")
        if secret_number is None:
            dispatcher.utter_message(text="Mi scuso, non riesco a trovare il numero segreto. Inizia di nuovo il gioco.")
            return []

        # Convert slots to integers
        guess = int(guess)
        secret_number = int(secret_number)

        # Printing the values and their types
        print(f"User's Guess: {guess}, Type: {type(guess)}")
        print(f"Secret Number: {secret_number}, Type: {type(secret_number)}")

        if guess == secret_number:
            dispatcher.utter_message(text="Bravo! Hai indovinato!")
            return [SlotSet("game_on", False)]
        else:
            dispatcher.utter_message(text="Non è corretto. Prova ancora!")
            return []
