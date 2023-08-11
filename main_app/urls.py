from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chats/', views.chats_index, name='index'),
  path('chats/<int:chat_id>/', views.chats_detail, name='detail'),
  path('chats/create/', views.ChatCreate.as_view(), name='chats_create'),

  path('accounts/signup/', SignUpView.as_view(), name='signup'),
  path('myprofile/', views.viewProfile, name='view_profile'),
]
