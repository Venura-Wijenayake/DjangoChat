from django.shortcuts import render #, redirect
from .models import Conversation,User,Event,Message

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def chats_index(request):
   return render(request, "chats/index.html")

def chats_detail(request):
   return render(request, "chats/detail.html")

def conversations(request):
   conversations= Conversation.objects.all()
   return render(request, "conversations_index.html",{"conversations":conversations})

def conversations_detail(request, conversation_id):
  conversation = Conversation.objects.get(id=conversation_id)
  return render(request, 'conversations_detail.html',{"conversation":conversation})