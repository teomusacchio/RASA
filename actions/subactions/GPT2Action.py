# actions.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionGPT2Response(Action):
    def name(self):
        return "action_gpt2_response"

    def run(self, dispatcher, tracker, domain):
        # Carica il modello e il tokenizer (puoi anche farlo all'avvio per ottimizzare)
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
        model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

        # Prendi l'ultimo messaggio dell'utente
        user_message = tracker.latest_message['text']

        # Usa GPT-2 per generare una risposta
        input_ids = tokenizer.encode(user_message, return_tensors="pt")
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

        # Invia la risposta all'utente
        dispatcher.utter_message(response)
