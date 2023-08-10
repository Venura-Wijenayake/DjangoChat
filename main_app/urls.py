from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('chats/', views.chats_index, name='index'),
    path('chats/', views.chats_detail, name='detail'),
    path('conversations/', views.conversations, name='conversations'),
    path('conversations/<int:conversation_id>/', views.conversations_detail, name='conversationdetail'),
    path('conversations/<int:conversation_id>/assoc_user/<int:user_id>/', views.assoc_user, name='assoc_user'),
    path('conversations/<int:conversation_id>/unassoc_user/<int:user_id>/', views.unassoc_user, name='unassoc_user'),
   

]    
