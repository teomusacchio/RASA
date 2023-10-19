from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test success!")

# @login_required
def chat_view(request):
    return render(request, 'chat.html')


def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get("message")

        # Comunicare con RASA API
        try:
            rasa_response = requests.post(
                "http://localhost:5005/webhooks/rest/webhook", json={"message": user_message})
            rasa_response.raise_for_status()

            response_data = rasa_response.json()
            if response_data and 'text' in response_data[0]:
                bot_message = response_data[0]["text"]
                return JsonResponse({"message": bot_message})
            else:
                return JsonResponse({"error": "Struttura della risposta inaspettata"})
        except requests.RequestException as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Metodo non supportato"})
