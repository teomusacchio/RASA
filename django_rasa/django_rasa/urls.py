from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rasa/', include('rasa_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
