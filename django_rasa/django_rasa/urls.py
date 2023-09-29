from django.urls import path, include

urlpatterns = [
    path('rasa/', include('rasa_app.urls')),
]
