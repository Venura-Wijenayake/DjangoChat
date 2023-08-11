from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chats/', views.chats_index, name='index'),
  path('myprofile/', views.viewProfile, name='view_profile'),
  path('chats/<int:cat_id>/', views.chats_detail, name='detail'),
  path('chats/create/', views.ChatCreate.as_view(), name='chats_create'),
  path('chats/<int:pk>/update/', views.ChatUpdate.as_view(), name='chats_update'),
  path('chats/<int:pk>/delete/', views.ChatDelete.as_view(), name='chats_delete'),
  # path('chats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  # path('chats/<int:chat_id>/add_photo/', views.add_photo, name='add_photo'),
  # path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  # path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
  # path('toys/', views.ToyList.as_view(), name='toys_index'),
  # path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  # path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  # path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  # path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
 
  path('accounts/signup/', SignUpView.as_view(), name='signup'),
  # path('register/', views.sign_up, name='register'),

]
