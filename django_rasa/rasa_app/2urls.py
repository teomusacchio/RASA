from django.urls import path, include

urlpatterns = [
    path('django_rasa/', include('rasa_app.django_rasa_urls')),
]
