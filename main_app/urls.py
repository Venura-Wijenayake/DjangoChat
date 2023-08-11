from django.contrib import admin
from django.urls import path
from . import views
from .views import SignUpView
from main_app.views import *

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('chats/', views.chats_index, name='index'),
  path('chats/<int:cat_id>/', views.chats_detail, name='detail'),
  path('accounts/signup/', SignUpView.as_view(), name='signup'),
  path('myprofile/', views.viewProfile, name='view_profile'),

#TAVY FORUM CODE
  path('admin/', admin.site.urls),
  path('',home,name='home'),
  path('addInForum/',addInForum,name='addInForum'),
  path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),

]
