from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('chats/', views.chats_index, name='index'),
    path('chats/', views.chats_detail, name='detail'),
    path('conversations/', views.conversations, name='conversations'),
    path('conversations/<int:conversation_id>/', views.conversations_detail, name='conversationdetail'),
]    
