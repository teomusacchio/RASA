from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views_crawler import search_view, download_file
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('chat/', views.chat_view, name='chat_view'),
    path('api/chatbot/', views.chatbot_response, name='chatbot_response'),
    path('search/', search_view, name='search_view'),
    path('download/<path:file_path>/', download_file, name='download_file'),
    path('test/', views.test_view, name='test_view'),

]
