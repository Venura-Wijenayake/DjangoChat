from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('chats/', views.chats_index, name='index'),
    path('chats/', views.chats_detail, name='detail'),
    path('conversations/', views.conversations_index, name='conversation_index'),
]    
