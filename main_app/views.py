from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User



def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def chats_users(request):
   users = User.objects.all()
   return render(request, "chats/users.html", {
    'users': users
  })

class UserCreate(CreateView):
  model = User
  fields = ['first_name', 'last_name', 'email', 'last_active']

class UserUpdate(UpdateView):
  model = User
  fields = ['first_name', 'last_name', 'email', 'last_active']

class UserDelete(DeleteView):
  model = User
  success_url = '/chats/users'

def chats_user_detail(request, user_id):
  user = User.objects.get(id=user_id)
  return render(request, "chats/userDetail.html", {"user": user})