from django.urls import path, include
from django.contrib import admin
from rasa_app import views
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('rasa/', include('rasa_app.urls')),
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),

]
