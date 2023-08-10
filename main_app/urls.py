from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('chats/users', views.chats_users, name='users'),
    path('chats/user/<int:user_id>', views.chats_user_detail, name='detail'),
    path('chats/user/create', views.UserCreate.as_view(), name='user_create'),
    path('chats/user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('chats/user/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
]    
