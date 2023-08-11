import os
import uuid
import boto3
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Conversation
from django.contrib.auth.models import User

def conversations(request):
   conversations= Conversation.objects.all()
   return render(request, "conversations_index.html",{"conversations":conversations})

class GroupDetail(DetailView):
  model = Conversation

def conversation_detail(request, conversation_id):
  conversation = Conversation.objects.get(id=conversation_id)
  return render(request, 'conversation_detail.html',{"conversation":conversation})
# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def group_detail(request, group_id):
  conversation = Conversation.objects.get(id=group_id)
  name_list = conversation.user.all().values_list('username')
  users_part_of_group = conversation.user.all().values()
  users_doesnt_belong_to_conversation = User.objects.exclude(username__in=name_list)
  return render(request, 'conversation/detail.html', {
    'conversation': conversation,
    'conversationUsers':users_part_of_group,
    'users': users_doesnt_belong_to_conversation
  })

class ChatGroupCreate(LoginRequiredMixin, CreateView):
  model = Conversation
  fields = ['chat_type','status','description']

class ConversationStatusUpdate(LoginRequiredMixin, UpdateView):
  model = Conversation
  fields = ['chat_type','status','description']

class ConversationDelete(LoginRequiredMixin, DeleteView):
  model = Conversation
  success_url = '/conversations'

@login_required
def assoc_user(request, group_id, username):
  user = User.objects.get(username=username)
  Conversation.objects.get(id=group_id).user.add(user)
  return redirect('conversation_detail', group_id=group_id)

@login_required
def unassoc_user(request, group_id, username):
  user = User.objects.get(username=username)
  Conversation.objects.get(id=group_id).user.remove(user)
  return redirect('conversation_detail', group_id=group_id)

class SignUpView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    # print(form)
    if form.is_valid():
      # Save the user to the db
      
      user = form.save()
      print(user)
      # Automatically log in the new user
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup template
  form = UserCreationForm()
  form = RegisterForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def chats_index(request):
  cats = Cat.objects.all()
  return render(request, 'chats/index.html', {
    'cats': cats
  })

@login_required
def chats_detail(request, chat_id):
  chat = Chat.objects.get(id=chat_id)
  # First, create a list of the toy ids that the cat DOES have
  id_list = chat.toys.all().values_list('id')
  # Query for the toys that the cat doesn't have
  # by using the exclude() method vs. the filter() method
  toys_chat_doesnt_have = Toy.objects.exclude(id__in=id_list)
  # instantiate FeedingForm to be rendered in detail.html
  feeding_form = FeedingForm()
  return render(request, 'chats/detail.html', {
    'chat': chat, 'feeding_form': feeding_form
  })

@login_required
def viewProfile(request):
   user = request.user
   return render(request, 'user/profile.html', {'user':user})
