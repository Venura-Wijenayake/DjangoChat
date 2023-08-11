from django.urls import path
from . import views
 
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chatgroup/create/', views.ChatGroupCreate.as_view(), name='chatgroup_create'),
  path('conversations/', views.conversations, name='conversations'),
  # //path('conversations/<int:pk>/', views.GroupDetail.as_view(), name='conversation_detail'),
  path('conversations/<int:group_id>/', views.group_detail, name='conversation_detail'),
  path('conversations/<int:pk>/delete', views.ConversationDelete.as_view(), name='conversation_delete'),
  path('conversations/<int:pk>/update/', views.ConversationStatusUpdate.as_view(), name='conversations_status_update'),
  path('conversations/<int:group_id>/assoc_user/<str:username>/', views.assoc_user, name='assoc_user'),
  path('conversations/<int:group_id>/unassoc_user/<str:username>/', views.unassoc_user, name='unassoc_user'),
  path('accounts/signup/', views.signup, name='signup'),
]
