from django.shortcuts import render
import requests
from django.http import JsonResponse


def chat_view(request):
    return render(request, 'chat.html')


def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get("message")
        
        # Comunicare con RASA API
        rasa_response = requests.post("http://localhost:5005"
                                      "/webhooks/rest/webhook",
                                      json={"message": user_message})
        
        # Prendere la risposta dal bot
        bot_message = rasa_response.json()[0]["text"]
        
        return JsonResponse({"message": bot_message})

    return JsonResponse({"error": "Metodo non supportato"})
# Create your views here.
